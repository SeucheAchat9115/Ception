from dataclasses import dataclass
from typing import Any


@dataclass
class ExperimentConfig:
    """Configuration class for the experiment settings"""

    name: str | None
    save_dir: str | None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ExperimentConfig":
        """
        Create an ExperimentConfig object from a dictionary

        Args:
            data (dict): Dictionary containing the configuration settings

        Returns:
            ExperimentConfig: Configuration settings for the experiment
        """
        return cls(**data)
