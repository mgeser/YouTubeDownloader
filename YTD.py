from pytube import YouTube


link = str(input("Input Your URL Here!: "))
def video():
    YouTube(link).streams.get_highest_resolution().download()
def audio():
    YouTube(link).streams.get_audio_only().download()

print("""
1. Download Video
2. Download Audio Only
""")

var = int(input("Masukkan Pilihan!: "))

if var == 1:
    print("Downloading Video")
    video()
    print("Video Downloaded")
elif var == 2:
    print("Downloading Audio")
    audio()
    print("Audio Downloaded")
else:
    print("unknown command")