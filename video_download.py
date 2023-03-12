import os
import sys
pos = input("url: ")
name = input("video name: ")
if(name == "" or pos == ""):
    print("video name or url error.")
    sys.exit()
returncode = os.system("ffmpeg -i \"" + pos + "\"" + " -c copy /Users/shichunyan/Desktop/qiangji/" + name + ".mp4")
if(returncode == 0):
    os.system("terminal-notifier -message \"Download Completed: " + name + "\" -title \"Qianji Downloader\"")
else:
    os.system("terminal-notifier -message \"Download Failed: " + name + "\" -title \"Qianji Downloader\"")
sys.exit()