#imports annotations for type hinting
from __future__ import annotations

import json

from catalogue import Video
from user_records import User, PlayRecord

#Option 1 def
def print_videos(videos_dictionary: dict) -> None:
    """ prints all videos in the dictionary
    args:
        videos_dictionary (dict): a dictionary of videos with key is Video ID and value is Video object

    """
    #Loops through dictionary and prints all videos
    try:
        # Loops through dictionary and prints all videos
        for video_list in videos_dictionary.values():
            #found below on w3schools and stackoverflow isinstance()
            if isinstance(video_list, list):
                for video in video_list:
                    print(video)
            else:
                print(video_list)

    except TypeError:
        print("Error: videos_dictionary must be a dictionary")
    except Exception as e:
        print(f"An error occurred while printing videos: {e}")

#Option 2 def
def video_search(videos_dictionary: dict, search_video: str) -> Video | None:
    """ searching for a specific video in the dictionary
    args:
        videos_dictionary (dict): a dictionary of videos with key is video title and value is Video object
        search_video: (str): the title of the video to search for

    returns:
    Video: if the video is found, return it, else return None
    """
    # for some unknown reason white spaces where appearing, causing issues when looking it up

    try:
        #stripping white spaces again, causes issues if not their
        search_video = search_video.strip().lower()
        for title, video_list in videos_dictionary.items():
            #stripping white spaces again, causes issues if not their
            if search_video == title.strip().lower():
                return video_list

        return None

    except Exception as e:
        print(f"An error occurred while searching for video: {e}")
        return None


#Option 3 def
def search_genre(videos_dictionary: dict, search_genre: str) -> None:
    """ searching for a specific genre in the dictionary
    args:
        videos_dictionary (dict): a dictionary of videos with key is video title and value is Video object
        search_genre: (str): the genre to search for

    """
    try:
        # loops through dictionary and stores the video info in video variable
        #whitespace again causing issues
        search_genre = search_genre.strip().lower()
        found = False

        for title, genre_list in videos_dictionary.items():
            for video in genre_list:
                #hets the genres from the class object using the fucntion
                video_genres = Video.get_genres(video)
                if search_genre in video_genres:
                    print(video)
                    found = True

        if not found:
            print(f"No videos found with genre: {search_genre}")

    except Exception as e:
        print(f"An error occurred while searching for genre: {e}")

#option 4 def
def show_user_history(users_dict: dict, videos_dict: dict) -> None:
    """ shows the user's play history

    Args:
        users_dict (dict): dictionary of all users
        videos_dict (dict): dictionary of all videos
    """
    username = input("Please enter the username of the user you would like to show the play history for: ")
    if username in users_dict:
        user_records = users_dict[username].get_history()
        print(f"Here is the play history for {username}: ")
        for vid_id in user_records:
            play_records_list = user_records[vid_id]
            title = videos_dict[vid_id].title
            for r in play_records_list:
                print(f"{title} starting at {sec_to_min(r.get_pos())}")

    else:
        print("Invalid username entered")

#option 5 def
def play_video_user(users_dict: dict, videos_dict: dict) -> None:
    """ creates a play record

    Args:
        users_dict (dict): dictionary of all users
        videos_dict (dict): dictionary of all videos
    """
    username = input("Please enter the username of the user you wish to use: ")
    if username in users_dict:
        video = input("Please enter the title of the video: ")
        found = False
        for t in videos_dict.values():
            if t.title.lower() == video.lower():
                users_dict[username].start_play(t.get_video_id())
                print(f"{users_dict[username].get_username()} is now playing {t.title}")
                found = True
                break

        if not found:
            print("Invalid title entered")

    else:
        print("Invalid username entered")

#Option 6 def
def new_video(videos_dictionary: dict) -> None:
    """ Adds a new video to the dictionary by creating an object of the video class
    args:
        videos_dictionary (dict): a dictionary of videos with key is Video ID and value is Video object


    """
    genres_list = []
    print("Please enter the following details to add a new video:")
    get_video_id = max(videos_dictionary.keys()) + 1
    get_title = input("Title: ")
    get_description = input("Description: ")
    get_duration = int(input("Duration seconds: "))
    get_release_year = int(input("Release Year: "))

    while True:
        get_genres = input("Please enter the genres")
        if get_genres in Video.return_valid_genres():
            genres_list.append(get_genres)
        else:
            print("Genre not valid. Please choose a valid genre")
            print(Video.return_valid_genres())
        print("Would you like to add another genre? (y/n)")
        another = input().lower()
        if another == "n":
            break
    new_video = Video(get_video_id, get_title, get_description, get_duration, get_release_year, genres_list)
    videos_dictionary[new_video.get_video_id()] = new_video
    print("Video added to list")
    print(videos[new_video.get_video_id()])

