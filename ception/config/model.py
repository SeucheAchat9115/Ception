from ception.config.base import BaseConfig


class ModelConfig(BaseConfig):
    """Configuration class for the model settings"""

    name: str | None
    backbone: str | None
    num_classes: int | None
    pretrained: bool | None

    def __init__(
        self,
        name=None,
        backbone=None,
        num_classes=None,
        pretrained=None,
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
