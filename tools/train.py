"""Main Function of the framework"""

import argparse

from ception.config.interface import load_config
from ception.data.generation.dummy_classification import create_dummy_classification_dataset


def main(args: argparse.Namespace) -> None:
    """
    Main entry point into the framework

    Args:
        args (argparse.Namespace): Arguments collected by argparser
    """
    # 1. Load yaml config and create a config object
    cfg = load_config(args.config)
    print(cfg)

    # 2. Initialize components that are required for training

    # 3. Setup the data pipeline
    create_dummy_classification_dataset(data_dir="data/ception_dummy_classification_dataset", exist_ok=True)

    # 4. Setup the model

    # 5. Perform training

    # 6. Finalize the training process


def parse_args() -> argparse.Namespace:
    """
    Parse command line arguments

    Returns:
        argparse.Namespace: Arguments passed on the cli interface
    """

    parser = argparse.ArgumentParser(description="Ception is a deep learning framework")
    parser.add_argument(
        "--config",
        type=str,
        default="configs/config.yaml",
        help="Config to overwrite default hyperparameters",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
