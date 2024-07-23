import { Button, DropdownMenu, Typography, useDesignSystemTheme } from '@databricks/design-system';
import { useCallback, useMemo } from 'react';
import { ReactComponent as ParallelChartSvg } from '../../../../../common/static/parallel-chart-placeholder.svg';
import type { RunsChartsRunData } from '../RunsCharts.common';
import LazyParallelCoordinatesPlot, { processParallelCoordinateData } from '../charts/LazyParallelCoordinatesPlot';
import { useRunsChartsTooltip } from '../../hooks/useRunsChartsTooltip';
import type { RunsChartsParallelCardConfig } from '../../runs-charts.types';
import {
  type RunsChartCardReorderProps,
  RunsChartCardWrapper,
  RunsChartsChartsDragGroup,
  RunsChartCardFullScreenProps,
} from './ChartCard.common';
import { useIsInViewport } from '../../hooks/useIsInViewport';
import {
  shouldEnableHidingChartsWithNoData,
  shouldUseNewRunRowsVisibilityModel,
} from '../../../../../common/utils/FeatureUtils';
import { FormattedMessage } from 'react-intl';
import { useUpdateExperimentViewUIState } from '../../../experiment-page/contexts/ExperimentPageUIStateContext';
import { downloadChartDataCsv } from '../../../experiment-page/utils/experimentPage.common-utils';
import type { RunsGroupByConfig } from '../../../experiment-page/utils/experimentPage.group-row-utils';
import { RunsChartsNoDataFoundIndicator } from '../RunsChartsNoDataFoundIndicator';

export interface RunsChartsParallelChartCardProps extends RunsChartCardReorderProps, RunsChartCardFullScreenProps {
  config: RunsChartsParallelCardConfig;
  chartRunData: RunsChartsRunData[];

  hideEmptyCharts?: boolean;

  onDelete: () => void;
  onEdit: () => void;
  groupBy: RunsGroupByConfig | null;
}

/**
 * A placeholder component displayed before parallel coords chart is being configured by user
 */
