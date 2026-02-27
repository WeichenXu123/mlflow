import pytest

import mlflow


@pytest.fixture
def reset_active_experiment():
    yield
    mlflow.tracking.fluent._active_experiment_id = None
    mlflow.tracking.fluent._experiment_id_env_cache.clear()
