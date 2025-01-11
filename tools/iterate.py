import argparse

from ception.config.interface import load_config
from ception.data.dataset.interface import get_dataloader, get_dataset
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

    print(f"CEPTION: Found {len(cfg.data)} splits in the configuration file")

    for split in cfg.data:
        print(f"CEPTION: Iterating over split {split}")
        dataset = get_dataset(split)
        dataloader = get_dataloader(split, dataset)

        for batch_idx, (image, annotation) in enumerate(dataloader):
            print(f"CEPTION: Iterating {batch_idx + 1}/{len(dataloader)}")
            print(f"CEPTION: Image shape: {image.shape}")
            print(f"CEPTION: Annotation: {annotation}")


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
        default="configs/dummy_classification.yaml",
        help="Config to overwrite default hyperparameters",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
