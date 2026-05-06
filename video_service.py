from user_service import UserService
from video_data_access import *

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
        print(f"Total videos: {len(self.__usable_video_data)}\n")

    @staticmethod
    def sec_to_min(seconds: int) -> str:
        """Convert seconds to a human-readable minutes and seconds string.

            Args:
                seconds (int): Number of seconds

            Returns:
                str: Formatted string in the form "N minutes and M seconds".
            """
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes} minutes and {secs} seconds"

    def get_usable_video_data(self) -> dict:
        """Get usable video data.

        Returns:
            dict: Usable video data.
        """
        return self.__usable_video_data

    def play_video_user_svc(self, username: str, user_service: UserService, video_id: int) -> bool:
        """Play a video user by username.

        Args:
            username (str): Username of the user to play a video.
            user_service (UserService): User service object.
            video_id (int): Video id to play a video.

        Returns:
            bool: True of play record created successfully. False otherwise.

        """
        try:
            users_dict = user_service.get_usable_user_data()

            if username not in users_dict:
                return False

            users_dict[username].start_play(video_id)
            return True

        except Exception as e:
            logger.error(f"Error creating play record for user {username}: {e}")
            return False