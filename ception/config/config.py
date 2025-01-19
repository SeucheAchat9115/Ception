from dataclasses import dataclass
from typing import Any

from ception.config.data import DataConfig
from ception.config.evaluation import EvaluationConfig
from ception.config.experiment import ExperimentConfig
from ception.config.model import ModelConfig
from ception.config.training import TrainingConfig
from ception.config.utils import UtilsConfig
from ception.data.io.reading.yaml import read_yaml_file


@dataclass
class Config:
    """Configuration class for all the settings"""

    data: DataConfig
    model: ModelConfig
    experiment: ExperimentConfig
    training: TrainingConfig
    evaluation: EvaluationConfig
    utils: UtilsConfig

    @classmethod
    def from_yaml(cls, yaml_path: str) -> "Config":
        """
        Load configuration from a yaml file

        Args:
            yaml_path (str): Path to the yaml file

        Returns:
            Config: Configuration object
        """
        config_data = read_yaml_file(yaml_path)
        return cls.from_dict(config_data)

    @classmethod
    def from_dict(cls, config_data: dict[str, Any]) -> "Config":
        """
        Load configuration from a dictionary

        Args:
            config_data (dict): Dictionary containing the configuration

        Returns:
            Config: Configuration object
        """
        return cls(
            data=DataConfig.from_dict(config_data.get("data", {})),
            model=ModelConfig.from_dict(config_data.get("model", {})),
            experiment=ExperimentConfig.from_dict(config_data.get("experiment", {})),
            training=TrainingConfig.from_dict(config_data.get("training", {})),
            evaluation=EvaluationConfig.from_dict(config_data.get("evaluation", {})),
            utils=UtilsConfig.from_dict(config_data.get("utils", {})),
        )

    @classmethod
    def from_default(cls) -> "Config":
        """
        Load default configuration

        Returns:
            Config: Configuration object
        """
        return cls.from_dict({})