const NotConfiguredParallelCoordsPlaceholder = ({ onEdit }: { onEdit: () => void }) => {
  const { theme } = useDesignSystemTheme();

  return (
    <div css={{ display: 'flex', flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <div css={{ display: 'flex', flexDirection: 'column', alignItems: 'center', maxWidth: 360 }}>
        <ParallelChartSvg />
        <Typography.Title css={{ marginTop: theme.spacing.md }} color="secondary" level={3}>
          <FormattedMessage
            defaultMessage="Compare parameter importance"
            description="Experiment page > compare runs > parallel coordinates chart > chart not configured warning > title"
          />
        </Typography.Title>
        <Typography.Text css={{ marginBottom: theme.spacing.md }} color="secondary">
          <FormattedMessage
            defaultMessage="Use the parallel coordinates chart to compare how various parameters in model affect your model metrics."
            description="Experiment page > compare runs > parallel coordinates chart > chart not configured warning > description"
          />
        </Typography.Text>
        <Button componentId="mlflow.charts.parallel_coords_chart_configure_button" type="primary" onClick={onEdit}>
          <FormattedMessage
            defaultMessage="Configure chart"
            description="Experiment page > compare runs > parallel coordinates chart > configure chart button"
          />
        </Button>
      </div>
    </div>
  );
};

/**
 * A placeholder component displayed before parallel coords chart is being configured by user
 */
const UnsupportedDataPlaceholder = () => {
  const { theme } = useDesignSystemTheme();

  return (
    <div css={{ display: 'flex', flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <div css={{ display: 'flex', flexDirection: 'column', alignItems: 'center', maxWidth: 360 }}>
        <ParallelChartSvg />
        <Typography.Title css={{ marginTop: theme.spacing.md, textAlign: 'center' }} color="secondary" level={3}>
          <FormattedMessage
            defaultMessage="Parallel coordinates chart does not support aggregated string values."
            description="Experiment page > compare runs > parallel coordinates chart > unsupported string values warning > title"
          />
        </Typography.Title>
        <Typography.Text css={{ marginBottom: theme.spacing.md }} color="secondary">
          <FormattedMessage
            defaultMessage="Use other parameters or disable run grouping to continue."
            description="Experiment page > compare runs > parallel coordinates chart > unsupported string values warning > description"
          />
        </Typography.Text>
      </div>
    </div>
  );
};

export const RunsChartsParallelChartCard = ({
  config,
  chartRunData,
  onDelete,
  onEdit,
  groupBy,
  fullScreen,
  setFullScreenChart,
  hideEmptyCharts,
  ...reorderProps
}: RunsChartsParallelChartCardProps) => {
  const updateUIState = useUpdateExperimentViewUIState();

  const toggleFullScreenChart = () => {
    setFullScreenChart?.({
      config,
      title: 'Parallel Coordinates',
      subtitle: displaySubtitle ? subtitle : null,
    });
  };

  const configuredChartRunData = useMemo(() => {
    if (!shouldUseNewRunRowsVisibilityModel() || config?.showAllRuns) {
      return chartRunData;
    }
    return chartRunData?.filter(({ hidden }) => !hidden);
  }, [chartRunData, config?.showAllRuns]);

  const containsStringValues = useMemo(
    () =>
      config.selectedParams?.some(
        (paramKey) => configuredChartRunData?.some((dataTrace) => isNaN(Number(dataTrace.params[paramKey]?.value))),
        [config.selectedParams, configuredChartRunData],
      ),
    [config.selectedParams, configuredChartRunData],
  );

  const updateVisibleOnlySetting = useCallback(
    (showAllRuns: boolean) => {
      updateUIState((state) => {
        const newCompareRunCharts = state.compareRunCharts?.map((existingChartConfig) => {
          if (existingChartConfig.uuid === config.uuid) {
            const parallelChartConfig = existingChartConfig as RunsChartsParallelCardConfig;
            return { ...parallelChartConfig, showAllRuns };
          }
          return existingChartConfig;
        });

        return { ...state, compareRunCharts: newCompareRunCharts };
      });
    },
    [config.uuid, updateUIState],
  );

  const [isConfigured, parallelCoordsData] = useMemo(() => {
    const selectedParamsCount = config.selectedParams?.length || 0;
    const selectedMetricsCount = config.selectedMetrics?.length || 0;

    const configured = selectedParamsCount + selectedMetricsCount >= 2;

    // Prepare the data in the parcoord-es format
    const data = configured
      ? processParallelCoordinateData(configuredChartRunData, config.selectedParams, config.selectedMetrics)
      : [];

    return [configured, data];
  }, [config, configuredChartRunData]);

  const isEmptyDataset = useMemo(() => {
    return shouldEnableHidingChartsWithNoData() && parallelCoordsData.length === 0;
  }, [parallelCoordsData]);

  const { elementRef, isInViewport } = useIsInViewport();

  const { setTooltip, resetTooltip, selectedRunUuid, closeContextMenu } = useRunsChartsTooltip(config);

  const containsUnsupportedValues = containsStringValues && groupBy;
  const displaySubtitle = isConfigured && !containsUnsupportedValues;

  const subtitle = shouldUseNewRunRowsVisibilityModel() ? (
    <>
      {config.showAllRuns ? (
        <FormattedMessage
          defaultMessage="Showing all runs"
          description="Experiment page > compare runs > parallel chart > header > indicator for all runs shown"
        />
      ) : (
        <FormattedMessage
          defaultMessage="Showing only visible runs"
          description="Experiment page > compare runs > parallel chart > header > indicator for only visible runs shown"
        />
      )}
    </>
  ) : (
    <>Comparing {parallelCoordsData.length} runs</>
  );

  const chartBody = (
    <>
      {!isConfigured ? (
        <NotConfiguredParallelCoordsPlaceholder onEdit={onEdit} />
      ) : containsUnsupportedValues ? (
        <UnsupportedDataPlaceholder />
      ) : parallelCoordsData.length === 0 ? (
        <RunsChartsNoDataFoundIndicator />
      ) : (
        // Avoid displaying empty set, otherwise parcoord-es goes crazy
        <div
          css={[
            styles.parallelChartCardWrapper,
            {
              height: fullScreen ? '100%' : undefined,
            },
          ]}
          ref={elementRef}
        >
          {isInViewport ? (
            <LazyParallelCoordinatesPlot
              data={parallelCoordsData}
              selectedParams={config.selectedParams}
              selectedMetrics={config.selectedMetrics}
              onHover={setTooltip}
              onUnhover={resetTooltip}
              axesRotateThreshold={8}
              selectedRunUuid={selectedRunUuid}
              closeContextMenu={closeContextMenu}
            />
          ) : null}
        </div>
      )}
    </>
  );

  if (fullScreen) {
    return chartBody;
  }

  // Do not render the card if the chart is empty and the user has enabled hiding empty charts
  if (hideEmptyCharts && isEmptyDataset) {
    return null;
  }

  const fullScreenEnabled = isConfigured && !containsUnsupportedValues && !isEmptyDataset;

  return (
    <RunsChartCardWrapper
      onEdit={onEdit}
      onDelete={onDelete}
      title="Parallel Coordinates"
      subtitle={displaySubtitle ? subtitle : null}
      uuid={config.uuid}
      tooltip="The Parallel Coordinates Chart now only shows runs with columns that are either numbers or strings. If a column has string entries, the runs corresponding to the 30 most recent unique values will be shown."
      dragGroupKey={RunsChartsChartsDragGroup.PARALLEL_CHARTS_AREA}
      // Disable fullscreen button if the chart is empty
      toggleFullScreenChart={fullScreenEnabled ? toggleFullScreenChart : undefined}
      additionalMenuContent={
        shouldUseNewRunRowsVisibilityModel() ? (
          <>
            <DropdownMenu.Separator />
            <DropdownMenu.CheckboxItem checked={!config.showAllRuns} onClick={() => updateVisibleOnlySetting(false)}>
              <DropdownMenu.ItemIndicator />
              <FormattedMessage
                defaultMessage="Show only visible"
                description="Experiment page > compare runs tab > chart header > move down option"
              />
            </DropdownMenu.CheckboxItem>
            <DropdownMenu.CheckboxItem checked={config.showAllRuns} onClick={() => updateVisibleOnlySetting(true)}>
              <DropdownMenu.ItemIndicator />
              <FormattedMessage
                defaultMessage="Show all runs"
                description="Experiment page > compare runs tab > chart header > move down option"
              />
            </DropdownMenu.CheckboxItem>
          </>
        ) : null
      }
      supportedDownloadFormats={['csv']}
      onClickDownload={(format) => {
        const savedChartTitle = [...config.selectedMetrics, ...config.selectedParams].join('-');

        if (format === 'csv') {
          downloadChartDataCsv(configuredChartRunData, config.selectedMetrics, config.selectedParams, savedChartTitle);
        }
      }}
      {...reorderProps}
    >
      {chartBody}
    </RunsChartCardWrapper>
  );
};

const styles = {
  parallelChartCardWrapper: {
    // Set "display: flex" here (and "flex: 1" in the child element)
    // so the chart will grow in width and height
    display: 'flex',
    overflow: 'hidden',
    cursor: 'pointer',
  },
};
