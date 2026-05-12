#imports annotations for type hinting
from __future__ import annotations

import json
import logging.config

from catalogue import Video
from user_records import User
from user_service import UserService
from user_data_access import JSONUserDataAccess
from user_data_access import TextUserDataAccess
from video_service import VideoService
from video_data_access import JSONVideoDataAccess
from video_data_access import DefaultVideoDataAccess

def config_log_json() -> None:
    """function to bring in the json logging config file"""
    with open ("logging_config.json", "r") as f:
        config = json.load(f)
    logging.config.dictConfig(config)

config_log_json()
logger = logging.getLogger(__name__)

def load_user_model() -> UserService:
    """
    Loads the user model or default user data based on user input.
    """
    filename = ""
    try:
        filename = input("Enter the path of the user model file or 'default: ").strip()

        if filename.lower() == "videos.json":
            logger.error("Trying to access the videos.json file instead of users file")
            return None

        if filename.lower() == "default":
            user_doa = TextUserDataAccess()
        else:
            user_doa = JSONUserDataAccess(filename)

        user_service = UserService(user_doa)
        user_service.load_serv_user()
        return user_service
    except FileNotFoundError as e:
        logger.error(f"File {filename} not found")
        return None

def load_video_model() -> VideoService:
    """
    Loads the video model or default video data based on user input.
    """
    filename = ""
    try:
        filename = input("Enter the path of the video model file or 'default': ").strip()

        if filename.lower() == "users.json":
            logger.error("Trying to access the users file instead of videos file")
            return None

        if filename.lower() == "default":
            video_doa = DefaultVideoDataAccess()
        else:
            video_doa = JSONVideoDataAccess(filename)

        video_service = VideoService(video_doa)
        video_service.load_serv_video()
        return video_service
    except FileNotFoundError as e:
        logger.error(f"File {filename} not found")
        return None





#Option 1 def
def print_videos() -> None:
    """
    Prints all videos from the video service.
    """
    returned_videos = video_service.return_all_videos()
    for video in returned_videos:
        print(video)

#Option 2 def
def video_search() -> Video | None:
    """
    Searches for a video by title and prints the results.
    """
    search_video = input("Enter the title of the video to search for: ")
    video_info = video_service.return_specific_videos(search_video)

    if video_info is not None:
        # isinstance is used to check if the iteam retuernd is a list, if it is then do the below source
        # w3schools, stackoverflow
        if isinstance(video_info, list):
            for video in video_info:
                print(video)
        else:
            print(video_info)
    else:
        logger.info("user functions: video chosen not found")
        print("Video not found.")


#Option 3 def
def search_genre() -> None:
    """
    Searches for and prints videos matching a user-specified genre.
    """
    try:
        # loops through dictionary and stores the video info in video variable
        #whitespace again causing issues
        search_video_genre = input("Please enter the genre you would like to look for: ")
        in_valid_genres = Video.validate_genre(search_video_genre)
        if in_valid_genres == True:
            valid_videos = video_service.return_videos_with_genre(search_video_genre)

        else:
            logger.info("user functions: genre chosen not found in valid genres")
            print("Genre not valid.")

        if valid_videos is not None:
            # isinstance is used to check if the iteam retuernd is a list, if it is then do the below source
            # w3schools, stackoverflow
            if isinstance(valid_videos, list):
                for video in valid_videos:
                    print(video)
            else:
                print(valid_videos)
        else:
            logger.info("user functions: video chosen not found")
            print("Video not found.")

    except TypeError as e:
        logger.error("TypeError in search_genre: videos_dictionary must be a dictionary: %s", e)
        print("Error: videos_dictionary must be a dictionary")
    except Exception as e:
        logger.error("Unexpected error while searching for genre: %s", e)
        print(f"An error occurred while searching for genre: {e}")

