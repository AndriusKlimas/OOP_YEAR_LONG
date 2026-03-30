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
    for video in videos_dictionary.values():
        print(video)

#Option 2 def
def video_search(videos_dictionary, search_video) -> Video | None:
    """ searching for a specific video in the dictionary
    args:
        videos_dictionary (dict): a dictionary of videos with key is Video ID and value is Video object
        search_video: (str): the title of the video to search for

    returns:
    Video: if the video is found, return it, else return None
    """
    for video in videos_dictionary.keys():
        if search_video in video:
            return video
        else:
            return None
    #loops through dictionary and stores the video info in video variable
    # for video in videos_dictionary.values():
    #     #if the search_video is found in video.title then return the video found
    #     if search_video.lower() in video.title.lower():
    #         return video


#Option 3 def
def search_genre(videos_dictionary, search_genre) -> None:
    """ searching for a specific genre in the dictionary
    args:
        videos_dictionary (dict): a dictionary of videos with key is Video ID and value is Video object
        search_genre: (str): the genre to search for

    """
    #loops through dictionary and stores the video info in video variable
    for video in videos_dictionary.values():
        #using the method check_genre from video class to check if the genre is in the video
        if video.check_genre(search_genre):
            #print out the video if the genre is found
            print(video)

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
    #loops through dictionary and stores the video info in video variable
    for video in videos_dictionary.values():
        #If the remove_video is found in the dictionary via title
        if remove_video.lower() in video.title.lower():
            #then delete that video from the dictionary
            del videos_dictionary[video.get_video_id()]
            #Return True
            return True
    #else return false so it will not crash
    return False

#Option 6 def
def new_video(videos_dictionary) -> None:
    """ Adds a new video to the dictionary by creating an object of the video class
    args:
        videos_dictionary (dict): a dictionary of videos with key is title and value is Video object


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
    #'checking if he video is in the dictionary'
    if get_title in videos_dictionary.keys:
        #'if it is then add the class object under hte same key'
        videos_dictionary[get_title].append(new_video)
        #'if not then add the class object under a new key'
    else:
        videos_dictionary[get_title] = new_video

    print("Video added to list")

    #added sleep for the fun of it
    time.sleep(3)

    print(videos[new_video.get_title()])

    # # creating a genere list for the new video
    # genres_list = []
    # # print to tell user to input info
    # print("Please enter the following details to add a new video:")
    # # set the video ID to the highest number in the list and then add 1 to it and sent it to that e.g. 5 is highest then it adds 1 and makes it a video id of 6
    # get_video_id = max(videos_dictionary.keys()) + 1
    # # asking for the title
    # get_title = input("Title: ")
    # # askign for description
    # get_description = input("Description: ")
    # # asking for duration
    # get_duration = int(input("Duration seconds: "))
    # # asking for release year
    # get_release_year = int(input("Release Year: "))
    # # loop to get genres
    # while True:
    #     # asking for genre
    #     get_genres = input("Please enter the genres")
    #     # cheking if genre is valid by using the return valid method from the class
    #     if get_genres in Video.return_valid_genres():
    #         # If it is then add it to teh list
    #         genres_list.append(get_genres)
    #     # If not
    #     else:
    #         # tell the user the genre is not allowed
    #         print("Genre not valid. Please choose a valid genre")
    #         # printing out all the valid genres
    #         print(Video.return_valid_genres())
    #     # asking if they want to add another genre
    #     print("Would you like to add another genre? (y/n)")
    #     # getting the user input
    #     another = input().lower()
    #     # if they aswear no then break the loop
    #     if another == "n":
    #         break
    # # creating the new video object with the gathered info
    # new_video = Video(get_video_id, get_title, get_description, get_duration, get_release_year, genres_list)
    # # adding the new video to the videos dictionary
    # videos_dictionary[new_video.get_video_id()] = new_video
    # # print saying it has been added
    # print("Video added to list")
    # # print out the video info added
    # print(videos[new_video.get_video_id()])


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

#Mnayally adding videos to the dictionary
videos[video1.get_video_id()] = video1
videos[video2.get_video_id()] = video2
videos[video3.get_video_id()] = video3
videos[video4.get_video_id()] = video4
videos[video5.get_video_id()] = video5

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
        #Getting the user to input the video they are searching for
        search_video = input("Please enter the Video title you are looking for: ")
        #calling the method to search the video
        video_info = video_search(videos, search_video)
        #If it variable video_info is not none then show the info
        if video_info is not None:
            print(video_info)
        #else show video is not found as it means video was not found
        else:
            print("Video not found.")

    #If 3 is entered
    case "3":
        #getting user to input the genre they are searching for
        search_video_genre = input("Please enter the genre you would like to look for: ")
        #calling the method to search the genre
        search_genre(videos, search_video_genre)


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
