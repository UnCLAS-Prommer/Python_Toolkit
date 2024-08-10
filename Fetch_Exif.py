import os, sys
from PIL import Image
from pillow_heif import register_heif_opener
def OutputFileTime(BaseFilePath):
    FileList = os.listdir(BaseFilePath)
    for i in FileList:
        try:
            img = Image.open(BaseFilePath + "\\" + i)
            exif_dict = img.getexif()
            print(exif_dict[306])
        except Exception as e:
            print(e)
register_heif_opener()
BaseFilePath = sys.argv[1]
OutputFileTime(BaseFilePath)