#option 4 def
def show_user_history(videos_dict: dict) -> None:
    """ shows the user's play history

    Args:
        videos_dict (dict): dictionary of all videos
    """
    try:
        username = logged_in_usernmae
        history = user_service.show_user_history_svc(username, videos_dict)

        print(f"Here is the play history for {username}")
        for line in history:
            print(line)

    except KeyError as e:
        logger.error("Missing key while showing user history: %s", e)
        print("An error occurred while showing user history")
    except AttributeError as e:
        logger.error("Attribute error while showing user history: %s", e)
        print("An error occurred while showing user history")
    except Exception as e:
        logger.error("Unexpected error while showing user history: %s", e)
        print("An error occurred while showing user history")

#option 5 def
def play_video_user(user_service, video_service) -> None:
    """ creates a play record

    Args:
        users_dict (dict): dictionary of all users
        videos_dict (dict): dictionary of all videos
    """
    try:
        username = logged_in_usernmae
        videos_dict = video_service.get_usable_video_data()

        video_title = input("Please enter the title of the video: ").strip()
        videos_found = video_service.return_specific_videos(video_title)

        if videos_found is None:
            print("Invalid title entered")
            logger.error("Invalid title entered")
            return

        if not isinstance(videos_found, list):
            videos_found = [videos_found]

        selected_video = None
        if len(videos_found) > 1:
            print("Multiple videos found with that title:")
            for id, video_obj in enumerate(videos_found, start=1):
                print(
                    f"{id}. ID: {video_obj.get_video_id()} | "
                    f"Description: {video_obj.get_description()} | "
                    f"Year: {video_obj.get_release_year()}"
                )

            try:
                choice = int(input("Please choose one (numbers only): ").strip())
                selected_video = videos_found[choice - 1]
            except (ValueError, IndexError):
                print("Invalid selection")
                logger.error("Invalid selection")
                return
        else:
            selected_video = videos_found[0]

        success = video_service.play_video_user_svc(username, user_service, selected_video.get_video_id())

        if success:
           print(f"{username} is now playing {selected_video.get_title()}")
        else:
            print("Error creating play record")
            logger.error("Error creating play record")

    except Exception as e:
        logger.error("Unexpected error while playing video: %s", e)
        print("An error occurred while playing video: %s", e)


#Option 6 def
def new_video() -> None:
    """Interactively collects details from the user to add a new video entry.

        The function prompts the user to enter information required for a new video:
        - Title
        - Description
        - Duration (validated to ensure it is a number)
        - Release year (validated to ensure it is a number)
        - Genres (user can add multiple genres, each must be valid as defined by `Video.return_valid_genres()`)

        Once all data is successfully collected and validated, a new video is created using create_new_video()

    """
    genres_list = []
    try:
        print("Please enter the following details to add a new video: ")
        get_title = input("Title: ")
        get_description = input("Description: ")
        valid_duration = False
        while not valid_duration:
            try:
                get_duration = int(input("Duration seconds: "))
                valid_duration = True
            except ValueError:
                print("Error: Duration must be a number. Please try again.")

        # Getting release year
        valid_year = False
        while not valid_year:
            try:
                get_release_year = int(input("Release Year: "))
                valid_year = True
            except ValueError:
                print("Error: Release Year must be a number. Please try again.")

    except ValueError as e:
        logger.error("ValueError in new_video input: Duration and Release Year must be numbers: %s", e)
        print("Error: Duration and Release Year must be numbers.")

    # loop for genre, user adding genres
    while True:
        get_genres = input("Please enter the genres")
        if get_genres in Video.return_valid_genres():
            genres_list.append(get_genres)
        else:
            logger.info("new_video: genre does not exist: %s", get_genres)
            print("Genre not valid. Please choose a valid genre")
            print(Video.return_valid_genres())
        print("Would you like to add another genre? (y/n)")
        another = input().lower()
        if another == "n":
            break
    video_service.create_new_video(get_title,get_description,get_duration,get_release_year,genres_list)


