#!/usr/bin/env python2

try:
    import unittest2 as unittest
except ImportError:
    import unittest  # noqa

import logging
import os
import re

from src.photo_sorter import PhotoSorter
from src.photo import Photo

from shutil import copy, rmtree


logger = logging.getLogger("sorter")

RESOURCES = os.path.join(os.path.dirname(__file__), "resources")
ROOT = os.path.join(os.path.dirname(__file__), "test_area")


def populate_test_area(source, destination):
    """Moves photos into the test area"""
    logger.info("Populating {} with example photos".format(source))

    for file in os.listdir(source):
        full_path = os.path.join(source, file)
        copy(full_path, destination)


def clear_test_area(path):
    """Removes example photos and folders from test area"""
    logger.info("Clearing {} of any photos or directories".format(ROOT))

    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)

        try:
            if os.path.isfile(full_path) or os.path.islink(full_path):
                os.unlink(full_path)
            elif os.path.isdir(full_path):
                rmtree(full_path)
        except Exception as e:
            print "Failed to delete {}. Given reason {}".format(full_path, e)


def get_sorter():
    """Generate photo sorter object for testing"""
    return PhotoSorter(ROOT)


class TestSorting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Runs pre-condition method before test execution."""
        populate_test_area(RESOURCES, ROOT)
        sorter = get_sorter()
        sorter.sort()

    @classmethod
    def tearDownClass(cls):
        """Runs methods for cleaning up after test execution."""
        clear_test_area(ROOT)

    def setUp(self):
        self.expected_dir = "2020-05"
        self.list_of_files_sorted = os.listdir(os.path.join(ROOT, self.expected_dir))
        self.list_of_files_root = os.listdir(ROOT)

    def test_image_identifier(self):
        """Tests the image identification process."""
        clear_test_area(ROOT)
        populate_test_area(RESOURCES, ROOT)
        sorter = get_sorter()
        nof_images = 1

        assert(len(sorter.img_list) == nof_images), "Expected: {}  Found: {}, number of images".format(
            nof_images, len(self.sorter.img_list))

        sorter.sort()

    def test_sorting_pos(self):
        """Tests the sorting of photos into directories."""
        expected_nof_directories = 1
        expected_nof_images = 1

        # Check that a new folder i created and that example photo is moved
        assert(self.expected_dir in self.list_of_files_root), "Directory {} not created".format(self.expected_dir)
        assert(len(self.list_of_files_root) == expected_nof_directories), "Expected: {} directories"

        # Check that new folder contains the example file
        assert(len(self.list_of_files_sorted) == expected_nof_images), \
            "Expected: {} Found: {}, image not at destination".format(len(self.list_of_files_sorted), expected_nof_images)

    def test_renaming_pos(self):
        """Tests the renaming of photos according to date taken."""
        expected_format = re.compile("\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}")
        sorted_image_name = self.list_of_files_sorted[0]

        assert(expected_format.search(sorted_image_name) is not None), \
            "Image did not follow naming according to {}".format(expected_format.pattern)


class TestPhoto(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Runs pre-condition method before test execution."""
        populate_test_area(RESOURCES, ROOT)

    @classmethod
    def tearDownClass(cls):
        """Runs methods for cleaning up after test execution."""
        clear_test_area(ROOT)

    def get_photo_object(self):
        sorter = get_sorter()
        img_path = os.path.join(ROOT, sorter.img_list[0])

        photo_info = sorter.get_exif(img_path)
        photo_info["Location"] = img_path
        photo = Photo(**photo_info)

        return photo

    def test_photo_camera_maker(self):
        photo = self.get_photo_object()

        assert(type(photo.camera_maker) is not None)

    def test_photo_length(self):
        photo = self.get_photo_object()

        assert(type(photo.length) is not None)

    def test_photo_width(self):
        photo = self.get_photo_object()

        assert(type(photo.width) is not None)

    def test_photo_reselution(self):
        photo = self.get_photo_object()

        assert(type(photo.resolution_unit) is not None)

    def test_photo_y_reselution(self):
        photo = self.get_photo_object()

        assert(type(photo.y_resolution) is not None)

    def test_photo_x_reselution(self):
        photo = self.get_photo_object()

        assert(type(photo.x_resolution) is not None)

    def test_photo_brightness(self):
        photo = self.get_photo_object()

        assert(type(photo.brightness) is not None)

    def test_photo_zoom_ratio(self):
        photo = self.get_photo_object()

        assert(type(photo.zoom_ratio) is not None)

    def test_photo_contrast(self):
        photo = self.get_photo_object()

        assert(type(photo.contrast) is not None)

    def test_photo_white_balance(self):
        photo = self.get_photo_object()

        assert(type(photo.white_balance) is not None)

    def test_photo_color_space(self):
        photo = self.get_photo_object()

        assert(type(photo.color_space) is not None)

    def test_photo_saturation(self):
        photo = self.get_photo_object()

        assert(type(photo.saturation) is not None)

    def test_photo_focal_length(self):
        photo = self.get_photo_object()

        assert(type(photo.focal_length) is not None)

    def test_photo_shutter_value(self):
        photo = self.get_photo_object()

        assert(type(photo.shutter_value) is not None)

    def test_photo_f_number(self):
        photo = self.get_photo_object()

        assert(type(photo.f_number) is not None)

    def test_photo_light_source(self):
        photo = self.get_photo_object()

        assert(type(photo.light_source) is not None)

    def test_photo_flash_value(self):
        photo = self.get_photo_object()

        assert(type(photo.flash_value) is not None)

    def test_photo_sharpness(self):
        photo = self.get_photo_object()

        assert(type(photo.sharpness) is not None)

    def test_photo_date_time(self):
        expected_format = re.compile("\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}")
        photo = self.get_photo_object()

        assert (type(photo.date_taken) is not None)
        assert (expected_format.search(photo.date_taken) is not None), \
            "Image did not follow naming according to {}".format(expected_format.pattern)


if __name__ == "__main__":
    unittest.main()
