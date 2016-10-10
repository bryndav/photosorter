from __future__ import print_function
from PIL import Image
import PIL.ExifTags
import os
import shutil

PATH = '/home/dbry/ownCloud/Foton/Mobilbilder'

# Iterate over all directories
for lib in os.listdir(PATH):
    # Try to enter the dict
    try:
        os.chdir(PATH + '/' + lib)
        newpath = PATH + '/' + lib
        
        # Iterate over all files inside the folder.
        for file in os.listdir(newpath):
            
            # Extract images.
            if file.endswith('.jpg') or file.endswith('.JPG') and not file.startswith('20'):    
                img = Image.open(newpath + '/' + file)

                exif = {
                    PIL.ExifTags.TAGS[k]: v
                    for k, v in img._getexif().items()
                    if k in PIL.ExifTags.TAGS
                }
                
                # Renameing function adding (number) when several photos has been taken the same day. 
                if os.path.isfile(exif['DateTime'][:-9].replace(':', '-')):
                    
                    for x in range(1, 30):
                        if os.path.isfile(exif['DateTime'][:-9].replace(':', '-')+ '(' + str(x) + ')'):
                            continue
                        else:
                            os.rename(file, exif['DateTime'][:-9].replace(':', '-')+ '(' + str(x) + ')')
                            break
                else:
                    os.rename(file, exif['DateTime'][:-9].replace(':', '-'))

    except OSError: pass

