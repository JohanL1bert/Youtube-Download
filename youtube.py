import pytube, re






def inpu():
	global ytlink
	while True:
		try:
			link = input()
			if "http" in link:
				ytlink = pytube.YouTube(link)
				video = ytlink.streams.all()
				break
			else:
				print ("Only links")
		except ValueError:
				link = None

inpu()


print ("Type VIDEO or AUDIO to choose")
inp = (input(str()))



def videomp():
	yt_videomp = ytlink.streams.filter(only_video = True).all()
	ab = 1
	for ds in yt_videomp:
		print (str(ab) +"." +str(ds))
		ab +=1



def audio():
	yt_audio = ytlink.streams.filter(only_audio=True).all()
	ad = 1
	for da in yt_audio:
		print (str(ad) +"." + str(da))
		ad +=1

if inp == "VIDEO":
	videomp()
elif inp == "AUDIO":
	audio()


