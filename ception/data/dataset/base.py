from typing import Any

from torch.utils.data import Dataset

from ception.config.data import SplitConfig


class BaseDataset(Dataset):
    """Base class for all datasets"""

    def __init__(self, cfg: SplitConfig) -> None:
        """
        Initialize the base dataset
        """
        self.cfg = cfg
        self.annotations: list[Any] = []

    def __len__(self) -> int:
        """
        Returns the length of the dataset

        Returns:
            int: Length of the dataset in terms of number of samples
        """
        return len(self.annotations)

    def __getitem__(self, index: int) -> tuple[Any, dict[str, Any]]:
        """
        Returns the sample at the given index

        Args:
            index (int): Index of the sample to be returned

        Returns:
            tuple: A tuple of data tensor and annotation dict
        """
        raise NotImplementedError
