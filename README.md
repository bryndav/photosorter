# Photosorter.py

# Intro
A common problem for me is that I take a lot of photos on my phone, sooner or later the time comes when storage is full.
What I usually do then is dumping my photos into a folder and then wipe the storage media. Photos on my phone usually
lacks good naming and it is a hustle to sort the photos so I just leave them in a messy folder for later.

This is where the photo sorter app comes into play, what it does is accessing the header information of photos to extract
the time and date the photo was taken, then it renames photos according to the date and puts them in a folder named
after the year and month the photo was taken (i.e 2019-01).

# Dependencies

* Pillow
    https://pillow.readthedocs.io/en/stable/index.html

# Extensions

Coming changes

* Port to python 3
* Move images to a single storage point
* Database, simple indexing of images

# Usage

Photo sorter is used as a commandline tool, use like so:

> python photo_sorter.py C:\Users\Stationara\Pictures\test

2020-05-28 18:24:43,471 - sorter - INFO - Starting to sort 8 photos in C:\Users\Stationara\Pictures\test ....