import os, sys
import pyheif
from PIL import Image
BasePath = sys.argv[1]
# 获取所有HEIC图像文件
heic_files = []
for filename in os.listdir(BasePath):
    if filename.endswith('.heic'):
        heic_files.append(filename)

# 批量转换为JPEG图像文件
for heic_file in heic_files:
    heif_file = pyheif.read(f'{BasePath}/{heic_file}')
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    image.save(f'{BasePath}/{heic_file.replace(".heic", ".jpg")}', 'JPEG')
