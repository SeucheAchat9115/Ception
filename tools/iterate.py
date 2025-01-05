"""Main Function of the framework"""

import argparse

from torch.utils.data import DataLoader

from ception.config.interface import load_config
from ception.data.dataset.interface import get_dataset
from ception.data.generation.dummy_classification import create_dummy_classification_dataset
from ception.utils.experiment import setup_experiment


def main(args: argparse.Namespace) -> None:
    """
    Main entry point into the framework

    Args:
        args (argparse.Namespace): Arguments collected by argparser
    """

    cfg = load_config(args.config)
    setup_experiment(cfg)

    create_dummy_classification_dataset(data_dir="dataset/ception_dummy_classification_dataset", exist_ok=True)
    dataset = get_dataset(cfg.data, "train")
    dataloader = DataLoader(dataset, batch_size=cfg.data.train_batch_size, shuffle=True, num_workers=0)

    for sample in dataloader:
        print(sample)


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
