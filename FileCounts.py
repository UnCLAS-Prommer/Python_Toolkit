import os, sys


def count(FolderPath):
    counts = 0
    FileList = os.listdir(FolderPath)
    for i in FileList:
        if i != "$RECYCLE.BIN" and i != "System Volume Information":
            if os.path.isfile(f"{FolderPath}/{i}"):
                counts += 1
            if os.path.isdir(f"{FolderPath}/{i}"):
                counts += count(f"{FolderPath}/{i}")
    return counts


BaseFilePath = sys.argv[1]
print(count(BaseFilePath))
