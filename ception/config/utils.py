from ception.config.base import BaseConfig


class UtilsConfig(BaseConfig):
    """Configuration class for the utility settings"""

    seed: int | None
    device: str | None

    def __init__(
        self,
        seed=42,
        device="cuda",
    ) -> None:
        """
        Initialize the configuration for the utility settings

        Args:
            seed (int): Seed for reproducibility
            device (str): Device to run the code
        """
        super().__init__(seed=seed, device=device)
