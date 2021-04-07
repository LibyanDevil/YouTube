try:
	from pytube import YouTube, Playlist
	from pytube.cli import on_progress
	import os
	from humanize import naturalsize
except Exception as e:
	print("Some Modules Are Missing {}".format(e))


if os.name == "nt":
	os.system("cls")

elif os.name == "prosix":
	os.system("clear")
else:
	os.system("cls || clear")


BANNER = ("""
		      \033[1;31m███████████████\033[1;31m
		      \033[0;30m███████████████\033[1;31m
		      \033[0;32m███████████████\033[1;31m
	\033[1;33m============================================\033[0m
	\033[1;32m|               Hello World                |\033[0m
	\033[1;33m============================================\033[0m
	\033[1;33m|           Download With Python           |\033[0m
	\033[1;33m============================================\033[0m
	\033[1;31m|               Libyan_Devil               |\033[0m
	\033[1;33m============================================

		1 = Video
		2 = PlayList		  \033[0m""")

print(BANNER)



def youtube():



	user = input("\033[1;33m >>> Enter URL : \033[0m")

	try:
		vid = YouTube(user,on_progress_callback=on_progress)
		mb = naturalsize(vid.streams.filter(file_extension='mp4').get_highest_resolution().filesize)
		print("\033[1;33m ===================\033[0m")
		print(" >>> Video Name : ",vid.title)
		print(" >>> Video Size : ",mb)
		print("\033[1;33m ===================\033[0m")


		vid.streams.get_highest_resolution().download()
		print("\033[0;32m================Downloaded==================\033[0m \n")
	except EOFError as err:
		print(err)


def Play_list():


	user = input("\033[1;33m >>> Enter URL : \033[0m")
	vid = Playlist(user)
	print(" >>> Playlist Name : ",vid.title)
	print(" ================================================= ")
	folder = vid.title
	for i in vid.video_urls:
		youtube = YouTube(i,on_progress_callback=on_progress)
		mb = naturalsize(youtube.streams.get_highest_resolution().filesize)
		print(" >>> Video Name : ",youtube.title)
		print(" >>> Video Size : ",mb)
		v = youtube.streams.get_highest_resolution().download(folder)
		print(" ================================================= ")

while True:
	
	PC = input("\033[1;33m >>> \033[0m")

	if PC == "1":
		youtube()

	elif PC == "2":
		Play_list()
		
	else:
		print("\033[1;31m >>> Please enter a viled number\033[0m")
