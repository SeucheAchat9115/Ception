"""This module contains functions for checking configuration files."""


def is_yaml_config(filename: str) -> bool:
    """
    Check if a file is a YAML configuration file

    Args:
        filename (str): Name of the file

    Returns:
        bool: True if the file is a YAML configuration file, False otherwise
    """
    return filename.endswith(".yaml") or filename.endswith(".yml")
