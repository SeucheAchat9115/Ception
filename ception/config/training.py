from ception.config.base import BaseConfig


class TrainingConfig(BaseConfig):
    """Configuration class for the training settings"""

    epochs: int | None
    optimizer: str | None
    lr: float | None
    lr_scheduler: str | None

    def __init__(
        self,
        epochs=10,
        optimizer="adam",
        lr=0.001,
        lr_scheduler="step",
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
