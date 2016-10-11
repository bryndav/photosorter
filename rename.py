from PIL import Image
import PIL.ExifTags
import os
import shutil

PATH = '/home/dbry/ownCloud/Foton/Mobilbilder'


class ImageInfo:
    """
    A class for using the PIL lib with method for creating a dict with
    picture header information.
    """
    def __init__(self, filepath):
        self.img = Image.open(filepath)

    def generateExif(self):
        self.exif = {
            PIL.ExifTags.TAGS[k]: v
            for k, v in self.img._getexif().items()
            if k in PIL.ExifTags.TAGS
            }


if __name__ == '__main__':
    
    for entry in os.listdir(PATH):
        
        if entry.endswith('.jpg') or entry.endswith('.JPG'):
            filepath = PATH + '/' + entry
            currentImg = ImageInfo(filepath)
            currentImg.generateExif()
            
            destination = PATH + '/' + currentImg.exif['DateTime'][:-12].replace(':', '-')
            
            if not os.path.isdir(destination): os.makedirs(destination)
            shutil.move(filepath, destination)
            
