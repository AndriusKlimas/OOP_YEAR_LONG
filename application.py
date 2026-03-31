#imports annotations for type hinting
from __future__ import annotations
import time
#Option 1 def
def print_videos(videos_dictionary) -> None:
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
def video_search(videos_dictionary, search_video) -> Video | None:
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
def search_genre(videos_dictionary, search_genre) -> None:
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
def show_user_history(users_dict: dict, videos_dict: dict):
    """ shows the user's play history

    Args:
        users_dict (dict): dictionary of all users
        videos_dict (dict): dictionary of all videos
    """
    #asks the user to enter the username they want to see the play history of
    username = input("Please enter the username of the user you would like to show the play history for: ")
    #if the username they entered is in the users list
    if username in users_dict:
        #sets up a variable to store the history for that user
        user_records = users_dict[username].get_history()
        #prints a statement ot let the user know the history
        print(f"Here is the play history for {username}: ")
        #for loop to search through all the play records for that user
        for r in user_records.values():
            #creates a variable to store the video id for that record
            vid_id = r.get_video_id()
            #creates a variable to store the title of the video with that video id
            title = videos_dict[vid_id].title
            #prints the title of the play record and the time in minutes and seconds of the position
            print(f"{title} starting at {sec_to_min(r.get_pos())}")

    #if the username isnt in the dictionary
    else:
        #letds the user know their username is invalid
        print("Invalid username entered")

#option 5 def
def play_video_user(users_dict: dict, videos_dict: dict):
    """ creates a play record

    Args:
        users_dict (dict): dictionary of all users
        videos_dict (dict): dictionary of all videos
    """
    # asks the user to enter the username they wish to play a video from
    username = input("Please enter the username of the user you wish to use: ")
    # if the username entered is found within the users dictionary
    if username in users_dict:
        # it asks the user to enter the title of the video they wish to watch
        video = input("Please enter the title of the video: ")
        # creates a variable for when the program finds the movie they entered
        found = False
        # for loop to search through all the movie titles in the videos dictionary
        for t in videos_dict.values():
            # if the title in the dictionary is the same as the title the user entered
            if t.title.lower() == video.lower():
                # uses the start_play function to create a play record for the specified user in the dictionary with the video_id of the specified video
                users_dict[username].start_play(t.get_video_id())
                #lets the user know that the user is now playing the movie they requested
                print(f"{users_dict[username].get_username()} is now playing {t.title}")
                # changes the found variable to true
                found = True
                # breaks from the loop
                break
        # if the title they entered was not found in the list
        if not found:
            # lets the user know they entered an invalid title
            print("Invalid title entered")
    # if the username they entered wasnt found in the user dictionary
    else:
        # lets the user know they entered an invalid username
        print("Invalid username entered")

#Option 7 def
def video_remover(videos_dictionary, remove_video) -> bool:
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
                print(f"{num}. {video}")

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





#Option 6 def
def new_video(videos_dictionary) -> None:
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

    #added sleep for the fun of it
    time.sleep(3)



    #for testing to see if added correctly
    # print(f"{videos.keys()}")
    # for key, value in videos.items():
    #     print(f"  Key: {key}, Value type: {type(value)}, Value: {value}")


#for pre-populating the dictionary, needed as cant add 2 manually to the same key
def add_video_to_dict(videos_dict, video):
    title = video.get_title()
    if title in videos_dict:
        videos_dict[title].append(video)
    else:
        videos_dict[title] = [video]

#imports Video class from catalogue.py
from catalogue import Video
#imports User class and PlayRecords class from user_records.py
from user_records import User, PlayRecord
# from user_records import User

#creates two blank dictionaries for the users and the videos
users: dict = {}
videos: dict = {}

