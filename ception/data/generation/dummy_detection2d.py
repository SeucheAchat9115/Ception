import os
import json

import numpy as np
from PIL import Image

class_mapping = {0: "red", 1: "blue", 2: "green", 3: "yellow", 4: "magenta"}

colour_rgb_mapping = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0),
    "magenta": (255, 0, 255),
}

def create_dummy_detection2d_dataset(data_dir: str, exist_ok: bool) -> None:
    """
    Create a dummy detection2d dataset with 100 images and corresponding labels as a coco json file

    Args:
        data_dir (str): Directory to save the dataset
        exist_ok (bool): If True, do not delete the directory if it already exists
    """

    if os.path.exists(data_dir):
        if exist_ok:
            print(f"CEPTION: {data_dir} already exists, skipping dataset creation")
            return
        else:
            raise FileExistsError(f"{data_dir} already exists")

    os.makedirs(data_dir, exist_ok=True)

    annotations = {"images": [], "annotations": [], "categories": []}
    annotations["categories"] = [
        {"id": 0, "name": "red"},
        {"id": 1, "name": "blue"},
        {"id": 2, "name": "green"},
        {"id": 3, "name": "yellow"},
        {"id": 4, "name": "magenta"},
    ]

    for image_idx in range(100):
        filename = os.path.join(data_dir, f"{image_idx:010d}.png")
        image = Image.new("RGB", (500, 500), (255, 255, 255))

        annotations["images"].append(
            {
                "id": image_idx, 
                "file_name": filename, 
                "height": 500, 
                "width": 500
            }
        )

        number_of_objects = np.random.randint(1, 10)

        for object_idx in range(number_of_objects):
            color_id = np.random.randint(0, 5)
            x = np.random.randint(0, 500)
            y = np.random.randint(0, 500)
            w = np.random.randint(10, 100)
            h = np.random.randint(10, 100)

            # Draw the object on the image
            object_image = Image.new("RGB", (w, h), colour_rgb_mapping[class_mapping[color_id]])
            image.paste(object_image, (x, y))

            annotations["annotations"].append(
                {
                    "image_id": image_idx,
                    "bbox": [x, y, w, h],
                    "category_id": color_id,
                    "id": len(annotations["annotations"]) + 1,
                    "iscrowd": 0,
                    "area": w * h
                }
            )
        
        image.save(filename)

    with open(os.path.join(data_dir, "annotations.json"), "w") as f:
        json.dump(annotations, f)

    print(f"CEPTION: Dummy detection2d dataset created at {data_dir}")