import json
import os

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


def create_dummy_classification_dataset(data_dir: str, exist_ok: bool) -> None:
    """
    Create a dummy classification dataset with 100 images and corresponding labels as a json file

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

    labels = {}

    for image_idx in range(100):
        color_id = np.random.randint(0, 5)
        filename = os.path.join(data_dir, f"{image_idx:010d}.png")
        image = Image.new("RGB", (500, 500), colour_rgb_mapping[class_mapping[color_id]])
        image.save(filename)

        labels[filename] = {"class_id": color_id, "class_name": class_mapping[color_id]}

    with open(os.path.join(data_dir, "labels.json"), "w") as f:
        json.dump(labels, f)

    print(f"CEPTION: Dummy classification dataset created at {data_dir}")
