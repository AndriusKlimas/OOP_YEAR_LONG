#imports annotations for type hinting
from __future__ import annotations

import json

from catalogue import Video
from user_records import User

#Option 1 def
def print_videos(videos_dictionary: dict) -> None:
    """ prints all videos in the dictionary
    args:
        videos_dictionary (dict): a dictionary of videos with key is title and value is Video object

    """
    #Loops through dictionary and prints all videos
    try:
        for title, video_list in videos_dictionary.items():
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
    #checking if the username is in the dicktionary
    if username in users_dict:
        #gets the play history fromthe users dickt
        user_records = users_dict[username].get_history()
        print(f"Here is the play history for {username}: ")

        #loops through the info getten
        for vid_id in user_records:
            play_records_list = user_records[vid_id]

            # Find the video by ID in the dictionary
            video = None
            for title, video_list in videos_dict.items():
                for v in video_list:
                    if v.get_video_id() == vid_id:
                        video = v
                        break
                if video:
                    break

            #checking if the video found in the dictionary
            if video:
                title = video.get_title()
                for r in play_records_list:
                    print(f"{title} starting at {sec_to_min(r.get_pos())})")
            else:
                print(f"Video with ID {vid_id} not found")
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
        videos_dictionary (dict): a dictionary of videos with key is title and value is Video object


    """
    #getting basic info
    genres_list = []
    print("Please enter the following details to add a new video:")
    #video id no longer key, now goes through dict, counts, and then adds 1 onto for new video id
    get_video_id = 0
    for video_list in videos_dictionary.values():
        for video in video_list:
            get_video_id += 1
    get_video_id += 1
    get_title = input("Title: ")
    get_description = input("Description: ")
    get_duration = int(input("Duration seconds: "))
    get_release_year = int(input("Release Year: "))
    #loop for genre
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
    #creating a new video class object
    new_video = Video(get_video_id, get_title, get_description, get_duration, get_release_year, genres_list)
    #'checking if he video is in the dictionary'
    if get_title in videos_dictionary.keys():
        #'if it is then add the class object under hte same key'
        videos_dictionary[get_title].append(new_video)
        #'if not then add the class object under a new key'
    else:
        videos_dictionary[get_title] = [new_video]

    print("Video added to list")

    #added sleep for the

#Option 7 def
def video_remover(videos_dictionary: dict, remove_video: str) -> bool:
    """ Removes a video from the dictionary
    args:
        videos_dictionary (dict): a dictionary of videos with key is Video ID and value is Video object
        remove_video: (str): the title of the video to remove

    return:
        bool: returns True if video is removed, else False
    """
    #ps need comments for this as its complex
    try:
        #stripping white spaces again, causes issues if not their
        search_video = remove_video.strip().lower()
        #to store the videos found
        videos_found = []
        #this will be used to store the title/key iof found
        title_key = None

        #finding all videos
        for title, video_list in videos_dictionary.items():
            if search_video == title.strip().lower():
                title_key = title
                if isinstance(video_list, list):
                    videos_found = video_list
                else:
                    videos_found = [video_list]
                break

        #if the videos_found list is empty, then do the below
        if not videos_found:
            print(f"No videos found with title provided: {remove_video}")
            return False

        #in this part will check how many iteams are added to teh list
        if len(videos_found) > 1:
            for num, video in enumerate(videos_found,1):
                print(f"{num}. Name= {Video.get_title(video)}, description = {Video.get_description(video)}, duration = {Video.get_duration_seconds(video)}, release_year = {Video.get_release_year(video)}")

            choice = int(input("Please enter the one you would like to remove(numbers only): "))
            try:
                actual_remove = choice - 1
                videos_found.pop(actual_remove)
            except IndexError:
                print("out of range")
            except ValueError:
                print("please enter a number")

        #if one video is found
        else:
            print(f"removing video: {videos_found}")
            videos_found.pop(0)

        #checking if ther list is not empty, if it is then remove the key for dictioanry
        if not videos_found:
            del videos_dictionary[title_key]

        return True
    except Exception as e:
        print(f"An error occurred while removing video: {e}")
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

# #for pre-populating the dictionary, needed as cant add 2 manually to the same key
# def add_video_to_dict(videos_dict, video):
#     title = video.get_title()
#     if title in videos_dict:
#         videos_dict[title].append(video)
#     else:
#         videos_dict[title] = [video]


def parse_videos(filename: str) -> list:
    """Parses a file of video information into a list of Video objects.

    Args:
        filename(str): the name of the file

    Returns:
        Invalid records are logged and skipped; the function returns a list of successfully
        created Video objects.
    """
    #opens the file inputed
    with open(filename) as file:
        videos_dictionary = json.load(file)

    new_videos = {}

    #going through each title and the indiviual info
    for title, videos_list in videos_dictionary.items():
        #creting an empty list with teh title as
        new_videos[title] = []

        #Goes throgh each video dictionary in the list for the title
        for i,video_dict in enumerate(videos_list, start=1):
            try:
                #makes the class object using the from_dict in the video class
                video = Video.from_dict(video_dict)
                #if make then it will add it to the list for that title and add it to dictionary
                new_videos[title].append(video)
            except Exception as e:
                #if error then it will tell the user what line hte issue is on
                print(f"Invalid video record #{i} under title '{title}' in {filename}: {e}")

    #returns the dictionary with the successful info
    return new_videos



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


def create_default_videos() -> dict:
    """Create and return the default videos dictionary used when no file is provided.

    Returns:
        A dictionary that maps video id to video title.
       """

    vids = {}
    v1 = Video(1, "Inception", "A mind-bending thriller", 8880, 2010, ["scifi", "thriller"])
    v2 = Video(2, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
    v3 = Video(3, "The Godfather", "Crime family saga", 10500, 1972, ["drama", "crime"])
    v4 = Video(4, "Toy Story", "Toys come to life", 4860, 1995, ["animation", "comedy"])
    v5 = Video(5, "Up", "Balloon building", 16732, 2008, ["animation", "drama"])
    #Do NOT TOUCH THIS AS I NEED IT FOR MULTIPLE VIDEOS UNDER HTE SAME TITLE
    v6 = Video(6, "Up", "Something else", 23143, 2008, ["animation", "comedy"])

    for v in (v1, v2, v3, v4, v5, v6):
        title = v.get_title()
        if title in vids:
            vids[title].append(v)
        else:
            vids[title] = [v]

    return vids

def create_default_users() -> dict:
    """Create and return the default users dictionary used when no file is provided.

    Returns:
        A dictionary that maps username to user object.
       """
    us = {}
    u1 = User("NoahClarke123", "Password123!")
    u2 = User("Film_Critic1", "ILoveMovies0000")
    u3 = User("Bob_iscool", "iamBob05$")
    u4 = User("Jedibob212", "Sidius66")
    u5 = User("IronManFan3", "TonyStark44!")

    for u in (u1, u2, u3, u4, u5):
        us[u.get_username()] = u
    return us


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

    # Videos
    video_filename = input(
        "Please enter a filename (json) where video information is stored or press Enter to use defaults: ").strip()
    vdata = data_setup("videos", video_filename)
    if vdata is None:
        videos = create_default_videos()
    else:
        # vdata is a list of Video objects
        videos = vdata


    # Users
    user_filename = input(
        "Please enter a filename where user information is stored or press Enter to use defaults: ").strip()
    udata = data_setup("users", user_filename)
    if udata is None:
        users = create_default_users()
    else:
        users = {u.get_username(): u for u in udata}

    keep_going = True
    while keep_going:
        print("Please choose form one of the following:")
        print("1. Login")
        print("2. Create a new account")
        print("0. Exit")
        choice = input().strip()

        if choice == "1":
            print("Enter username:")
            username = input().strip()
            print("Enter password:")
            password = input().strip()

            user = User.validate_login(users, username, password)
            if user is not None:
                users[username] = user
                keep_going = False
            else:
                print("Invalid username or password")


        if choice == "2":
            print("in development")
            #in development


        if choice == "0":
            quit()





    print("1. View all Videos")
    print("2. Search for specific video")
    print("3. Show all videos in specific genre")
    print("4. View all PlayRecords by a user")
    print("5. Play a specific Video for a specified User")
    print("6. Add a new Video to the system")
    print("7. Remove a Video from the system")
    print("0. Exit Application")

    choice = input("Enter your choice (1-7) or 0 to exit: ")


    #Section 1(for any user logged in)
    match choice:
        case "1":
            print_videos(videos)
        case "2":
            search_video = input("Please enter the Video title you are looking for: ")
            video_info = video_search(videos, search_video)
            if video_info is not None:
                # isinstance is used to check if the iteam retuernd is a list, if it is then do the below source
                # w3schools, stackoverflow
                if isinstance(video_info, list):
                    for video in video_info:
                        print(video)
                else:
                    print(video_info)
            else:
                print("Video not found.")

        case "3":
            # getting user to input the genre they are searching for
            search_video_genre = input("Please enter the genre you would like to look for: ")
            in_valid_genres = Video.validate_genre(search_video_genre)
            if in_valid_genres == True:
                search_genre(videos, search_video_genre)
            else:
                print("Genre not valid.")
            # calling the method to search the genre



        #Section 2 (For that specific user only)
        case "4":
            show_user_history(users, videos)

        case "5":
            play_video_user(users, videos)




        #Section 3(for admin only)
        case "6":
            new_video(videos)

        case "7":

            remove_video = input("Please enter the name of the video you would like to remove: ")
            # calling the method to remove the video
            video_removed = video_remover(videos, remove_video)
            # if the video method comes back as true then print video removed
            if video_removed == True:
                print("Video removed from list")
            # else print video not found
            else:
                print("Video not found.")

        case "0":
            print("Exiting Application. Goodbye!")

        case _:
            print("Invalid choice. Please choose a valid choice.")
