from ception.config.data import SplitConfig
from ception.data.annotation.base import BaseAnnotationLoader
from ception.data.annotation.dummy_classification import DummyClassificationAnnotationLoader


def get_annotation_loader(cfg: SplitConfig) -> BaseAnnotationLoader:
    if cfg.annotation_type in ["dummy_classification_json"]:
        return DummyClassificationAnnotationLoader(cfg)
    else:
        raise NotImplementedError(f"Annotation type {cfg.annotation_type} not implemented yet")
