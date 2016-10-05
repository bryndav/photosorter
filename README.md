# photosorter

# short intro
This is my first GitProject, mostly for learning the ropes. The idé is to create a python script that will sort photos in to sub-directorys.

# program idé

I want to be able to upload images from my cellphone into a folder called my photos.
In this folder there should be a python script that access each photos header (through som standard lib hopefully) to find out the date the photo was taken. From there it will first check if there is a subfolder for the month the photo was taken (done through the OS.path checkdir? function) if so move the photo there, otherwise create a folder called ex. "2016-05" and then move the photo.

# steps to make this program come true

  * Find a suitable package for accessing photo headers, this should take all the common formats such as jpg. png. etc.
  
  * Write the sudocode for the program
  
  * Learn how to structure the skeleton for a real python project, create __init__.py and what not?
  
  * Dare to ask for help from the github crowd and see what the fuss is all about.
  
# extensions

Include a renaming function for the photos aswell, so instead of the standard names like IMG698774 give it a name related to the date it was taken? Or maybe name it after some other hint that can be extracted from the header of a photo?