#Option 7 def
def video_remover():
    """this gets in inputs from the user to remove a video

        Will ask user to choose between videos of same title if they are the same.
        Once user chooses, chosen one will be removed.
        If no more values in the key then key gets removed from dict
    """
    #ps need comments for this as its complex
    remove_video = input("Please enter the name of the video you would like to remove: ")
    # calling the method to remove the video
    valid , videos_found = video_service.video_remover_amount_srv(remove_video)

    if valid is None:
        print("Video not found")

    if valid == True:
        for num, video in enumerate(videos_found, 1):
            print(f"{num}. Name= {Video.get_title(video)}, description = {Video.get_description(video)}, duration = {Video.get_duration_seconds(video)}, release_year = {Video.get_release_year(video)}")

        try:
            choice = int(input("Please choose one (numbers only): ").strip())
        except ValueError:
            print("Please enter a valid format")
            choice = None
        if choice is not None:
            removed = video_service.video_remover_multiple_srv(choice, videos_found, title_key = remove_video)
            print(f"removed1: {removed}")

        else:
            print("Skipping removal due to invalid input")




    if valid == False:
        removed= video_service.video_remover_single_srv(videos_found, title_key = remove_video)
        print(f"removed: {removed}")


def video_editor():
    """
    Allows the user to edit details of a selected video.

    Allows for change of
        - description
        - duration (validated to ensure it is a number)
        - release year (validated to ensure it is a number)
        - genres add and remove
    """
    print("See all videos below:")

    video_list = video_service.video_editor_display_srv()

    for video_number, title, video in video_list:
        print(f"\n{video_number}. Video ID: {Video.get_video_id(video)}")
        print(f"   Title: {Video.get_title(video)}")
        print(f"   Description: {Video.get_description(video)}")
        print(f"   Duration: {Video.get_duration_seconds(video)} seconds")
        print(f"   Release Year: {Video.get_release_year(video)}")
        print(f"   Genres: {', '.join(Video.get_genres(video)) if Video.get_genres(video) else 'No genres'}")

    selected_video = None
    selected_title = None

    while selected_video is None:
        try:
            choice = int(input("Please enter the one you would like to edit (numbers only): "))
            selected_video, selected_title = video_service.video_editor_chosen_return_srv(choice, video_list)
            print(f"selected video: {selected_video}")

        except ValueError:
            logger.info("video_editor: No video selected")
            print("Invalid selection.")


    #printing oput what the admin wants to do
    print("\n What would you like to edit?")
    print("1. Description")
    print("2. Duration (seconds)")
    print("3. Release Year")
    print("4. Genres ")
    print("0. Cancel")

    edit_choice = input("Please enter your choice(numbers only): ").strip()

    #will change the description using direct access
    # will change the description
    if edit_choice == "1":
        new_description = input("Please enter the new description you would like: ")
        if video_service.video_editor_description_change_srv(selected_video, new_description):
            print("New description has been changed")
            print(selected_video)
        else:
            print("Invalid input. Description must be a non-empty string.")

    # will change the duration
    elif edit_choice == "2":
        new_duration = None
        while new_duration is None:
            try:
                new_duration = int(input("Enter new duration (in seconds): "))
                if video_service.video_editor_duration_change_srv(selected_video, new_duration):
                    print("Duration updated!")
                    print(selected_video)
                else:
                    print("Invalid input. Duration must be a number.")
            except ValueError:
                print("Invalid input. Duration must be a number.")
                new_duration = None

    # will change the release year using direct access
    elif edit_choice == "3":
        new_year = None
        while new_year is None:
            try:
                new_year = int(input("Enter new release year: "))
                if video_service.video_editor_year_change_srv(selected_video, new_year):
                    print("Release year updated!")
                    print(selected_video)
                else:
                    print("Invalid input. Release year must be a number.")
            except ValueError:
                print("Invalid input. Release year must be a number.")
                new_year = None

    #if option 4 ius chosen run the below
    elif edit_choice == "4":
        print("\n Genre Options:")
        print("1. Add a genre")
        print("2. Remove a genre")
        print("0. Cancel")

        genre_choice = input("Please enter your choice(numbers only): ").strip()

        #if 1 is inputed, it will run and user will input the new genre they want
        if genre_choice == "1":
            valid_genres = Video.return_valid_genres()
            print(f"Valid genres: {', '.join(valid_genres)}")

            new_genre = input("Enter genre to add: ").strip()

            success, message = video_service.genre_add_srv(selected_video, new_genre)

            if success:
                print(message)
                logger.info("video_editor genre add: Chosen added successfully")
                print(selected_video)
            else:
                print(message)
                logger.info("video_editor genre add: Chosen genre does not exist")

        #if choice 2 then run the below, will print out what genres are in the video and allow for removal
        elif genre_choice == "2":
            current_genres = selected_video.get_genres()

            if current_genres:
                print(f"Current genres: {', '.join(current_genres)}")
                genre_to_remove = input("Enter genre to remove: ").strip()

                success, message = video_service.genre_remove_srv(selected_video, genre_to_remove)

                if success:
                    print(message)
                    logger.info("video_editor genre remove: Chosen removed successfully")
                    print(selected_video)
                else:
                    print(message)
                    logger.info("video_editor genre remove: Chosen genre does not exist")
            else:
                logger.info("video_editor genre: Video chosen has no genres")
                print("Video selected has no genres.")

        elif genre_choice == "0":
            print("Canceled")
            return None
        else:
            print("Invalid input. Please enter a valid choice.")
            return None




