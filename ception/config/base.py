from typing import Any


class BaseConfig:
    """Base class for the configuration settings"""

    def __init__(self, **kwargs: Any) -> None:
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
            pretty_string += f"{key}: {value}\n"
        return pretty_string
