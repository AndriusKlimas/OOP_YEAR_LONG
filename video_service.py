from user_service import UserService
from video_data_access import *

class VideoService:
    def __init__(self, video_data: IVideoDataAccess):
        self.__video_data = video_data

        self.__usable_video_data = {}


    def load_serv_video(self):
        if not self.__video_data:
            raise AttributeError("No user_data class present- cannot load data")

        self.__usable_video_data = self.__video_data.load()

        # Print all loaded usernames, for testing
        print("\n✅ Videos loaded:")
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

    def new_video_svr(self,get_title:str ,get_description:str ,get_duration:int ,get_release_year:int ,genres_list: list ):
        """Create a new video record"""
        try:
            # video id no longer key, now goes through dict, counts, and then adds 1 onto for new video id
            get_video_id = 0
            for video_list in self.__usable_video_data.values():
                for video in video_list:
                    get_video_id += 1
            get_video_id += 1

            # creating a new video class object
            try:
                new_video = Video(get_video_id, get_title, get_description, get_duration, get_release_year, genres_list)
            except Exception as e:
                logger.error("Unexpected error while creating new video class object: %s", e)

            # 'checking if he video is in the dictionary'
            if get_title in self.__usable_video_data.keys():
                # 'if it is then add the class object under hte same key'
                self.__usable_video_data[get_title].append(new_video)
                # 'if not then add the class object under a new key'
            else:
                self.__usable_video_data[get_title] = [new_video]

            self.__video_data.store(self.__usable_video_data)

        except AttributeError:
            logger.error("Attribute error while creating new video: %s", e)

        except TypeError:
            logger.error("TypeError while creating new video: %s", e)

        except Exception as e:
            logger.error("Unexpected error while creating new video")


    def video_remover_amount_srv(self,remove_video:str):
        # stripping white spaces again, causes issues if not their
        search_video = remove_video.strip().lower()
        # to store the videos found
        videos_found = []

        # searching through the videos and adding them to teh list
        for title, video_list in self.__usable_video_data.items():
            if search_video == title.strip().lower():
                title_key = title
                if isinstance(video_list, list):
                    videos_found = video_list
                else:
                    videos_found = [video_list]
                break

        # if none are found then return None
        if not videos_found:
            logger.info("video_remover: No video found in dictionary")
            return None, None

        if len(videos_found) > 1:
            return True, videos_found

        if len(videos_found) == 1:
            return False, videos_found

    def video_remover_single_srv(self, videos_found: list, title_key: str) -> bool:
        removed_video = videos_found[0]
        videos_found.pop(0)

        if not videos_found:
            del self.__usable_video_data[title_key.strip().lower()]
            self.__video_data.store(self.__usable_video_data)

        return removed_video

        #
        # try:
        #     # stripping white spaces again, causes issues if not their
        #     search_video = remove_video.strip().lower()
        #     # to store the videos found
        #     videos_found = []
        #     # this will be used to store the title/key iof found
        #     title_key = None
        #
        #     # finding all videos
        #     for title, video_list in self.__usable_video_data.items():
        #         if search_video == title.strip().lower():
        #             title_key = title
        #             if isinstance(video_list, list):
        #                 videos_found = video_list
        #             else:
        #                 videos_found = [video_list]
        #             break

            # if the videos_found list is empty, then do the below
            # if not videos_found:
            #     logger.info("video_remover: No video found in dictionary")
            #     return False
            #
            # if len(videos_found) == 1:
            #     videos_found.pop(0)
            #     return False
            #
            # else:
            #     return videos_found

            # in this part will check how many iteams are added to teh list
            # if len(videos_found) > 1:
            #     for num, video in enumerate(videos_found, 1):
            #         print(
            #             f"{num}. Name= {Video.get_title(video)}, description = {Video.get_description(video)}, duration = {Video.get_duration_seconds(video)}, release_year = {Video.get_release_year(video)}"
        # except Exception as e:
        #     logger.error("Unexpected error while removing video: %s", e)
        #     print(f"An error occurred while removing video: {e}")
        #     return False

    def video_remover_multiple_srv(self, choice: int, videos_found: list, title_key: str) -> list:
        removed_video = None

        try:
            actual_remove = choice - 1
            removed_video = videos_found[actual_remove]
            videos_found.pop(actual_remove)
        except IndexError as e:
            logger.error("IndexError in video_remover:  choice chosen is out of range: %s", e)
            return None
        except ValueError as e:
            logger.error("ValueError in video_remover: Value provided is not an int: %s", e)
            return None

        # checking if ther list is not empty, if it is then remove the key for dictioanry
        if not videos_found:
            del self.__usable_video_data[title_key.strip().lower()]

        # IMPORTANT: Store the changes back to the JSON file
        self.__video_data.store(self.__usable_video_data)

        return removed_video
