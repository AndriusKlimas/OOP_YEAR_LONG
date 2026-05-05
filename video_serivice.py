from video_data_access import *
from catalogue import *

class VideoService:
    def __init__(self, video_data):
        self.__video_data = video_data

        self.__usable_video_data = {}
