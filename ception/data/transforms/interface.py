from torchvision import transforms as T

from ception.config.data import SplitConfig


def get_transforms(cfg: SplitConfig) -> T.Compose:
    """
    Get the transforms for the dataset

    Args:
        cfg (SplitConfig): Configuration for the dataset

    Returns:
        T.Compose: Transformations to be applied to the dataset
    """
    if cfg.transforms is not None:
        return transforms_dict_to_compose(cfg.transforms)
    else:
        return T.Compose([T.ToTensor()])


def transforms_dict_to_compose(transforms_dict: dict) -> T.Compose:
    """
    Convert a dictionary of transforms to a torchvision.transforms.Compose object

    Args:
        transforms_dict (dict): Dictionary of transforms

    Returns:
        T.Compose: Composed transforms
    """
    transforms = []
    for transform_name, transform_params in transforms_dict.items():
        transform = getattr(T, transform_name)
        transforms.append(transform(**transform_params))
    return T.Compose(transforms)
