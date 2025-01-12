from ception.data.annotation.base import BaseAnnotationLoader
import json

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

        annotation_list = []

        for anno in annotations["annotations"]:
            anno_dict = {
                "filename": anno["image_id"],
                "bbox": anno["bbox"],
                "category_id": anno["category_id"],
            }
            annotation_list.append(anno_dict)

        return annotation_list