from torch.utils.data import DataLoader

from ception.config.base import DataConfig
from ception.data.dataset.base import BaseDataset
from ception.data.dataset.classification import ClassificationDataset


def get_dataset(cfg: DataConfig, split: str) -> BaseDataset:
    """
    Get the dataset class based on the name

    Args:
        cfg (Dict[str, Any]): Configuration dictionary
        split (str): Split of the dataset

    Returns:
        BaseDataset: Dataset class
    """

    if cfg.dataset_type == "classification":
        return ClassificationDataset(cfg)
    else:
        raise NotImplementedError(f"Dataset type {cfg.dataset_type} not implemented yet")


def get_dataloader(cfg: DataConfig, dataset: BaseDataset) -> DataLoader:
    """
    Get the dataloader class based on the name

    Args:
        cfg (Dict[str, Any]): Configuration dictionary
        dataset (BaseDataset): Dataset class

    Returns:
        DataLoader: Dataloader class
    """
    return DataLoader(dataset, batch_size=cfg.train_batch_size, shuffle=True, num_workers=0)
