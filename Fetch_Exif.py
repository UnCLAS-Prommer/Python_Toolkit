import os, sys
from PIL import Image
from pillow_heif import register_heif_opener
def OutputFileTime(BaseFilePath):
    FileList = os.listdir(BaseFilePath)
    for i in FileList:
        try:
            img = Image.open(BaseFilePath + "\\" + i)
            exif_dict = img.getexif()
            if (306 in exif_dict):
                print(i + " Time: " + exif_dict[306])
            else:
                print(i + " have no time info.")
        except Exception as e:
            print(e)
register_heif_opener()
BaseFilePath = sys.argv[1]
OutputFileTime(BaseFilePath)