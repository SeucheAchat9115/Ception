from PIL import Image

from ception.config.data import SplitConfig
from ception.data.annotation.interface import get_annotation_loader
from ception.data.dataset.base import BaseDataset
from ception.data.transforms.interface import get_transforms


class ImageAnnotationDataset(BaseDataset):
    """Dataset class for image and annotation tasks"""

    def __init__(self, cfg: SplitConfig) -> None:
        """
        Initialize the dataset

        Args:
            cfg (SplitConfig): Configuration for the dataset
        """
        super().__init__(cfg)

        self.cfg = cfg

        self.transforms = get_transforms(cfg)

        print(f"CEPTION: Loading annotations from {self.cfg.annotation_location} for split {self.cfg.name}")
        annotation_loader = get_annotation_loader(self.cfg)
        self.annotations = annotation_loader.load_annotations(self.cfg.annotation_location)
        print(f"CEPTION: Found {len(self.annotations)} annotations for split {self.cfg.name}")

    def __getitem__(self, index: int) -> tuple:
        """
        Get the image and annotation at the given index

        Args:
            index (int): Index of the image and annotation pair

        Returns:
            tuple: Image and annotation
        """
        annotation = self.annotations[index]
        image_filename = annotation["filename"]
        image = Image.open(image_filename).convert("RGB")

        if self.transforms is not None:
            image = self.transforms(image)

        return image, annotation
