from pytube import YouTube,Playlist
import socket
import socks
from urllib.error import HTTPError, URLError
from moviepy.editor import *
import os

socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1",1080)
socket.socket = socks.socksocket
def downLoad():
    while True:
        try:
            playlist = Playlist("https://www.youtube.com/playlist?list=PLrwoLwbVlFs0YWniFQzRRGOF_FVZrL3G3")
            break
        except HTTPError:
            print("请求出错：HTTPError")
            continue
        except URLError:
            print("请求出错: URLError")
            continue

    while True:
        try:
            for video in playlist:
                print(video)
                yt = YouTube(video)
                yt.streams.first().download()
            # yt = YouTube("https://www.youtube.com/watch?v=BCp68zpRTDs&list=PLrwoLwbVlFs0YWniFQzRRGOF_FVZrL3G3&index=2&t=0s")
            # yt.streams.first().download()
            break
        except HTTPError:
            print("请求出错：HTTPError")
            continue
        except URLError:
            print("请求出错: URLError")
            continue


def transfer(file):
    for root, dirs, files in os.walk(file):
        for filename in files:
            if "mp4" in filename:
                video = VideoFileClip(filename)
                print(filename)
                audio = video.audio
                audioname = filename[0:-3]+"mp3"
                print(audioname)
                audio.write_audiofile(audioname)
                os.remove(filename)


def change_name(path):
    for root,dirs,files in os.walk(path):
        for filename in files:
            if "mp4" in filename:
                if len(filename) <= 30:
                    path
                else:
                    newName = "xz"+filename[19:]
                    os.rename(filename,newName)


downLoad()
change_name("/Users/mac/PycharmProjects/pytube") #需修改下载路径
transfer("/Users/mac/PycharmProjects/pytube")
