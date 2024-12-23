"""Main Function of the framework"""

import argparse


def main(args: argparse.Namespace) -> None:
    """
    Main entry point into the framework

    Args:
        args (argparse.Namespace): Arguments collected by argparser
    """
    assert isinstance(args.config, str)
    print(args)


def parse_args() -> argparse.Namespace:
    """
    Parse command line arguments

    Returns:
        argparse.Namespace: Arguments passed on the cli interface
    """

    parser = argparse.ArgumentParser(
        description="DeepFrame is a deep learning framework"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="DeepFrame/configs/config.yaml",
        help="Config to overwrite default hyperparameters",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
