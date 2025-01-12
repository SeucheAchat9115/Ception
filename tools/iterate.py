import argparse

from ception.config.interface import load_config
from ception.data.dataset.interface import get_dataloader, get_dataset
from ception.data.generation.dummy_detection2d import create_dummy_detection2d_dataset
from ception.utils.argparse import parse_args
from ception.utils.experiment import setup_experiment


def main(args: argparse.Namespace) -> None:
    """
    Main entry point into the framework

    Args:
        args (argparse.Namespace): Arguments collected by argparser
    """

    cfg = load_config(args.config)
    setup_experiment(cfg)

    # create_dummy_classification_dataset(data_dir="dataset/ception_dummy_classification_dataset", exist_ok=True)
    create_dummy_detection2d_dataset(data_dir="dataset/ception_dummy_detection2d_dataset", exist_ok=True)

    print(f"CEPTION: Found {len(cfg.data)} splits in the configuration file")

    for split in cfg.data:
        print(f"CEPTION: Iterating over split {split}")
        dataset = get_dataset(split)
        dataloader = get_dataloader(split, dataset)

        for batch_idx, (image, annotation) in enumerate(dataloader):
            print(f"CEPTION: Iterating {batch_idx + 1}/{len(dataloader)}")
            print(f"CEPTION: Image shape: {image.shape}")
            print(f"CEPTION: Annotation: {annotation}")


if __name__ == "__main__":
    main(parse_args())
