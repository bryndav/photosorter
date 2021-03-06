#!/usr/bin/env python2
import os
import logging
import shutil
import sys
import PIL.ExifTags

from photo import Photo
from PIL import Image

# Setting up logger properties
logger = logging.getLogger("sorter")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class PhotoSorter(object):
    """
    Given a path to a folder containing images, sorts the images and renames them to
    the date and time when they where taken. Image information is extracted from the
    headers containing information regarding time, location and system settings.
    """

    def __init__(self, root_folder=None):
        """
        :param root_folder: Path to folder containing images (str)
        """
        self.root_folder = root_folder
        self.img_list = self.get_unsorted_images()

        self.current_img = None
        self.current_exif = None

    def sort(self, root_folder=None):
        """
        Method that drives the sorting process.

        :param root_folder: Optional path to folder containing images (str)
        """
        if root_folder is not None:
            self.root_folder = root_folder
            self.img_list = self.get_unsorted_images()

        if self.img_list:
            logger.info("Starting to sort {} photos in {} ....".format(len(self.img_list), self.root_folder))

            for img in self.generate_img():
                storage_dir = self._move_image()
                self._rename_img(storage_dir, img)
                Photo(**self.current_exif)
        else:
            logger.info("No photos found in {} exiting....".format(self.root_folder))

    def _move_image(self):
        """
        Creates a new directory based on that time (i.e 2019-01) a photo was taken and moves the photo
        into that directory.

        :return: Path to the new storage location (str)
        """
        year_month = self.current_exif['DateTime'][:-12].replace(':', '-')
        storage_dir = self._check_destination_folder(year_month)

        logger.debug("Moving {} to {}".format(self.current_img, storage_dir))
        shutil.move(self.current_img, storage_dir)

        return storage_dir

    def _rename_img(self, storage_dir, img):
            """
            Renames a image based on the date it was taken extracted from the image header.

            :param storage_dir: Path to the new storage location (str)
            :param img: Name of the file (str)
            """
            new_name = "{}_{}.jpg".format(
                self.current_exif['DateTime'][:-9].replace(':', '-'),
                self.current_exif['DateTime'][11:].replace(':', '-'))

            old_file = os.path.join(storage_dir, img)
            new_file = os.path.join(storage_dir, new_name)
            self.current_exif["Location"] = new_file

            try:
                logger.debug("Renaming {} to {}".format(old_file, new_file))
                os.rename(old_file, new_file)
            except Exception as e:
                logger.warning("Unable to rename {} to {}, file already exists".format(old_file, new_file))
                logger.debug(e)

    def generate_img(self):
        """
        A generator that returns images in the root folder given that they have a certain file ending.

        :return: Path to a file to be moved (str)
        """
        for img in self.img_list:
            self.current_img = os.path.join(self.root_folder, img)
            self.current_exif = self.get_exif(self.current_img)

            if self.current_exif is None:
                continue

            yield img

    def get_unsorted_images(self):
        """
        Looks for images in the root folder of type jpg or jpeg.
        """
        img_list = []

        for f in os.listdir(self.root_folder):
            file_type = f.split(".")[-1]

            if file_type.lower() in ["jpg", "jpeg"]:
                img_list.append(f)

        logger.debug("Found {} images in {}".format(len(img_list), self.root_folder))

        return img_list

    def get_exif(self, filepath):
        """
        A function for generating information about a image header.

        :return: Dictionary containing information tags (dict)
        """
        img = Image.open(filepath)

        try:
            exif = {PIL.ExifTags.TAGS[k]: v for k, v in img._getexif().items()
                    if k in PIL.ExifTags.TAGS}
        except AttributeError as e:
            logger.warning(e)
            exif = None

        if "DateTime" not in exif.keys():
            logger.warning("No valid DateTime field in exif for {}".format(filepath))
            exif = None

        return exif

    def _check_destination_folder(self, year_month):
        """
        Checks if there is a folder named as the argument. If not creates that folder.

        :param year_month: A string representing a year and month xxxx-yy (str)
        :return: Full path to the folder
        """
        destination = os.path.join(self.root_folder, year_month)

        if not os.path.isdir(destination):
            logger.debug("Creating directory {}".format(destination))
            os.makedirs(destination)

        return destination


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Sorts images according to date taken")
    parser.add_argument("img_path", type=str, help="path to image directory")
    parser.add_argument("-v", "--verbosity", action="store_true", default=0, help="increases verbosity")
    args = parser.parse_args()

    if args.verbosity:
        logger.setLevel(logging.DEBUG)

    if os.path.isdir(args.img_path):
        sorter = PhotoSorter(args.img_path)
        sorter.sort()

    else:
        print "Given path {} is not a valid directory, please provide a valid full path"
