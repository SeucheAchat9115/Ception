from ception.data.image.folder import ImageLoaderFromFolder


def get_image_loader(cfg):
    if cfg.data_type in ["classification_image_folder"]:
        return ImageLoaderFromFolder(cfg)
    else:
        raise NotImplementedError(f"Image type {cfg.data_type} not implemented yet")
