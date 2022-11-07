from pytube import YouTube
import os
# url input from user
yt = YouTube(
    str(input("Enter the URL of the video: \n>> ")))
video = yt.streams.filter(only_audio=True).first()
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'

print("Title:",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length,"seconds")
#ys= yt.streams.get_highest_resolution()
out_file = video.download(output_path=destination)
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
print("Downloading...")
print(yt.title + "\n Download completed")