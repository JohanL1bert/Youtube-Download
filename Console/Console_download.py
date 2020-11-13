#Check in this script is awfull

import re
from pytube import YouTube
from urllib.parse import urlparse


# CONST and PATTERN
running = True
template_video = " type=video"
template_music = " type=music"

while True:
    download_link = input("Enter link to download: ")
    o_parse = urlparse(download_link)
    if o_parse.scheme == "https" and o_parse.netloc == "www.youtube.com":
        break
    else:
        print("Link is not valid ")


yt = YouTube(download_link)


def repeat(running):
    while running:
        print('\n'
   """
      '''''''''''''''''''''''''''''''''''''''
      '         INPUT:                      '
      '   V  - to video without sound       '
      '   M  - music                        '
      '   VM - video with music             '                   
      '                                     '
      '''''''''''''''''''''''''''''''''''''''
      """)
        print("\n")
        global choice_filter 
        choice_filter= input("Enter: ")
        print("\n")
        if choice_filter == "M":
            stream = yt.streams.filter(only_audio = True, file_extension='mp4')
            running = False
        elif choice_filter == "V":
            stream = yt.streams.filter(only_video = True, file_extension='mp4')
            running = False
        elif choice_filter == "VM":
            stream = yt.streams.filter(progressive = True, file_extension='mp4')
            running = False

    
    return stream
    # Don't wanna get choice_filter =/


def main():
    stream = repeat(running)
    reverse_list = ""
    for i in (stream):
        reverse_list += str(i)

    if choice_filter == "M":
        pattern_search = (r'(abr="[1-9]{3}kbps)"')
    else:
        pattern_search = (r'(res="[+]?\d+p)')

        
    pattern_result = re.findall(pattern_search, reverse_list)

    
    #pattern
    reverse_str = str(pattern_result)
    clean_str = reverse_str.replace("'",'').replace('"', '').replace('(', '').replace(')', '').replace(',','').replace('[', '').replace("]",'')
    spl_string = clean_str.split()


    # Add pattern to value after every iteration
    if choice_filter == "M":
        result = list(s + template_music for s in spl_string)
    else:
        result = list(s + template_video for s in spl_string)

    view_template = result.copy()

    count = 1
    for x in view_template:
        print(f"{count}. {x}")
        count += 1

    print("\n")
    #pattern
    if choice_filter == "M":
        input_resolution = input("Choice abr bitrate like: 128kbps: ")
        filter_to_download = stream.filter(subtype="mp4", abr=input_resolution).first()
    else:
        input_resolution = input("Type video resolution. For example: 1080p or 144p: ")
        filter_to_download = stream.filter(subtype="mp4", resolution=input_resolution).first()



    filter_to_download.download()

        

main()
