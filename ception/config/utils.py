"""Configuration classes for the settings"""

from typing import Any

from ception.io.reading.yaml import read_yaml_file


class BaseConfig:
    """Base class for the configuration settings"""

    def __init__(
        self,
        **kwargs: Any,
    ) -> None:
        """
        Initialize the base class for the configuration settings

        Args:
            **kwargs: Arbitrary keyword arguments
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """
        Pretty print the configuration object

        Returns:
            str: Pretty printed string of the configuration object
        """
        pretty_string = "\n"
        for key, value in self.__dict__.items():
            pretty_string += f"{key}:\n"
            for k, v in value.__dict__.items():
                if k != "self":
                    pretty_string += f"  {k}: {v}\n"
        pretty_string += "\n"
        return pretty_string


class ExperimentConfig(BaseConfig):
    """Configuration class for the experiment settings"""

    def __init__(
        self,
        name: str | None = None,
        save_dir: str | None = "./experiments/",
    ) -> None:
        """
        Initialize the configuration for the experiment settings

        Args:
            name (str): Name of the experiment
            save_dir (str): Directory to save the experiment results
        """
        super().__init__(name=name, save_dir=save_dir)


class ModelConfig(BaseConfig):
    """Configuration class for the model settings"""

    def __init__(
        self,
        name: str | None = None,
        backbone: str | None = None,
        num_classes: int | None = None,
        pretrained: bool | None = False,
    ) -> None:
        """
        Initialize the configuration for the model settings

        Args:
            name (str): Name of the model
            backbone (str): Name of the backbone architecture
            num_classes (int): Number of classes in the model
            pretrained (bool): Use pretrained weights
        """
        super().__init__(name=name, backbone=backbone, num_classes=num_classes, pretrained=pretrained)


class DataConfig(BaseConfig):
    """Configuration class for the data settings"""

    def __init__(
        self,
        train_dataset: str | None = None,
        train_batch_size: int | None = 2,
        val_dataset: str | None = None,
        val_batch_size: int | None = 2,
    ) -> None:
        """
        Initialize the configuration for the data settings

        Args:
            train_dataset (str): Name of the training dataset
            train_batch_size (int): Batch size for training
            val_dataset (str): Name of the validation dataset
            val_batch_size (int): Batch size for validation
        """
        super().__init__(
            train_dataset=train_dataset,
            train_batch_size=train_batch_size,
            val_dataset=val_dataset,
            val_batch_size=val_batch_size,
        )


class TrainingConfig(BaseConfig):
    """Configuration class for the training settings"""

    def __init__(
        self,
        epochs: int | None = 10,
        optimizer: str | None = "adam",
        lr: float | None = 0.001,
        lr_scheduler: str | None = "step",
    ) -> None:
        """
        Initialize the configuration for the training settings

        Args:
            epochs (int): Number of epochs to train the model
            optimizer (str): Name of the optimizer
            lr (float): Learning rate for the optimizer
            lr_scheduler (str): Name of the learning rate scheduler
        """
        super().__init__(epochs=epochs, optimizer=optimizer, lr=lr, lr_scheduler=lr_scheduler)


class EvaluationConfig(BaseConfig):
    """Configuration class for the evaluation settings"""

    def __init__(
        self,
        metric_name: str | None = None,
    ) -> None:
        """
        Initialize the configuration for the evaluation settings

        Args:
            metric_name (str): Name of the evaluation metric
        """
        super().__init__(metric_name=metric_name)


class UtilsConfig(BaseConfig):
    """Configuration class for the utility settings"""

    def __init__(
        self,
        seed: int | None = 42,
        device: str | None = "cuda",
    ) -> None:
        """
        Initialize the configuration for the utility settings

        Args:
            seed (int): Seed for reproducibility
            device (str): Device to run the code
        """
        super().__init__(seed=seed, device=device)


class Config(BaseConfig):
    """Configuration class for all the settings"""

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
