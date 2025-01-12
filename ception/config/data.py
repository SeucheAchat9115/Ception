from ception.config.base import BaseConfig


class SplitConfig(BaseConfig):
    """Configuration class for the split settings"""

    name: str | None
    data_type: str | None
    data_location: str | None
    annotation_type: str | None
    annotation_location: str | None
    batch_size: int | None
    transforms: dict | None

    def __init__(
        self,
        name=None,
        data_type=None,
        data_location=None,
        annotation_type=None,
        annotation_location=None,
        batch_size=2,
        transforms=None,
    ) -> None:
        """
        Initialize the configuration for the split settings

        Args:
            name (str): Name of the split
            data_type (str): Type of the data
            data_location (str): Location of the data
            annotation_type (str): Type of the annotation
            annotation_location (str): Location of the annotation
            batch_size (int): Batch size for the data
            transforms (dict): Transformation settings for the data
        """
        super().__init__(
            name=name,
            data_type=data_type,
            data_location=data_location,
            annotation_type=annotation_type,
            annotation_location=annotation_location,
            batch_size=batch_size,
            transforms=transforms,
        )


class DataConfig(BaseConfig):
    """Configuration class for the data split settings"""

    train: SplitConfig | None
    val: SplitConfig | None
    test: SplitConfig | None

    def __init__(self, train=None, val=None, test=None) -> None:
        """
        Initialize the configuration for the data split settings

        Args:
            train (SplitConfig): Configuration for the training split
            val (SplitConfig): Configuration for the validation split
            test (SplitConfig): Configuration for the testing split
        """
        super().__init__(
            train=SplitConfig(name="train", **train) if train is not None else None,
            val=SplitConfig(name="val", **val) if val is not None else None,
            test=SplitConfig(name="test", **test) if test is not None else None,
        )

    def __len__(self) -> int:
        """
        Get the number of configuration settings that are not None

        Returns:
            int: Number of configuration settings
        """
        return len([value for value in self.__dict__.values() if value is not None])

    def __iter__(self):
        """
        Iterate over the configuration settings

        Returns:
            Any: Value of the configuration setting
        """
        for value in self.__dict__.values():
            if value is not None:
                yield value
