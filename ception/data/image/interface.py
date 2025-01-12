from ception.config.data import SplitConfig
from ception.data.image.base import BaseImageFileLoader
from ception.data.image.folder import ImageFileLoaderFromFolder


def get_image_filename_loader(cfg: SplitConfig) -> BaseImageFileLoader:
    if cfg.data_type in ["classification_image_folder"]:
        return ImageFileLoaderFromFolder(cfg)
    else:
        raise NotImplementedError(f"Image file loader type {cfg.data_type} not implemented yet")
