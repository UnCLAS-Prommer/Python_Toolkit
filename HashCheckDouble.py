import os, hashlib, progressbar, shutil, random

flist = list()
basepath = "G:\\"


def search(paths):
    if (
        paths.find("$RECYCLE.BIN") == -1
        and paths.find("System Volume Information") == -1
        and paths.find("Check") == -1
    ):
        if os.path.isfile(paths):
            flist.append(paths)
        else:
            for objects in os.listdir(paths):
                search(os.path.join(paths, objects))


def filehash(paths) -> str:
    h = hashlib.md5()
    with open(paths, "rb") as f:
        while b := f.read():
            h.update(b)
    return h.hexdigest()


def filehash2(paths) -> str:
    h = hashlib.sha256()
    with open(paths, "rb") as f:
        while b := f.read():
            h.update(b)
    return h.hexdigest()


search(basepath)
# print(flist)
dictionary = dict()
p = progressbar.ProgressBar(
    widgets=[progressbar.Percentage(), "(", progressbar.SimpleProgress(), ")"]
)
for file in p(flist):
    tmp = filehash(file)
    if dictionary.get(tmp, "null") == "null":
        dictionary[filehash(file)] = file
    else:
        if filehash2(dictionary.get(tmp)) == filehash2(file):
            print(file + " 与 " + dictionary.get(tmp) + "相同，已经移动")
            try:
                shutil.move(file, "G:\\Check\\doubles")
            except Exception as e:
                print(e)
                shutil.move(file, file + "." + str(int(1000 * random.random())))
