from ception.data.annotation.dummy_classification import DummyClassificationAnnotationLoader


def get_annotation_loader(cfg):
    if cfg.annotation_type in ["dummy_classification_json"]:
        return DummyClassificationAnnotationLoader(cfg)
    else:
        raise NotImplementedError(f"Annotation type {cfg.annotation_type} not implemented yet")
