from dataclasses import dataclass
from typing import Any


@dataclass
class EvaluationConfig:
    """Configuration class for the evaluation settings"""

    metric_name: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "EvaluationConfig":
        """
        Create an EvaluationConfig object from a dictionary

        Args:
            data (dict): Dictionary containing the configuration settings

        Returns:
            EvaluationConfig: Configuration settings for the evaluation
        """
        return cls(**data)