#Option 7 def
def video_remover(videos_dictionary: dict, remove_video: str) -> bool:
    """ Removes a video from the dictionary
    args:
        videos_dictionary (dict): a dictionary of videos with key is Video ID and value is Video object
        remove_video: (str): the title of the video to remove

    return:
        bool: returns True if video is removed, else False
    """
    for video in videos_dictionary.values():
        if remove_video.lower() in video.title.lower():
            del videos_dictionary[video.get_video_id()]
            return True
    return False

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

def parse_videos(filename: str) -> list:
    """Parses a file of video information into a list of Video objects.

    Args:
        filename(str): the name of the file

    Returns:
        Invalid records are logged and skipped; the function returns a list of successfully
        created Video objects.
    """
    with open(filename) as file:
        video_dicts = json.load(file)

    videos = []
    for i, video_dict in enumerate(video_dicts, start=1):
        try:
            video = Video.from_dict(video_dict)
            videos.append(video)
        except Exception as e:
            # Log invalid record and continue
            print(f"Invalid video record #{i} in {filename}: {e}")
    return videos


def parse_users(filename: str) -> list:
    """Parses a file of user information into a list of User objects.

    Args:
        filename(str): the name of the file

    Returns:
        Invalid records are logged and skipped; the function returns a list of successfully
        created User objects.
    """
    with open(filename) as file:
        users_dicts = json.load(file)

    users = []
    for i, users_dict in enumerate(users_dicts, start=1):
        try:
            user = User.from_dict(users_dict)
            users.append(user)
        except Exception as e:
            print(f"Invalid user record #{i} in {filename}: {e}")
    return users


def parse_playrecords(filename: str, users: dict | None) -> list:
    """Parses a file of playrecord information.

    Args:
        filename(str): the name of the file
        users: (dict): a dictionary of users

    Returns:
        Invalid records are logged and skipped; the function returns a list of PlayRecord objects that were created.

    If a `users` mapping is provided the function will attempt to attach play records to
    the corresponding User objects by calling User.start_play.
    """
    with open(filename) as file:
        play_dicts = json.load(file)

    playrecords = []
    for i, play_dict in enumerate(play_dicts, start=1):
        try:
            # If we have a users mapping we prefer to attach the record to that user
            if users is not None:
                username = play_dict.get("username")
                video_id = play_dict.get("video_id")
                pos = play_dict.get("position_in_seconds", 0)

                if username is None:
                    raise ValueError(f"Unknown username '{username}'")
                if video_id is None:
                    raise ValueError(f"Unknown video_id '{video_id}'")

                # Use start_play to create and register the play record.
                success = users[username].start_play(video_id, pos)
                if not success:
                    raise ValueError(f"Failed to create play record for user '{username}' and video '{video_id}'")

                # Retrieve the most recent play record for this user/video
                pr_list = users[username].get_plays(video_id)
                if pr_list:
                    playrecords.append(pr_list[-1])
            else:
                # No users mapping available: try to use PlayRecord.from_dict (may raise)
                pr = PlayRecord.from_dict(play_dict)
                playrecords.append(pr)
        except Exception as e:
            print(f"Invalid playrecord #{i} in {filename}: {e}")
    return playrecords


users: dict = {}
videos: dict = {}

