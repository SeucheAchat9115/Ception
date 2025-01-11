from ception.config.data import SplitConfig


class BaseImageLoader:
    def __init__(self, cfg: SplitConfig) -> None:
        """
        Initialize the image loader from a folder

        Args:
            cfg (SplitConfig): Configuration dictionary
        """
        self.cfg = cfg
