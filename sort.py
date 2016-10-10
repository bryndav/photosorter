from PIL import Image
import PIL.ExifTags
import os
import shutil

PATH = '/home/dbry/ownCloud/Foton/Mobilbilder'

for entry in os.listdir(PATH):
    if entry.endswith('.jpg') or entry.endswith('.JPG'):
        
        source = PATH + '/' + entry
        
        img = Image.open(source)
        exif = {
            PIL.ExifTags.TAGS[k]: v
            for k, v in img._getexif().items()
            if k in PIL.ExifTags.TAGS
        }
        
        destination = PATH + '/' + exif['DateTime'][:-12].replace(':', '-')
        if not os.path.isdir(destination): os.makedirs(destination)
        shutil.move(source, destination)
