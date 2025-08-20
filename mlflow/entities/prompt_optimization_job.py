import json
from enum import Enum
from typing import Any, Dict, List, Optional

from mlflow.entities._mlflow_object import _MlflowObject
from mlflow.protos.service_pb2 import PromptOptimizationJob as ProtoPromptOptimizationJob


class PromptOptimizationJobStatus(Enum):
    """Status of a prompt optimization job."""
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class PromptOptimizationJob(_MlflowObject):
    """Prompt optimization job entity."""

    def __init__(
        self,
        job_id: str,
        dataset_url: str,
        prompt_url: str,
        scorer_names: List[str],
        config: Dict[str, Any],
        status: PromptOptimizationJobStatus,
        creation_time: int,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        result: Optional[Dict[str, Any]] = None,
        error_message: Optional[str] = None,
        progress: Optional[float] = None,
    ):
        self._job_id = job_id
        self._dataset_url = dataset_url
        self._prompt_url = prompt_url
        self._scorer_names = scorer_names
        self._config = config
        self._status = status
        self._creation_time = creation_time
        self._start_time = start_time
        self._end_time = end_time
        self._result = result
        self._error_message = error_message
        self._progress = progress

    @property
    def job_id(self) -> str:
        """Unique identifier for the job."""
        return self._job_id

    @property
    def dataset_url(self) -> str:
        """URL or path to the evaluation dataset."""
        return self._dataset_url

    @property
    def prompt_url(self) -> str:
        """URL or path to the original prompt."""
        return self._prompt_url

    @property
    def scorer_names(self) -> List[str]:
        """List of scorer names to use for evaluation."""
        return self._scorer_names

    @property
    def config(self) -> Dict[str, Any]:
        """Configuration for the optimization job."""
        return self._config

    @property
    def status(self) -> PromptOptimizationJobStatus:
        """Current status of the job."""
        return self._status

    @property
    def creation_time(self) -> int:
        """Timestamp when the job was created."""
        return self._creation_time

    @property
    def start_time(self) -> Optional[int]:
        """Timestamp when the job started running."""
        return self._start_time

    @property
    def end_time(self) -> Optional[int]:
        """Timestamp when the job completed."""
        return self._end_time

    @property
    def result(self) -> Optional[Dict[str, Any]]:
        """Result of the optimization job."""
        return self._result

    @property
    def error_message(self) -> Optional[str]:
        """Error message if the job failed."""
        return self._error_message

    @property
    def progress(self) -> Optional[float]:
        """Progress of the job as a percentage (0.0 to 1.0)."""
        return self._progress

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "job_id": self.job_id,
            "dataset_url": self.dataset_url,
            "prompt_url": self.prompt_url,
            "scorer_names": self.scorer_names,
            "config": self.config,
            "status": self.status.value,
            "creation_time": self.creation_time,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "result": self.result,
            "error_message": self.error_message,
            "progress": self.progress,
        }

    @classmethod
    def from_proto(cls, proto):
        """Create a PromptOptimizationJob from a protobuf message."""
        return cls(
            job_id=proto.job_id,
            dataset_url=proto.dataset_url,
            prompt_url=proto.prompt_url,
            scorer_names=list(proto.scorer_names),
            config=json.loads(proto.config) if proto.config else {},
            status=PromptOptimizationJobStatus(proto.status),
            creation_time=proto.creation_time,
            start_time=proto.start_time if proto.HasField("start_time") else None,
            end_time=proto.end_time if proto.HasField("end_time") else None,
            result=json.loads(proto.result) if proto.result else None,
            error_message=proto.error_message if proto.HasField("error_message") else None,
            progress=proto.progress if proto.HasField("progress") else None,
        )

    def to_proto(self):
        """Convert this PromptOptimizationJob to a protobuf message."""
        proto = ProtoPromptOptimizationJob()
        proto.job_id = self.job_id
        proto.dataset_url = self.dataset_url
        proto.prompt_url = self.prompt_url
        proto.scorer_names.extend(self.scorer_names)
        proto.config = json.dumps(self.config) if self.config else ""
        proto.status = self.status.value
        proto.creation_time = self.creation_time
        if self.start_time is not None:
            proto.start_time = self.start_time
        if self.end_time is not None:
            proto.end_time = self.end_time
        if self.result is not None:
            proto.result = json.dumps(self.result)
        if self.error_message is not None:
            proto.error_message = self.error_message
        if self.progress is not None:
            proto.progress = self.progress
        return proto

    def __repr__(self):
        return (
            f"<PromptOptimizationJob(job_id='{self.job_id}', "
            f"status='{self.status.value}', "
            f"prompt_url='{self.prompt_url}')>"
        )
