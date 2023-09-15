import os,sys
import requests
def download(name):
    returncode = os.system("ffmpeg -version")
    if(returncode != 0):
        print(returncode)
        print("FFmpeg error.")
    else:
        returncode = os.system("ffmpeg -protocol_whitelist concat,file,http,https,tcp,tls,crypto -i tmp.m3u8 -c copy " + name + ".mp4")
        if (returncode == 0):
            os.remove("tmp.m3u8")
        else:
            print(returncode)
            print("FFmpeg error.")
            os.remove("tmp.m3u8")
def fetchm3u8(url,confusion):
    if(confusion == -1):
        try:
            resp = requests.get(url)
            data = resp.text
            dataline = data.split("\n")
        except Exception as e:
            print(e)
            print("Please retry.")
            init()
        for i in dataline:
            if (i.find("#") == -1 and i.find("https") == -1 and len(i) >= 2):
                print("Domain needed")
                domain = input("Domain: ")
                domain = domain if domain[-1] == "/" else domain + "/"
                break
        with open("tmp.m3u8", "w") as f:
            for i in dataline:
                if(i.find("#") == -1 and len(i) >= 2 and i.find("https") == -1):
                    f.write(domain + i + "\n")
                else:
                    f.write(i + "\n")
        f.close()
    else:
        print("Url is confused. Please input a new url.\n")
        init()

def getinput():
    url = input("url: ")
    name = input("video name: ")
    if(name == "" or url == ""):
        print("video name or url is empty. Please retry.\n")
        init()
    else:
        return url,name
    
def init():
    url,name = getinput()
    name = name if name.find(".mp4") == -1 else name[0:-4]
    fetchm3u8(url,url.find("confusion_index"))
    download(name)
init()
