

class VideoService:
    def __init__(self, video_data):
        self.__video_data = video_data

        self.__usable_video_data = {}



    def load_serv_video(self):
        if not self.__video_data:
            raise AttributeError("No user_data class present- cannot load data")

        self.__usable_video_data = self.__video_data.load()

        # Print all loaded usernames, for testing
        print("\n✅ Users loaded:")
        for video_name in self.__usable_video_data.keys():
            print(f"  - {video_name}")
        print(f"Total users: {len(self.__usable_video_data)}\n")