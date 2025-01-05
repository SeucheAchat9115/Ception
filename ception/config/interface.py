"""This module provides an interface for loading configuration settings."""

from ception.config.base import Config
from ception.config.check import is_yaml_config


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
