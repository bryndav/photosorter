from PIL import Image
import PIL.ExifTags
import os
import shutil

PATH = '/home/dbry/ownCloud/Foton/Mobilbilder'

def generateExif(filepath):
    """
    A function for genereating information about a image header.
    """
    img = Image.open(filepath)
    exif = {
        PIL.ExifTags.TAGS[k]: v
        for k, v in img._getexif().items()
        if k in PIL.ExifTags.TAGS
        }
    return exif

if __name__ == '__main__':

    for entry in os.listdir(PATH):
  
        if entry.endswith('.jpg') or entry.endswith('.JPG'):
            filepath = PATH + '/' + entry
            currentExif = generateExif(filepath)

            destination = PATH + '/' + currentExif['DateTime'][:-12].replace(':', '-')

            if not os.path.isdir(destination): os.makedirs(destination)
            try:
                shutil.move(filepath, destination)
            except shutil.Error: pass
