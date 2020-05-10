from playsound import playsound
import glob
def create_playlist(path):
    for song in glob.glob(path):
        print("Playing...",song)
        playsound(song)
create_playlist("E:memory/kushal choice/*.mp3")