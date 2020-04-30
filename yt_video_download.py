import youtube_dl,os

yd = {}
path = 'E:/memory'
os.chdir(path)
url = 'https://youtu.be/mt9xg0mmt28'
with youtube_dl.YoutubeDL(yd) as y:
    print("Downloading..."+url)
    y.download([url])
print("Video downloaded")