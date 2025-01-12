from typing import Any

import yaml


def read_yaml_file(yaml_path: str) -> dict[str, Any]:
    """
    Read a YAML file and return its content as a dictionary.

    Args:
        yaml_path (str): Path to the YAML file

    Returns:
        dict: Content of the YAML file
    """
    with open(yaml_path) as file:
        return yaml.safe_load(file) or {}
