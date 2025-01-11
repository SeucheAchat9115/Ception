from glob import glob

from ception.data.image.base import BaseImageLoader


class ImageLoaderFromFolder(BaseImageLoader):
    def load_images(self, path: str) -> list:
        """
        Load images from the folder

        Args:
            path (str): Path to the folder containing images

        Returns:
            list: List of image paths
        """

        png_images = glob(path + "/*.png")
        jpg_images = glob(path + "/*.jpg")
        jpeg_images = glob(path + "/*.jpeg")
        images = png_images + jpg_images + jpeg_images

        return images
