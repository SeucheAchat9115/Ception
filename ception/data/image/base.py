from ception.config.data import SplitConfig


class BaseImageFileLoader:
    def __init__(self, cfg: SplitConfig) -> None:
        """
        Initialize the image loader from a folder

        Args:
            cfg (SplitConfig): Configuration dictionary
        """
        self.cfg = cfg

    def load_images(self, path: str | None) -> list:
        """
        Load images from the folder

        Args:
            path (str): Path to the folder containing images

        Returns:
            list: List of image paths
        """
        raise NotImplementedError
