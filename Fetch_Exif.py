import os, sys
from PIL import Image
from pillow_heif import register_heif_opener
import piexif


def GetExifData(i, img):
    if img.format == "HEIF":
        exif_dict = img.getexif()
        if 306 in exif_dict:
            print(i + " Time: " + exif_dict[306])
        else:
            print(i + " have no time info.")
    else:
        exif_dict = piexif.load(img.info["exif"])
        if 36867 in exif_dict["Exif"]:
            print(i + " Time: " + str(exif_dict["Exif"][36867]))
        else:
            print(i + " have no time info.")


def OutputFileTime(BaseFilePath):
    FileList = os.listdir(BaseFilePath)
    for i in FileList:
        try:
            img = Image.open(BaseFilePath + "\\" + i)
            GetExifData(i, img)
            img.close()
        except Exception as e:
            print("File " + i + " met an error: " + str(e))


register_heif_opener()
BaseFilePath = sys.argv[1]
OutputFileTime(BaseFilePath)
