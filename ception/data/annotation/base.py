from ception.config.data import SplitConfig


class BaseAnnotationLoader:
    def __init__(self, cfg: SplitConfig) -> None:
        """
        Initialize the base annotation loader

        Args:
            cfg (SplitConfig): Configuration dictionary
        """
        self.cfg = cfg

    def load_annotations(self, path: str) -> list:
        """
        Load annotations from a given path

        Args:
            path (str): Path to the annotation file/folder

        Returns:
            list: List of annotations
        """
        raise NotImplementedError
