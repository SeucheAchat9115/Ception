import os
import numpy as np
from PIL import Image
import json

class_mapping = {
    0: "red",
    1: "blue",
    2: "green",
    3: "yellow",
    4: "magenta"
}

colour_rgb_mapping = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0),
    "magenta": (255, 0, 255)
}

def create_dummy_classification_dataset(data_dir: str) -> None:
    """
    Create a dummy classification dataset with 100 images and corresponding labels as a json file

    Args:
        data_dir (str): Directory to save the dataset
    """

    if os.path.exists(data_dir):
        raise FileExistsError(f"Directory {data_dir} already exists")
    
    os.makedirs(data_dir)

    labels = {}

    for image_idx in range(100):
        color_id = np.random.randint(0, 5)
        image = Image.new("RGB", (500, 500), colour_rgb_mapping[class_mapping[color_id]])
        image.save(os.path.join(data_dir, f"{image_idx:010d}.png"))
        
        labels[f"{image_idx:010d}.png"] = {
            "class_id": color_id, 
            "class_name": class_mapping[color_id]
            }

    with open(os.path.join(data_dir, "labels.json"), "w") as f:
        json.dump(labels, f)
    