from dataclasses import dataclass


@dataclass
class YoutubeVideo:
    id: str
    publishedAt: str
    channelId: str
    channelTitle: str
    title: str
    description: str
    thumbnails: dict
    liveBroadcastContent: str
    publishTime: str

@dataclass
# class YoutubeChannel:
