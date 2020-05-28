#!/usr/bin/env python2

try:
    import unittest2 as unittest
except ImportError:
    import unittest  # noqa

import logging
import os
import re

import src.photo_sorter as ps

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
    return ps.PhotoSorter(ROOT)


class SortingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Runs pre-condition method before test execution"""
        populate_test_area(RESOURCES, ROOT)
        sorter = get_sorter()
        sorter.sort()

    @classmethod
    def tearDownClass(cls):
        """Runs methods for cleaning up after test execution"""
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


if __name__ == "__main__":
    unittest.main()
