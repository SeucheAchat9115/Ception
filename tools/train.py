"""Main Function of the framework"""

import argparse

from ception.config.interface import load_config
from ception.data.generation.dummy_classification import create_dummy_classification_dataset
from ception.utils.argparse import parse_args


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


if __name__ == "__main__":
    main(parse_args())
