from googleapiclient.discovery import build
import random

DEVELOPER_KEY = 'AIzaSyApEnin2TzAI7zPzrGqrwP6UvPU6yTw5Vw'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

prefix = ['IMG ', 'IMG_', 'IMG-', 'DSC ']
postfix = [' MOV', '.MOV', ' .MOV']


def get_youtube_videos(videos_num: int):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    query = random.choice(prefix) + str(random.randint(999, 9999)) + random.choice(postfix)
    search_response = youtube.search().list(
        q=query,
        part='snippet',
        maxResults=videos_num
    ).execute()

    videos = []

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append('%s' % (search_result['id']['videoId']))

    return search_response.get('items', [])


for video in get_youtube_videos(10):
    for key, item in video.items():
        print(f"{key}, {item}")
    for key, item in video["snippet"].items():
        print(f"{key}, {item}")
    print()