def view_video_play(user_service, video_service) -> None:
    """Allow the user to see all play history for a specified video.

    Args:
        video_dict (dict): Dictionary of video information
        users_dict (dict): Dictionary of users information
    """
    try:
        video_name = input("Please enter the video you would like to view the play history of: ").strip()

        videos_dict = video_service.get_usable_video_data()
        matched_videos = video_service.return_specific_videos(video_name)

        if matched_videos is None:
            print("Invalid video entered")
            logger.error("Invalid video entered")
            return

        # Normalise to list in case one object is returned.
        if not isinstance(matched_videos, list):
            matched_videos = [matched_videos]

        matched_video_ids = [video_obj.get_video_id() for video_obj in matched_videos]

        records_found = video_service.view_video_play_svc(matched_video_ids, user_service)

        print(f"\nPlay history for '{video_name}':")

        if len(records_found) == 0:
            print("No play history found for this video.")
            return

        for username, vid_id, record in records_found:
            print(f"User: {username} | Video ID: {vid_id} | Position: {VideoService.sec_to_min(record.get_pos())}")

    except Exception as e:
        print(f"An error occurred while viewing play history: {e}")
        logger.error("An error occurred while viewing play history")


def user_login() -> tuple[bool, str]:
    """ aks user to login by providing credentials
    Passes the info to check_login_info()

    Returns:
        tuple[bool, str]
        True if the user is logged in, False otherwise


    """
    username = input("Username: ")
    password = input("Password: ")
    valid, valid_name = user_service.check_login_info(username, password)
    return valid, valid_name


def create_login() -> tuple[bool, str]:
    """ getting user input for new login, passes info to create_login_srv


    Returns:
        tuple[bool, str]: A tuple containing:
            - bool: True if creation failed, False if successful
            - str: Error message if failed, username if successful

    raises:
    ValueError: Invalid input provided
    KeyError: Users dictionary not found
    Exception: An unexpected error occurred during account creation
    """

    try:
        print("Welcome new user")
        print("Please enter the username you would like: ")
        username = input().strip()
        print("Please enter the password you would like: ")
        password = input().strip()
        valid, username = user_service.create_login_srv(username, password)
        return valid, username

    except KeyError as e:
        logger.error("KeyError in create_login: Users dictionary not found %s", e)
        print("Error: Users dictionary not found")
        return True, "Error: Users dictionary not accessible"
    except ValueError as e:
        logger.error("ValueError in create_login: Invalid input provided %s", e)
        print("Error: Invalid input provided")
        return True, "Error: Invalid input"
    except Exception as e:
        logger.error("Unexpected error during create_login: %s", e)
        print(f"An error occurred during account creation: {e}")
        return True, "An unexpected error occurred during account creation"


