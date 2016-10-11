from PIL import Image
import PIL.ExifTags
import os
import sort

PATH = '/home/dbry/ownCloud/Foton/Mobilbilder'

    
for lib in os.listdir(PATH):
        
    try:
        os.chdir(PATH + '/' + lib)
        newpath = PATH + '/' + lib
            
        for file in os.listdir(newpath):
                
            if file.endswith('.jpg') or file.endswith('.JPG'):
                filepath = newpath + '/' + file
            
                currentIMG = sort.ImageInfo(filepath)
                currentIMG.generateExif()
                    
                os.rename(file, currentIMG.exif['DateTime'][:-9].replace(':', '-')
                            + '_' + currentIMG.exif['DateTime'][11:].replace(':', '-')
                            )
    except OSError: pass

            
