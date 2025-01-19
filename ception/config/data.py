from dataclasses import dataclass
from typing import Any


@dataclass
class SplitConfig:
    """Configuration class for the split settings"""

    name: str | None
    data_type: str | None
    data_location: str | None
    annotation_type: str | None
    annotation_location: str | None
    batch_size: int | None
    transforms: dict | None

    @classmethod
    def from_dict(cls, data: dict[str, Any], name: str) -> "SplitConfig":
        """
        Create a SplitConfig object from a dictionary

        Args:
            data (dict): Dictionary containing the configuration settings
            name (str): Name of the split (train, val, or test)

        Returns:
            SplitConfig: Configuration settings for the split
        """
        data = data.get(name, {})
        data["name"] = name
        return cls(**data)


@dataclass
class DataConfig:
    """Configuration class for the data split settings"""

    train: SplitConfig | None = None
    val: SplitConfig | None = None
    test: SplitConfig | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "DataConfig":
        """
        Create a DataConfig object from a dictionary

        Args:
            data (dict): Dictionary containing the configuration settings

        Returns:
            DataConfig: Configuration settings for the data split
        """
        splits = {key: SplitConfig.from_dict(data, key) for key in ["train", "val", "test"] if key in data}
        return cls(**splits)

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
