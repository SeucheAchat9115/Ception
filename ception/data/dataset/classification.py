from ception.data.dataset.base import BaseDataset


class ClassificationDataset(BaseDataset):
    """Dataset class for classification tasks"""

    def __init__(self, cfg) -> None:
        """
        Initialize the classification dataset
        """
        super().__init__(cfg)

        self.cfg = cfg
