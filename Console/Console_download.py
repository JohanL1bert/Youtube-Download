import re
from pytube import YouTube
from urllib.parse import urlparse


download_link = input("Input links to download: ")
yt = YouTube(download_link)


running = True

while running:
    choice_filter = input("Input V or M to filter. V - video; M - music: ")
    if choice_filter == "M":
        stream = yt.streams.filter(only_audio = True, file_extension='mp4')
        running = False

    if choice_filter == "V":
        stream = yt.streams.filter(only_video = True, file_extension='mp4')
        running = False

    reverse_list = ""
    for i in (stream):
        reverse_list += str(i)

    pattern_search = (r'(res="[+]?\d+p)')
    pattern_result = re.findall(pattern_search, reverse_list)
    
    #pattern
    template_video = " type=video"
    reverse_str = str(pattern_result)
    clean_str = reverse_str.replace("'",'').replace('"', '').replace('(', '').replace(')', '').replace(',','').replace('[', '').replace("]",'')
    spl_string = clean_str.split()


    # Add pattern to value after every iteration
    result = list(s + template_video for s in spl_string)
    
    video_view = result.copy()

    count = 1
    for x in video_view:
        print(f"{count}. {x}")
        count += 1

    #pattern
    type_pattern_get = "mp4"
    input_resolution = input("Type video resolution. For example: 1080p or 144p: ")
    filter_to_download = stream.filter(subtype="mp4", resolution=input_resolution).first()
    filter_to_download.download()

        






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