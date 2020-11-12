import re
from pytube import YouTube
from urllib.parse import urlparse




download_link = input("Input links to download: ")
yt = YouTube(download_link)


save_filter = []

running = True

while running:
    choice_filter = input("Input V or M to filter. V - video; M - music: ")
    if choice_filter == "M":
        stream = yt.streams.filter(only_audio = True, file_extension='mp4')

        running = False

    if choice_filter == "V":
        stream = yt.streams.filter(only_video = True, file_extension='mp4')

        running = False

    rev_list = ""
    for i in (stream):
        rev_list += str(i)

    pattern_search = (r'(res="[+]?\d+p)|(type="[a-z]{5}")')
    pat_res = re.findall(pattern_search, rev_list)
    
    count = 0
    for x in pat_res:
        count += 1
        print(x, count)






#config_atrr = ('scheme', 'netloc')
#test = urlparse("https://www.youtube.com/")


#def request_download():
    #get_url = input("Paste there link of video what you wand download: ")


   # return get_url


#def asker():
    #get_answer = input("Video or Music? V - video; M - music ")
    #return get_answer
    


##request_download()
##asker()