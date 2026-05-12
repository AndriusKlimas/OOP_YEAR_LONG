from user_service import UserService
from video_data_access import *

class VideoService:
    def __init__(self, video_data: IVideoDataAccess):
        """
            Initializes the VideoService object.

            Parameters:
                video_data (IVideoDataAccess): The backend data access object for videos.
            """
        self.__video_data = video_data

        self.__usable_video_data = {}


    def load_serv_video(self):
        """
            Loads all videos from the data source into memory and prints their titles.

            Returns:
                None
            """
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

    def return_all_videos (self) -> list:
        """Returns a list of all video objects currently loaded.

    Returns:
        list: All video objects.

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



    def return_specific_videos(self, search_video: str) -> list:
        """
    Searches for videos by title.

    Parameters:
        search_video (str): The title to search for.

    Returns:
        list: List of video objects with the given title, or None if not found.
    """
        try:
            search_video = search_video.strip().lower()
            for title, video_list in self.__usable_video_data.items():
                if search_video == title.strip().lower():
                    return video_list

            return None

        except Exception as e:
            logger.error("Unexpected error searching for videos: %s", e)
            return None

    def return_videos_with_genre(self, search_genre: str) -> list:
        """Will go through dictionary and look for specific value

                    If key found then it will return all values

                    if not then returns none

                return:
                    valid_videos - if something found
                    None - if nothing found
                """
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

    def create_new_video(self,get_title:str ,get_description:str ,get_duration:int ,get_release_year:int ,genres_list:
    list ):
        """
    Adds a new video with the specified details.

    Parameters:
        get_title (str): The title of the video.
        get_description (str): The video's description.
        get_duration (int): The video's duration in seconds.
        get_release_year (int): The year the video was released.
        genres_list (list): List of genres to associate with the video.

    Returns:
        None
    """
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
        """ This willl get the amount of videos that can be removed

        Args:
            remove_video (str): The video Name to remove

        Return:
            video_found : The amount of videos that can be removed

        """
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
        """
            Removes a single video from the list and updates the video data store.

            Parameters:
                videos_found (list): The list of found video objects to remove from.
                title_key (str): The key associated with the video, used for deletion if the list is empty.

            Returns:
                bool: The removed video object.
            """
        removed_video = videos_found[0]
        videos_found.pop(0)

        if not videos_found:
            del self.__usable_video_data[title_key.strip().lower()]
            self.__video_data.store(self.__usable_video_data)

        return removed_video


    def video_remover_multiple_srv(self, choice: int, videos_found: list, title_key: str) -> list:
        """
            Removes a video from a list based on the user's selection and updates the video data store.

            Parameters:
                choice (int): The index (1-based) of the video selected for removal.
                videos_found (list): The list of video objects found that match the criteria.
                title_key (str): The key associated with the video(s), used for data deletion if list becomes empty.

            Returns:
                list: The video object that was removed, or None if no video was removed due to error.
            """
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

    def video_editor_display_srv(self) -> list:
        """
            Returns a numbered list of all videos for display in an editor UI.

            Returns:
                list: List of (video_number, title, video_object).
            """

        video_list = []
        video_number = 1

        # displays all the videos stored in a neat list
        for title, videos in self.__usable_video_data.items():
            for video in videos:
                video_list.append((video_number, title, video))
                video_number += 1

        return video_list


    def video_editor_chosen_return_srv(self, choice: int, video_list: list)-> tuple:
        """
            Returns the video and its title based on user's selection.

            Parameters:
                choice (int): The index (number) of the selected video.
                video_list (list): List of (video_number, title, video_object).

            Returns:
                tuple: (video, title) if found; otherwise (None, None).
            """
        try:
            choice = int(choice)
        except ValueError:
            logger.info("video_editor: No video selected")
            return None, None

            # looping through everything on the video_list
        for num, title, video in video_list:
            if num == choice:
                return video, title

            # if nothing was selected
        if choice > len(video_list) or choice < 1:
            logger.info("video_editor: No video selected")
            return None, None


    def video_editor_description_change_srv(self,selected_video, new_description: str) -> bool:
        """
            Updates the description of the selected video.

            Parameters:
                selected_video (object): The video to update.
                new_description (str): The new description.

            Returns:
                bool: True if changed successfully, False otherwise.
            """
        try:
            selected_video.description = new_description.strip()

            # Save changes to JSON file
            self.__video_data.store(self.__usable_video_data)
            return True

        except ValueError as e:
            logger.error("ValueError in video_editor: description input error: %s", e)
            return False

    def video_editor_duration_change_srv(self, selected_video, new_duration: int) -> bool:
        """
            Updates the duration of the selected video.

            Parameters:
                selected_video (object): The video to update.
                new_duration (int): The new duration.

            Returns:
                bool: True if changed successfully, False otherwise.
            """
        try:
            selected_video._duration_seconds = new_duration

            # Save changes to JSON file
            self.__video_data.store(self.__usable_video_data)
            return True

        except ValueError as e:
            logger.error("ValueError in video_editor: duration input must be a number %s", e)
            return False


    def video_editor_year_change_srv(self,selected_video, new_year: int) -> bool:
        """
            Updates the release year of the selected video.

            Parameters:
                selected_video (object): The video to update.
                new_year (int): The new release year.

            Returns:
                bool: True if changed successfully, False otherwise.
            """
        try:
            selected_video._release_year = new_year

            # Save changes to JSON file
            self.__video_data.store(self.__usable_video_data)
            return True

        except ValueError as e:
            logger.error("ValueError in video_editor: year input must be a number %s", e)
            return False

    def genre_add_srv(self,selected_video, new_genre: str)-> tuple:
        """
            Adds a genre to the selected video if not present.

            Parameters:
                selected_video (object): The video object to update.
                new_genre (str): The genre to add.

            Returns:
                tuple: (True, message) if added, (False, message) if failed.
            """

        # Check if genre is already in the video
        if selected_video.check_genre(new_genre):
            return False, f"Genre '{new_genre}' is already in the video"

        # Try to add the genre
        if selected_video.add_genre(new_genre):
            # Save changes to JSON file
            self.__video_data.store(self.__usable_video_data)
            return True, f"Genre '{new_genre}' added!"
        else:
            return False, f"Genre '{new_genre}' is invalid or already exists."


    def genre_remove_srv(self, selected_video, genre_to_remove: str) -> tuple:
        """
            Removes a genre from the selected video.

            Parameters:
                selected_video (object): The video to update.
                genre_to_remove (str): The genre to remove.

            Returns:
                tuple: (True, message) if removed, (False, message) if not found.
            """
        # Check if video has any genres
        if not selected_video.get_genres():
            return False, "Video has no genres."

        # Check if genre is in the video
        if genre_to_remove in selected_video.get_genres():
            selected_video._genres.remove(genre_to_remove)
            # Save changes to JSON file
            self.__video_data.store(self.__usable_video_data)
            return True, f"Genre '{genre_to_remove}' removed!"
        else:
            return False, f"Genre '{genre_to_remove}' is not in this video."
