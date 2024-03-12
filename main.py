from pytube import YouTube as yt
import os
from pathlib import Path

#to install: pyinstaller main.py --onefile
#pack install: pip install pipreqs, pip install pytube

def get_link():
    user_input = input("Please provide link: ")
    url = user_input
    return url

def get_video_by_quality(quality):
    url = get_link()
    ytv= yt(url)
    video = ytv.streams.filter(res=quality).first()

    try:
        print("Video is downloading, please wait...")
        path_to_download = str(os.path.join(Path.home(), 'Downloads'))
        video.download(path_to_download)
        print("Video has been downloaded, check your Downloads directory!")
    except Exception as e:
        print("The video you selected either doesnt exist, or the resolution is too high!!")
        print(e)

def get_video_highest():
    url = get_link()
    ytv = yt(url)
    video = ytv.streams.get_highest_resolution()

    try:
        print("Video is downloading, please wait...")
        path_to_download = str(os.path.join(Path.home(), 'Downloads'))
        video.download(path_to_download)
        print("Video has been downloaded, check your Downloads directory!")
    except Exception as e:
        print("The video you selected doesnt exist!")
        print(e)

def get_video_lowest():
    url = get_link()
    ytv = yt(url)
    video = ytv.streams.get_lowest_resolution()

    try:
        print("Video is downloading, please wait...")
        path_to_download = str(os.path.join(Path.home(), 'Downloads'))
        video.download(path_to_download)
        print("Video has been downloaded, check your Downloads directory!")
    except Exception as e:
        print("The video you selected doesnt exist!")
        print(e)

def get_audio():
    url = get_link()
    yto = yt(url)
    video = yto.streams.get_audio_only()
    try:
        print("Audio is downloading, please wait...")
        path_to_download = str(os.path.join(Path.home(), 'Downloads'))
        video.download(path_to_download)
        print("Audio has been downloaded, check your Downloads directory!")
    except Exception as e:
        print("The video you selected doesnt exist!")
        print(e)



def main():

    qualities = ["highest", "lowest", "1080p", "720p", "480p", "360p", "240p", "144p"]
    choices = ["video", "audio"]

    print("Welcome to youtube file downloader")
    choice_audio_video = input("Do you want to download audio file or video file?: ")
    choice_l = choice_audio_video.lower().strip()

    if choice_l not in choices:
        print("Wrong answer!")
        exit()
    if choice_l == "audio":
        get_audio()
    if choice_l == "video":
        quality = input("Please provide the video quality: ")
        quality_l = quality.lower()
        if quality_l not in qualities:
            print("The quality you provided is not valid one!")
        elif quality_l == "highest":
            get_video_highest()
        elif quality_l == "lowest":
            get_video_lowest()
        else:
            get_video_by_quality(str(quality))

    input("Type anything to close...")


if __name__ == '__main__':
    main()