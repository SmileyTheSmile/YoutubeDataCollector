from pytube import YouTube


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_audio_only()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


if __name__ == '__main__':
    with open('file.csv', 'w') as file:
        file.write("ffsdf")

    #link = input("Enter the YouTube video URL: ")
    #Download(link)
