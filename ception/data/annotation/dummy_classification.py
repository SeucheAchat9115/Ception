import json

from ception.data.annotation.base import BaseAnnotationLoader


class DummyClassificationAnnotationLoader(BaseAnnotationLoader):
    """
    Annotation loader for dummy classification dataset type
    """

    def load_annotations(self, path: str | None) -> list:
        """
        Load annotations from a given path

        Args:
            path (str): Path to the annotation json file in dummy classification format

        Returns:
            list: List of annotations
        """
        if path is None:
            return []

        with open(path) as f:
            annotations = json.load(f)

        annotation_list = []

        for filename, anno_dict in annotations.items():
            anno_dict["filename"] = filename
            annotation_list.append(anno_dict)

        return annotation_list
