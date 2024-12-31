"""Main Function of the framework"""

import argparse
from ception.utils.config import load_default_config


def main(args: argparse.Namespace) -> None:
    """
    Main entry point into the framework

    Args:
        args (argparse.Namespace): Arguments collected by argparser
    """
    cfg = load_default_config()


def parse_args() -> argparse.Namespace:
    """
    Parse command line arguments

    Returns:
        argparse.Namespace: Arguments passed on the cli interface
    """

    parser = argparse.ArgumentParser(
        description="Ception is a deep learning framework"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="ception/configs/config.yaml",
        help="Config to overwrite default hyperparameters",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
