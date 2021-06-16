import re, os
from pytube import YouTube
from urllib.parse import urlparse


# CONST and PATTERN
RUNNING = True
TEMPLATE_VIDEO = " type=video"
TEMPLATE_MUSIC = " type=music"
ARRAY_WORDS = ['VM', 'vm', 'V', 'v', 'M', 'm']
TEMPLATE =(  
   """
      '''''''''''''''''''''''''''''''''''''''
      '         INPUT:                      '
      '   V  - to video without sound       '
      '   M  - music                        '
      '   VM - video with music             '                   
      '                                     '
      '''''''''''''''''''''''''''''''''''''''
      """)



def create_folder():
    try:
        os.makedirs('Download_Youtube')
    except FileExistsError:
        pass


def valid_link():
    while True:
        download_link = input("Enter link to download: ")
        o_parse = urlparse(download_link)
        if o_parse.scheme == "https" and o_parse.netloc == "www.youtube.com":
            break
        else:
            print("Link is not valid ")
    
    return download_link


def status_choice(run):
    while run: 
        print('\n')
        print(TEMPLATE)
        print('\n')
        choice_filter = input('Enter: ')
        if choice_filter not in ARRAY_WORDS:
            print('Not valid words')
            continue
        else:
            break

    return choice_filter


def choice_filter(yt, choice):
    if (choice in ('M', 'm')):
        stream = yt.streams.filter(only_audio = True, file_extension='mp4')
    elif (choice in ('V', 'v')):
        stream = yt.streams.filter(only_video = True, file_extension='mp4')
    elif (choice in ('VM', 'vm')):
        stream = yt.streams.filter(progressive = True, file_extension='mp4')

    return stream, choice


def to_string(stream_obj):
    reverse_list = ''
    for i in (stream_obj):
        reverse_list += str(i)
    
    return reverse_list


def choice_pattern(youtube_choice, str_stream):
    if youtube_choice in ('M', 'm'):
        pattern_search = (r'(abr="[1-9]{3}kbps)"')
    else:
        pattern_search = (r'(res="[+]?\d+p)')
    
    pattern_result = re.findall(pattern_search, str_stream)
    return pattern_result


def clear_pattern(pattern,):
    str_patt = str(pattern)
    clean_str = str_patt.replace("'",'').replace('"', '').replace('(', '').replace(')', '').replace(',','').replace('[', '').replace("]",'')
    spl_string = clean_str.split()
    return spl_string


def creat_list_patt(choice, TEMPLATE_MUSIC, TEMPLATE_VIDEO, splitted_string):
    if choice in ('M', 'm'):
        result = list(s + TEMPLATE_MUSIC for s in splitted_string)
    else:
        result = list(s + TEMPLATE_VIDEO for s in splitted_string)

    view_template = result.copy()
    return view_template


def view(view_temp):
    count = 1
    for i in view_temp:
        print(f"{count}. {i}")
        count += 1


def download_stream_filter(choice, stream):
    if choice in ('M', 'm'):
        input_resolution = input("Choice abr bitrate like: 128kbps: ")
        filter_to_download = stream.filter(subtype="mp4", abr=input_resolution).first()
    else:
        input_resolution = input("Type video resolution. For example: 1080p or 144p: ")
        filter_to_download = stream.filter(subtype="mp4", resolution=input_resolution).first()

    return filter_to_download


def download_path(obj_dow):
    obj_dow.download('Download_Youtube')


def main():
    create_folder()
    download = valid_link()
    yt = YouTube(download)
    choice_filt = status_choice(RUNNING)
    stream_obj, youtube_stream_choice = choice_filter(yt, choice_filt)
    string_obj_stream = to_string(stream_obj)
    get_pattern = choice_pattern(youtube_stream_choice, string_obj_stream)
    split_string = clear_pattern(get_pattern)
    view_temp = creat_list_patt(youtube_stream_choice, TEMPLATE_MUSIC, TEMPLATE_VIDEO, split_string)
    view(view_temp)
    get_downloadt_stream = download_stream_filter(youtube_stream_choice, stream_obj)
    download_path(get_downloadt_stream)


main()
