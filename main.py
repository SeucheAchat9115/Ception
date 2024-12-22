import argparse


def main(args):
    pass


def parse_args() -> argparse.Namespace:
    """
    Parse command line arguments
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
    args = parse_args()
    main(args)
