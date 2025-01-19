import json

from ception.data.annotation.base import BaseAnnotationLoader


class Detection2dCocoAnnotationLoader(BaseAnnotationLoader):
    """
    Annotation loader for 2D object detection dataset type
    """

    def load_annotations(self, path: str | None) -> list:
        """
        Load annotations from a given path

        Args:
            path (str): Path to the annotation json file

        Returns:
            list: List of annotations
        """
        if path is None:
            return []

        with open(path) as f:
            annotations = json.load(f)

        image_mapping = {}
        for image in annotations["images"]:
            image_mapping[image["id"]] = image["file_name"]

        class_mapping = {}
        for category in annotations["categories"]:
            class_mapping[category["id"]] = category["name"]

        annotation_list: list[list[dict]] = [[] for _ in range(len(annotations["images"]))]

        for anno in annotations["annotations"]:
            anno_dict = {
                "image_id": anno["image_id"],
                "image_filename": image_mapping[anno["image_id"]],
                "category_id": anno["category_id"],
                "category_name": class_mapping[anno["category_id"]],
                "bbox": anno["bbox"],
            }
            annotation_list[anno["image_id"]].append(anno_dict)

        return annotation_list
