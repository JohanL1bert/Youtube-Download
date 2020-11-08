from pytube import YouTube
from urllib.parse import urlparse


download_link = input("Input links to download: ")
yt = YouTube(download_link)
choice_filter = input("Input V or M to filter. V - video; M - music: ")
if choice_filter == "M" or 'm':
    stream = yt.streams.filter(only_audio=True, file_extension='mp4').all




config_atrr = ('scheme', 'netloc')
test = urlparse("https://www.youtube.com/")


def request_download():
    get_url = input("Paste there link of video what you wand download: ")


    return get_url


def asker():
    get_answer = input("Video or Music? V - video; M - music ")
    return get_answer
    


##request_download()
##asker()