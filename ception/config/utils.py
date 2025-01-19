from dataclasses import dataclass
from typing import Any


@dataclass
class UtilsConfig:
    """Configuration class for the utility settings"""

    seed: int | None
    device: str | None

    @classmethod
    def from_dict(cls, config_data: dict[str, Any]) -> "UtilsConfig":
        """
        Load configuration from a dictionary

        Args:
            config_data (dict): Dictionary containing the configuration

        Returns:
            UtilsConfig: Configuration object
        """
        return cls(
            seed=config_data.get("seed"),
            device=config_data.get("device"),
        )
