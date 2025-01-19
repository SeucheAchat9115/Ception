from dataclasses import dataclass
from typing import Any


@dataclass
class TrainingConfig:
    """Configuration class for the training settings"""

    epochs: int | None
    optimizer: str | None
    lr: float | None
    lr_scheduler: str | None

    @classmethod
    def from_dict(cls, config_data: dict[str, Any]) -> "TrainingConfig":
        """
        Load configuration from a dictionary

        Args:
            config_data (dict): Dictionary containing the configuration

        Returns:
            TrainingConfig: Configuration object
        """
        return cls(
            epochs=config_data.get("epochs"),
            optimizer=config_data.get("optimizer"),
            lr=config_data.get("lr"),
            lr_scheduler=config_data.get("lr_scheduler"),
        )