video1 = Video(1, "Inception", "A mind-bending thriller", 8880, 2010, ["scifi", "thriller"])
video2 = Video(2, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
video3 = Video(3, "The Godfather", "Crime family saga", 10500, 1972, ["drama", "crime"])
video4 = Video(4, "Toy Story", "Toys come to life", 4860, 1995, ["animation", "comedy"])
video5 = Video(5, "UP", "Ballon building", 16732, 2008, ["animation", "drama"])

videos[video1.get_video_id()] = video1
videos[video2.get_video_id()] = video2
videos[video3.get_video_id()] = video3
videos[video4.get_video_id()] = video4
videos[video5.get_video_id()] = video5

user1 = User("NoahClarke123", "Password123!")
user2 = User("Film_Critic1", "ILoveMovies0000")
user3 = User("Bob_iscool", "iamBob05$")
user4 = User("Jedibob212", "Sidius66")
user5 = User("IronManFan3", "TonyStark44!")

users[user1.get_username()] = user1
users[user2.get_username()] = user2
users[user3.get_username()] = user3
users[user4.get_username()] = user4
users[user5.get_username()] = user5


def create_default_playrecords():
    """Create the hardcoded play records used by the example data.

    This simply calls start_play on the example users and videos. Keeping this
    in a function makes it easy to reuse or skip later if the program loads
    playrecords from files.
    """
    record1 = user1.start_play(video1.get_video_id(), 500)
    record2 = user1.start_play(video3.get_video_id())
    record3 = user2.start_play(video2.get_video_id(), 1000)
    record4 = user2.start_play(video5.get_video_id())
    record5 = user3.start_play(video3.get_video_id(), 2500)
    record6 = user3.start_play(video1.get_video_id())
    record7 = user1.start_play(video2.get_video_id(), 600)
    record8 = user4.start_play(video4.get_video_id())
    record9 = user5.start_play(video5.get_video_id(), 60)
    record10 = user2.start_play(video1.get_video_id(), 4000)
    return [record1, record2, record3, record4, record5, record6, record7, record8, record9, record10]

# create defaults immediately (keeps original behaviour)
create_default_playrecords()

def data_setup(parse_type: str, filename: str | None = None):
    """Prompt the user (up to 3 tries) for a filename and parse the file.

    Args:
        parse_type (str): one of "videos", "users" or "playrecords".
        filename (str | None): optional initial filename to try first (if provided
                                the function will attempt it, otherwise it will
                                prompt the user).

    Returns:
        list: list of parsed objects on success, or None to indicate the caller
              should use the hardcoded defaults.
    """
    attempts = 3
    for attempt in range(attempts):
        # If caller provided a filename, try it first on the first attempt.
        if attempt == 0 and filename:
            fname = filename.strip()
        else:
            fname = input(f"Enter {parse_type} filename (JSON) or press Enter to use defaults: ").strip()

        if not fname:
            # User chose defaults or pressed Enter
            return None

        try:
            if parse_type == "videos":
                items = parse_videos(fname)
            elif parse_type == "users":
                items = parse_users(fname)
            elif parse_type == "playrecords":
                # parse_playrecords uses the current `users` mapping to attach records
                items = parse_playrecords(fname, users)
            else:
                print("Unknown data type requested; using defaults.")
                return None

            print(f"Loaded {len(items)} {parse_type} from {fname}")
            return items
        except FileNotFoundError:
            print(f"File not found: {fname}. Attempts left: {attempts - attempt - 1}")
        except Exception as e:
            print(f"Error loading {parse_type} from {fname}: {e}. Attempts left: {attempts - attempt - 1}")

    print(f"Failed to load {parse_type} after {attempts} attempts; using defaults.")
    return None

if __name__ == "__main__":

    video_filename = input("Please enter a filename where video information is stored or press Enter to use defaults: ").strip()
    vdata = data_setup("videos", video_filename)
    user_filename = input("Please enter a filename where user information is stored or press Enter to use defaults: ").strip()
    udata = data_setup("users", user_filename)
    pr_filename = input("Please enter a filename where Play Record information is stored or press Enter to use defaults: ").strip()
    prdata = data_setup("playrecords", pr_filename)



    print("1. View all Videos")
    print("2. Search for specific video")
    print("3. Show all videos in specific genre")
    print("4. View all PlayRecords by a user")
    print("5. Play a specific Video for a specified User")
    print("6. Add a new Video to the system")
    print("7. Remove a Video from the system")
    print("0. Exit Application")

    choice = input("Enter your choice (1-7) or 0 to exit: ")

    match choice:
        case "1":
            print_videos(videos)
        case "2":
            search_video = input("Please enter the Video title you are looking for: ")
            video_info = video_search(videos, search_video)
            #If it variable video_info is not none then show the info
            if video_info is not None:
                print(video_info)
            else:
                print("Video not found.")

        case "3":
            search_video_genre = input("Please enter the genre you would like to look for: ")
            search_genre(videos, search_video_genre)

        case "4":
            show_user_history(users, videos)

        case "5":
            play_video_user(users, videos)

        case "6":
            new_video(videos)

        case "7":
            #Need to work on as multiple videos may have same name
            remove_video = input("Please enter the name of the video you would like to remove: ")
            video_removed = video_remover(videos, remove_video)
            if video_removed == True:
                print("Video removed from list")

            else:
                print("Video not found.")

        case "0":
            print("Exiting Application. Goodbye!")

        case _:
            print("Invalid choice. Please choose a valid choice.")