#setting up video classes and storing them in variables
video1 = Video(1, "Inception", "A mind-bending thriller", 8880, 2010, ["scifi", "thriller"])
video2 = Video(2, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
video3 = Video(3, "The Godfather", "Crime family saga", 10500, 1972, ["drama", "crime"])
video4 = Video(4, "Toy Story", "Toys come to life", 4860, 1995, ["animation", "comedy"])
video5 = Video(5, "UP", "Ballon building", 16732, 2008, ["animation", "drama"])
video6 = Video(6, "UP", "ballon finding", 1435, 2018, ["comedy", "drama"])

#Mnayally adding videos to the dictionary, round about way of populating the dictionary when same name
add_video_to_dict(videos, video1)
add_video_to_dict(videos, video2)
add_video_to_dict(videos, video3)
add_video_to_dict(videos, video4)
add_video_to_dict(videos, video5)
add_video_to_dict(videos, video6)



# users = User
user1 = User("NoahClarke123", "Password123!")
user2 = User("Film_Critic1", "ILoveMovies0000")
user3 = User("Bob_iscool", "iamBob05$")
user4 = User("Jedibob212", "Sidius66")
user5 = User("IronManFan3", "TonyStark44!")

#Manually adding users to the dictionary
users[user1.get_username()] = user1
users[user2.get_username()] = user2
users[user3.get_username()] = user3
users[user4.get_username()] = user4
users[user5.get_username()] = user5

#Manually creates 10 play records using the user data and video data
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



def sec_to_min(seconds):
    """Convert seconds to a human-readable minutes and seconds string.

        Args:
            seconds (int): Number of seconds

        Returns:
            str: Formatted string in the form "N minutes and M seconds".
        """
    #creates a minute variable which is equal to the nearest whole minute
    minutes = seconds // 60
    #creates a second variable which takes the remainder of the floored minute
    secs = seconds % 60
    #returns the minutes and seconds of the video position
    return f"{minutes} minutes and {secs} seconds"

#Shows a menu to the user with different option on our video playing application
print("Welcome, please choose on of the below Options:")
print("1. View all Videos")
print("2. Search for specific video")
print("3. Show all videos in specific genre")
print("4. View all PlayRecords by a user")
print("5. Play a specific Video for a specified User")
print("6. Add a new Video to the system")
print("7. Remove a Video from the system")
print("0. Exit Application")

#getting users input
choice = input("Enter your choice (1-7) or 0 to exit: ")

#Setting up match case for user input
match choice:
    #If 1 is entered
    case "1":
        #Calling the method to print all videos
        print_videos(videos)
    #If 2 is entered(stack overflow helped with searching this)
    case "2":
            search_video = input("Please enter the Video title you are looking for: ")
            video_info = video_search(videos, search_video)
            if video_info is not None:
                #isinstance is used to check if the iteam retuernd is a list, if it is then do the below source
                # w3schools, stackoverflow
                if isinstance(video_info, list):
                    for video in video_info:
                        print(video)
                else:
                    print(video_info)
            else:
                print("Video not found.")


    #If 3 is entered
    case "3":
        #getting user to input the genre they are searching for
        search_video_genre = input("Please enter the genre you would like to look for: ")
        in_valid_genres = Video.validate_genre(search_video_genre)
        if in_valid_genres == True:
            search_genre(videos, search_video_genre)
        else:
            print("Genre not valid.")
        #calling the method to search the genre




    #of 4 is entered
    case "4":
        show_user_history(users, videos)

    #If 5 is entered
    case "5":
        play_video_user(users, videos)

    #If 6 is entered
    case "6":
        #Calling the method to add a new video
        new_video(videos)



    #If 7 is entered
    case "7":
        #Need to work on as multiple videos may have same name
        remove_video = input("Please enter the name of the video you would like to remove: ")
        #calling the method to remove the video
        video_removed = video_remover(videos, remove_video)
        #if the video method comes back as true then print video removed
        if video_removed == True:
            print("Video removed from list")
        #else print video not found
        else:
            print("Video not found.")


    #If 0 is entered
    case "0":
        print("Exiting Application. Goodbye!")
    #if anything else is entered
    case _:
        print("Invalid choice. Please choose a valid choice.")

    #added to dev_main
