from glob import glob

from ception.data.image.base import BaseImageFileLoader


class ImageFileLoaderFromFolder(BaseImageFileLoader):
    def load_images(self, path: str | None) -> list:
        """
        Load image files from a folder

        Args:
            path (str): Path to the folder containing images

        Returns:
            list: List of image paths
        """
        if path is None:
            return []

        png_image_filenames = glob(path + "/*.png")
        jpg_image_filenames = glob(path + "/*.jpg")
        jpeg_image_filenames = glob(path + "/*.jpeg")
        image_filenames = png_image_filenames + jpg_image_filenames + jpeg_image_filenames

        return image_filenames
