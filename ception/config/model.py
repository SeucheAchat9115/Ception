from dataclasses import dataclass
from typing import Any


@dataclass
class ModelConfig:
    """Configuration class for the model settings"""

    name: str | None
    backbone: str | None
    num_classes: int | None
    pretrained: bool | None

    @classmethod
    def from_dict(cls, config_data: dict[str, Any]) -> "ModelConfig":
        """
        Load configuration from a dictionary

        Args:
            config_data (dict): Dictionary containing the configuration

        Returns:
            ModelConfig: Configuration object
        """
        return cls(
            name=config_data.get("name"),
            backbone=config_data.get("backbone"),
            num_classes=config_data.get("num_classes"),
            pretrained=config_data.get("pretrained"),
        )
