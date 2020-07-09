import logging

from copy import copy


logger = logging.getLogger("sorter")


class Photo(object):
    """
    Object representing a photo with a set of properties extracted from the image representation.
    Adapter for Exif -> SQL and vice versa.
    """

    def __init__(self, **kwargs):
        """Populates photo properties."""
        key_words = ["ImageLength", "ImageWidth", "ResolutionUnit", "YResolution", "XResolution",
                     "BrightnessValue", "DigitalZoomRatio", "Contrast", "WhiteBalance", "ColorSpace",
                     "Saturation", "FocalLength", "ShutterSpeedValue", "FNumber", "LightSource",
                     "Flash", "Sharpness", "Model", "Make", "DateTime", "Location"]

        self._img_data = {k: v for k, v in kwargs.iteritems() if k in key_words}

        # Reformat date time -> YYYY-MM-DD-HH-MM-SS
        self._img_data["DateTime"] = "{}_{}.jpg".format(
                self._img_data['DateTime'][:-9].replace(':', '-'),
                self._img_data['DateTime'][11:].replace(':', '-'))

        # TODO create a SQL insert query representing a photo
        # self.sql_data = kwargs.pop("SQL", None)

    @property
    def length(self):
        return copy(self._img_data["ImageLength"])

    @property
    def width(self):
        return copy(self._img_data["ImageWidth"])

    @property
    def resolution_unit(self):
        return copy(self._img_data["ResolutionUnit"])

    @property
    def y_resolution(self):
        return copy(self._img_data["YResolution"])

    @property
    def x_resolution(self):
        return copy(self._img_data["XResolution"])

    @property
    def brightness(self):
        return copy(self._img_data["BrightnessValue"])

    @property
    def zoom_ratio(self):
        return copy(self._img_data["DigitalZoomRatio"])

    @property
    def contrast(self):
        return copy(self._img_data["Contrast"])

    @property
    def white_balance(self):
        return copy(self._img_data["WhiteBalance"])

    @property
    def color_space(self):
        return copy(self._img_data["ColorSpace"])

    @property
    def saturation(self):
        return copy(self._img_data["Saturation"])

    @property
    def focal_length(self):
        return copy(self._img_data["FocalLength"])

    @property
    def shutter_value(self):
        return copy(self._img_data["ShutterSpeedValue"])

    @property
    def f_number(self):
        return copy(self._img_data["FNumber"])

    @property
    def light_source(self):
        return copy(self._img_data["LightSource"])

    @property
    def flash_value(self):
        return copy(self._img_data["Flash"])

    @property
    def sharpness(self):
        return copy(self._img_data["Sharpness"])

    @property
    def camera_model(self):
        return copy(self._img_data["Model"])

    @property
    def camera_maker(self):
        return copy(self._img_data["Make"])

    @property
    def date_taken(self):
        return copy(self._img_data["DateTime"])

    def to_sql(self):
        pass

    def to_dict(self):
        return copy(self._img_data)
