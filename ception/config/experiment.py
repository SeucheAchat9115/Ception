from ception.config.base import BaseConfig


class ExperimentConfig(BaseConfig):
    """Configuration class for the experiment settings"""

    name: str | None
    save_dir: str | None

    def __init__(
        self,
        name=None,
        save_dir="./output/",
    ) -> None:
        """
        Initialize the configuration for the experiment settings

        Args:
            name (str): Name of the experiment
            save_dir (str): Directory to save the experiment results
        """
        super().__init__(name=name, save_dir=save_dir)