#creating a normal login funtion
def normal_login():
    """Handle user login or account creation menu loop.

        Returns:
            str: Username of logged-in or newly created user.

        Raises:
            SystemExit: When user selects exit option.
        """
    keep_going = True
    while keep_going:
        print("Please choose form one of the following:")
        print("1. Login")
        print("2. Create a new account")
        print("0. Exit")
        choice = input().strip()
        match choice:
            case "1":
                keep_going, username = user_login()
                if keep_going == False:
                    return username


            case "2":
                keep_going, username = create_login()
                if keep_going == False:
                    return username

            case "0":
                print("Exiting")
                quit()

            case _:
                print("Invalid choice")
                keep_going == True

# Creating a dev login option
def dev_mode():
    """Developer mode menu for auto-login testing without normal authentication.

        Returns:
            str: Username of the auto-logged-in user.


        Raises:
            SystemExit: When user selects exit option.
        """
    keep_going = True
    while keep_going:
        print("Welcome Dev ^_^ hope you have fun")
        print("Please choose form one of the following:")
        print("1. auto login for testing, with json")
        print("2. auto login for testing, without json")
        print("3. auto login (admin) for testing, without/with json")
        print("0. Exit")
        choice = input().strip()

        match choice:
            case "1":
                username = "anna_writer".strip()
                logged_in_usernmae = username
                keep_going = False
                return logged_in_usernmae

            case "2":
                username = "NoahClarke123".strip()
                logged_in_usernmae = username
                keep_going = False
                return logged_in_usernmae

            case "3":
                username = "admin".strip()
                logged_in_usernmae = username
                keep_going = False
                return logged_in_usernmae

            case "0":
                print("Exiting...")
                quit()

            case _:
                print("Invalid choice")


def normal_view(logged_in_usernmae):
    """Handles when the person loging in is not admin
    args:
        str: the logged-in usernmae


    """
    user_run = True
    while user_run:
        print(f"Welcome {logged_in_usernmae}, please choose one of the following:")
        print("1. View all Videos")
        print("2. Search for specific video")
        print("3. Show all videos in specific genre")
        print("4. View all PlayRecords by a user")
        print("5. Play a specific Video for a specified User")
        print("6. View all PlayRecords by a video")
        print("0. Exit")
        choice = input(f"Choice: ").strip()
        # Section 1(for any user logged in)
        match choice:
            case "1":
                print_videos()

            case "2":
                video_search()

            case "3":
                search_genre()

            case "4":
                show_user_history(video_service.get_usable_video_data())

            case "5":
                play_video_user(user_service, video_service)

            case "6":
                view_video_play(user_service, video_service)

            case "0":
                user_run = False
                print("Exiting...")
                quit()

            case _:
                print("Invalid choice. Please choose a valid choice.")

#keep here
def admin_view(logged_in_usernmae):
    """ handles the logic then the username logged in is admin

    args:
        str: the logged-in usernmae
    """
    admin_run = True
    while admin_run:
        print(f"Welcome {logged_in_usernmae}")
        print("1. Add a new Video to the system")
        print("2. Remove a Video from the system")
        print("3. Edit a video")
        print("0. Exit")
        choice = input(f"Choice: ").strip()
        match choice:
            case "1":
                new_video()

            case "2":
                video_remover()

            case "3":
                video_editor()

            case "0":
                admin_run = False
                print("Exiting...")
                quit()

            case _:
                logger.info("admin functions: Invalid choice by user.")
                print("Invalid choice. Please choose a valid choice.")

if __name__ == "__main__":

    valid = False
    video_service = None
    while not valid:
        video_service = load_video_model()
        if video_service is not None:
            valid = True


    # Users
    valid = False
    user_service = None
    while not valid:
        user_service = load_user_model()
        if user_service is not None:
            valid = True



    logged_in_usernmae = None
    print("what would you like to go into?")
    print("1. Normal Login")
    print("2. Super secret dev mode?")
    choice = input().strip()

    match choice:
        case "1":
            logged_in_usernmae = normal_login()

        case "2":
            logged_in_usernmae = dev_mode()

        case _:
            print("Invalid choice. Please choose a valid choice.")


    admin = user_service.admin_check_srv(logged_in_usernmae)

    if admin != True:
        normal_view(logged_in_usernmae)


    if admin == True:
        admin_view(logged_in_usernmae)


