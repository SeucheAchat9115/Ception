from ception.data.dataset.base import BaseDataset

# from ception.data.dataset.registry import get_dataset_registry


class ClassificationDataset(BaseDataset):
    """Dataset class for classification tasks"""

    def __init__(self, cfg) -> None:
        """
        Initialize the classification dataset
        """
        super().__init__(cfg)

        self.cfg = cfg
        # self.data_cfg = get_dataset_registry(cfg.data.name)
