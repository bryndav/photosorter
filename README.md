# Photosorter.py

# Intro
A common problem for me is that I take a lot of photos on my phone, sooner or later the time comes when storage is full.
What I usually do then is dumping my photos into a folder and then whipe to storage media. Photos on my phone usually
lacks good naming and it is a hustle to sort the photos so I just leave them in a messy folder for later.

This is where the photosorter app comes into play, what it does is accessing the header information of photos to extract
the time and date the photo was taken, then it renames photos according to the date and puts them in a folder named
after the year and month the photo was taken (i.e 2019-01).

# Dependencies

* Pillow
    https://pillow.readthedocs.io/en/stable/index.html

# Extensions

Coming changes

* Args parsing, for easier use then needing to go into the code to change folder path
* Database, simple indexing of images

# Usage

import PhotoSorter

image_folder_path = "C:\\Users\\User\\Photos"

sort_photos = PhotoSorter(image_folder_path)
sort_photos.sort()


Alternative

PhotoSorter.sort("C:\\Users\\User\\Photos")