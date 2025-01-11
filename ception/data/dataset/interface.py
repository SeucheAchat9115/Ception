from torch.utils.data import DataLoader

from ception.config.data import SplitConfig
from ception.data.dataset.base import BaseDataset
from ception.data.dataset.classification import ImageClassificationDataset


def get_dataset(cfg: SplitConfig) -> BaseDataset:
    """
    Get the dataset class based on the name

    Args:
        cfg (SplitConfig): Configuration dictionary

    Returns:
        BaseDataset: Dataset class
    """

    if cfg.data_type in ["classification_image_folder"]:
        return ImageClassificationDataset(cfg)
    else:
        raise NotImplementedError(f"Dataset type {cfg.data_type} not implemented yet")


def get_dataloader(cfg: SplitConfig, dataset: BaseDataset) -> DataLoader:
    """
    Get the dataloader class based on the name

    Args:
        cfg (Dict[str, Any]): Configuration dictionary
        dataset (BaseDataset): Dataset class

    Returns:
        DataLoader: Dataloader class
    """
    return DataLoader(dataset, batch_size=cfg.batch_size, shuffle=True, num_workers=0)
