from typing import Any

from ception.config.base import BaseConfig
from ception.config.check import is_yaml_config
from ception.config.data import DataConfig
from ception.config.evaluation import EvaluationConfig
from ception.config.experiment import ExperimentConfig
from ception.config.model import ModelConfig
from ception.config.training import TrainingConfig
from ception.config.utils import UtilsConfig
from ception.data.io.reading.yaml import read_yaml_file


class Config(BaseConfig):
    """Configuration class for all the settings"""

    data: DataConfig
    model: ModelConfig
    experiment: ExperimentConfig
    training: TrainingConfig
    evaluation: EvaluationConfig
    utils: UtilsConfig

    def __init__(
        self,
        config_data: dict[str, dict[str, Any]] | None = None,
    ) -> None:
        """
        Initialize the configuration for all the settings

        Args:
            config_data (dict): Dictionary containing the configuration settings
        """
        if config_data is None:
            # Load default values
            super().__init__(
                data=DataConfig(),
                model=ModelConfig(),
                experiment=ExperimentConfig(),
                training=TrainingConfig(),
                evaluation=EvaluationConfig(),
                utils=UtilsConfig(),
            )
        else:
            # Overwrite default values with values from config file
            super().__init__(
                data=DataConfig(**config_data["data"]),
                model=ModelConfig(**config_data["model"]),
                experiment=ExperimentConfig(**config_data["experiment"]),
                training=TrainingConfig(**config_data["training"]),
                evaluation=EvaluationConfig(**config_data["evaluation"]),
                utils=UtilsConfig(**config_data["utils"]),
            )

    @classmethod
    def from_yaml(self, yaml_path: str) -> "Config":
        """
        Load configuration from a yaml file

        Args:
            yaml_path (str): Path to the yaml file

        Returns:
            Config: Configuration object
        """
        config_data = read_yaml_file(yaml_path)
        return self(config_data)

    @classmethod
    def from_dict(self, config_data: dict[str, Any]) -> "Config":
        """
        Load configuration from a dictionary

        Args:
            config_data (dict): Dictionary containing the configuration

        Returns:
            Config: Configuration object
        """
        return self(config_data)

    @classmethod
    def from_default(self) -> "Config":
        """
        Load default configuration

        Returns:
            Config: Configuration object
        """
        return self()


def load_config(source: str | dict[str, str] | None = None) -> Config:
    """
    Load configuration settings from a source.

    Args:
        source (str | dict | None): Source of the configuration. This can be:
            - A string (path to a YAML file)
            - A dictionary (direct configuration data)
            - None (to load the default configuration)

    Returns:
        Config: Configuration settings
    """
    if source is None:
        print("CEPTION: Loading default configuration.")
        return Config.from_default()
    if isinstance(source, str):
        print(f"CEPTION: Loading configuration from '{source}'.")
        if is_yaml_config(source):
            return Config.from_yaml(source)
        raise ValueError("Unsupported file format. Must be a YAML file.")
    if isinstance(source, dict):
        print("CEPTION: Loading configuration from dictionary.")
        return Config.from_dict(source)
    raise ValueError("Unsupported source type. Must be None, str, or dict.")
