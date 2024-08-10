import piexif, os, sys
from PIL import Image
def OutputFileTime(BaseFilePath):
    FileList = os.listdir(BaseFilePath)
    for i in FileList:
        try:
            img = Image.open(i)
            exif_dict = piexif.load(img.info['exif'])
            print(i + " Time: " + str(exif_dict['0th'][piexif.ImageIFD.DateTime]))
        except Exception as e:
            print(e)

BaseFilePath = sys.argv[0]
OutputFileTime(BaseFilePath)