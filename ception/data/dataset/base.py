from typing import Any

from torch.utils.data import Dataset


class BaseDataset(Dataset):
    """Base class for all datasets"""

    def __init__(self, cfg) -> None:
        """
        Initialize the base dataset
        """
        self.cfg = cfg
        self.data: list[dict[str, Any]] = []

    def __len__(self) -> int:
        """
        Returns the length of the dataset

        Returns:
            int: Length of the dataset in terms of number of samples
        """
        return len(self.data)

    def __getitem__(self, index: int) -> tuple:
        """
        Returns the sample at the given index

        Args:
            index (int): Index of the sample to be returned

        Returns:
            tuple: A dictionary containing the sample data
        """
        raise NotImplementedError
