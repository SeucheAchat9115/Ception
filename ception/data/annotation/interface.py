from ception.config.data import SplitConfig
from ception.data.annotation.base import BaseAnnotationLoader
from ception.data.annotation.classification.json import ClassificationJsonAnnotationLoader
from ception.data.annotation.detection2d.coco import Detection2dCocoAnnotationLoader


def get_annotation_loader(cfg: SplitConfig) -> BaseAnnotationLoader:
    if cfg.annotation_type in ["classification_json"]:
        return ClassificationJsonAnnotationLoader(cfg)
    elif cfg.annotation_type in ["detection2d_coco"]:
        return Detection2dCocoAnnotationLoader(cfg)
    else:
        raise NotImplementedError(f"Annotation type {cfg.annotation_type} not implemented yet")
