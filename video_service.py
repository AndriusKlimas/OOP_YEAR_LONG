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

    @staticmethod
    def view_video_play_svc( video_ids: list[int], user_service: UserService) -> list[tuple[str, int, object]]:
        """Get all play records for a specified video

        Args:
            video_ids (list[int]): List of video ids that match
            user_service (UserService): User service object.

        Returns:
            list[tuple[str, int, object]]: All play records for a specified video

        Raises:
            ValueError: If video_ids is empty or invalid.
        """
        try:
            if not video_ids:
                raise ValueError("No video IDs provided")

            users_dict = user_service.get_usable_user_data()
            records_found = []

            for username, user_obj in users_dict.items():
                user_history = user_obj.get_history()
                for vid_id, play_records_list in user_history.items():
                    if vid_id in video_ids:
                        for record in play_records_list:
                            records_found.append((username, vid_id, record))

            return records_found

        except Exception as e:
            logger.error(f"Error retrieving play records for videos: {e}")
            return []

    def print_videos_svc (self) -> list:
        """Print all videos in the dictionary

        returns:
            all_videos (list[tuple[str, int, object]]): All videos in the dictionary

        """
        all_videos = []
        try:
            for title, video_list in self.__usable_video_data.items():
                if isinstance(video_list, list):
                    for video in video_list:
                        all_videos.append(video)
                else:
                    print(video_list)
                    all_videos.append(video_list)

            return all_videos
        except TypeError as e:
            logger.error("TypeError in print_videos: videos_dictionary must be a dictionary: %s", e)
        except Exception as e:
            logger.error("Unexpected error while printing videos: %s", e)



    def video_search_srv(self, search_video: str) -> list:
        """Search video by name"""
        try:
            search_video = search_video.strip().lower()
            for title, video_list in self.__usable_video_data.items():
                if search_video == title.strip().lower():
                    return video_list

            return None

        except Exception as e:
            logger.error("Unexpected error searching for videos: %s", e)
            return None

    def search_genre_srv(self, search_genre: str) -> list:
        search_genre = search_genre.strip().lower()
        found = False
        valid_videos = []

        # goes through all videos in the dictionary
        for title, genre_list in self.__usable_video_data.items():
            for video in genre_list:
                # gets the genres from the class object using the fucntion
                video_genres = Video.get_genres(video)
                if search_genre in video_genres:
                    valid_videos.append(video)
                    found = True
        if not found:
            logger.info("No videos found with genre: %s", search_genre)
            return None

        return valid_videos

    def new_video_svr(self):
        """Create a new video record"""

        print("under contruction")