import os
import sort.currentExif

PATH = '/home/dbry/ownCloud/Foton/Mobilbilder'

for lib in os.listdir(PATH):

    try:
        os.chdir(PATH + '/' + lib)
        newpath = PATH + '/' + lib

        for file in os.listdir(newpath):

            if file.endswith('.jpg') or file.endswith('.JPG'):
                filepath = newpath + '/' + file

                currentExif = sort.generateExif(filepath)

                os.rename(file, currentExif['DateTime'][:-9].replace(':', '-')
                            + '_' + currentExif['DateTime'][11:].replace(':', '-')
                            )
    except OSError: pass


            
