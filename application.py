#Option 1 def
def print_videos(videos_dictionary):
    #Loops through dictionary and prints all videos
    for video in videos_dictionary.values():
        print(video)

#Option 2 def
def video_search(videos_dictionary, search_video):
    #loops through dictionary and stores the video info in video variable
    for video in videos_dictionary.values():
        #if the search_video is found in video.title then return the video found
        if search_video.lower() in video.title.lower():
            return video
    #Else return none so it will not crash
    return None

#Option 3 def
def search_genre(videos_dictionary, search_genre):
    #loops through dictionary and stores the video info in video variable
    for video in videos_dictionary.values():
        #using the method check_genre from video class to check if the genre is in the video
        if video.check_genre(search_genre):
            #print out the video if the genre is found
            print(video)
    #else return none so it will not crash
    return None

#option 4 def
def show_user_history(users_dict: dict, videos_dict: dict):
    username = input("Please enter the username of the user you would like to show the play history for: ")
    if username in users:
        user_records = users_dict[username].get_history()
    else:
        user_records = {}
    if not user_records:
        print("Invalid username entered")
    else:
        print(f"Here is the play history for {username}")
        for r in user_records.values():
            vid_id = r.get_video_id()
            title = videos_dict[vid_id].title
            print(f"{title} starting at {sec_to_min(r.get_pos())}")

#option 5 def
def play_video_user(user_dict: dict, videos_dict: dict):
    # asks the user to enter the username they wish to play a video from
    username = input("Please enter the username of the user you wish to use: ")
    # if the username entered is found within the users dictionary
    if username in user_dict:
        # it asks the user to enter the title of the video they wish to watch
        video = input("Please enter the title of the video: ")
        # creates a variable for when the program finds the movie they entered
        found = False
        # for loop to search through all the movie titles in the videos dictionary
        for t in videos_dict.values():
            # if the title in the dictionary is the same as the title the user entered
            if t.title.lower() == video.lower():
                # uses the start_play function to create a play record for the specified user in the dictionary with the video_id of the specified video
                user_dict[username].start_play(t._video_id)
                #updates the play_records list to include the new play record
                play_records: dict = User.get_play_history()
                'lets the user know that the user is now playing the movie they requested'
                print(f"{user_dict[username].get_username()} is now playing {t.title}")
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
def video_remover(videos_dictionary, remove_video):
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
def new_video(videos_dictionary):
    # creating a genere list for the new video
    genres_list = []
    # print to tell user to input info
    print("Please enter the following details to add a new video:")
    # set the video ID to the highest number in the list and then add 1 to it and sent it to that e.g. 5 is highest then it adds 1 and makes it a video id of 6
    get_video_id = max(videos_dictionary.keys()) + 1
    # asking for the title
    get_title = input("Title: ")
    # askign for description
    get_description = input("Description: ")
    # asking for duration
    get_duration = int(input("Duration seconds: "))
    # asking for release year
    get_release_year = int(input("Release Year: "))
    # loop to get genres
    while True:
        # asking for genre
        get_genres = input("Please enter the genres")
        # cheking if genre is valid by using the return valid method from the class
        if get_genres in Video.return_valid_genres():
            # If it is then add it to teh list
            genres_list.append(get_genres)
        # If not
        else:
            # tell the user the genre is not allowed
            print("Genre not valid. Please choose a valid genre")
            # printing out all the valid genres
            print(Video.return_valid_genres())
        # asking if they want to add another genre
        print("Would you like to add another genre? (y/n)")
        # getting the user input
        another = input().lower()
        # if they aswear no then break the loop
        if another == "n":
            break
    # creating the new video object with the gathered info
    new_video = Video(get_video_id, get_title, get_description, get_duration, get_release_year, genres_list)
    # adding the new video to the videos dictionary
    videos_dictionary[new_video.get_video_id()] = new_video
    # print saying it has been added
    print("Video added to list")
    # print out the video info added
    print(videos[new_video.get_video_id()])
    return videos_dictionary


from catalogue import Video
from user_records import User, PlayRecord
# from user_records import User

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

record1 = User.start_play(user1, video1.get_video_id(), 500)
record2 = User.start_play(user1, video3.get_video_id())
record3 = User.start_play(user2, video2.get_video_id(), 1000)
record4 = User.start_play(user2, video5.get_video_id())
record5 = User.start_play(user3, video3.get_video_id(), 2500)
record6 = User.start_play(user3, video1.get_video_id())
record7 = User.start_play(user1, video2.get_video_id(), 600)
record8 = User.start_play(user4, video4.get_video_id())
record9 = User.start_play(user5, video5.get_video_id(), 60)
record10 = User.start_play(user2, video1.get_video_id(), 4000)

#updates the play_record dictionary with the play_history dictionary stored in User class
play_records: dict = User.get_play_history()

def sec_to_min(seconds):
    """Convert seconds to a human-readable minutes and seconds string.

        Args:
            seconds (int): Number of seconds (must be >= 0).

        Returns:
            str: Formatted string in the form "N minutes and M seconds".

        Raises:
            ValueError: If *seconds* is negative.
        """

    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes} minutes and {secs} seconds"

print("Welcome, please choose on of the below Options:")
print("1. View all Videos")
print("2. Search for specific video")
print("3. Show all videos in specific genre")
print("4. View all PlayRecords by a user")
print("5. Play a specific Video for a specified User")
print("6. Add a new Video to the system")
print("7. Remove a Video from the system")
print("0. Exit Application")


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
        # #Setting a variable to sore the name of the movie
        # search_video = input("Please enter the Video title you are looking for: ")
        # #going through dictionary looking through the values stored in each key for the one seached for
        # for video in videos.values():
        #     #If the search gets a ping back then it will move on, all lower case as user may spell it with caps or without
        #     if search_video.lower() in video.title.lower():
        #         #Printing that specific video with all the info needed
        #         print(video)
        #         #Will break out of the function if its found
        #         break
        # #f not found/broken out of then it will print the below
        # else:
        #     print("Video not found.")

    #If 3 is entered
    case "3":
        #getting user to input the genre they are searching for
        search_video_genre = input("Please enter the genre you would like to look for: ")
        #calling the method to search the genre
        search_genre(videos, search_video_genre)

        # going through dictionary looking through the values stored in each key for the one searched for
        # for video in videos.values():
        #     #calling the method check_genre from class to check the genre is their
        #     if video.check_genre(search_genre):
        #         #If it is their then print the info for the video that had the genre in it
        #         print(video)

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
        #creating a genere list for the new video
        # genres_list = []
        # #Print to tell user to input info
        # print("Please enter the following details to add a new video:")
        # #set the video ID to the highest number in the list and then add 1 to it and sent it to that e.g. 5 is highest then it adds 1 and makes it a video id of 6
        # get_video_id = max(videos.keys()) + 1
        # #Asking for the title
        # get_title = input("Title: ")
        # #Askign for description
        # get_description = input("Description: ")
        # # Asking for duration
        # get_duration = int(input("Duration seconds: "))
        # # Asking for release year
        # get_release_year = int(input("Release Year: "))
        # #Loop to get genres
        # while True:
        #     #Asking for genre
        #     get_genres = input("Please enter the genres")
        #     #Cheking if genre is valid by using the return valid method from the class
        #     if get_genres in Video.return_valid_genres():
        #         #If it is then add it to teh list
        #         genres_list.append(get_genres)
        #     #If not
        #     else:
        #         #Tell the user the genre is not allowed
        #         print("Genre not valid. Please choose a valid genre")
        #         #Printing out all the valid genres
        #         print(Video.return_valid_genres())
        #     #asking if they want to add another genre
        #     print("Would you like to add another genre? (y/n)")
        #     #getting the user input
        #     another = input().lower()
        #     #if they aswear no then break the loop
        #     if another == "n":
        #         break
        # # creating the new video object with the gathered info
        # new_video = Video(get_video_id, get_title, get_description, get_duration, get_release_year, genres_list)
        # #adding the new video to the videos dictionary
        # videos[new_video.get_video_id()] = new_video
        # #print saying it has been added
        # print("Video added to list")
        # #print out the video info added
        # print(videos[new_video.get_video_id()])


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
        # going through dictionary looking through the values stored in each key for the one seached for
        # for video in videos.values():
        #     # If the search gets a ping back then it will move on, all lower case as user may spell it with caps or without
        #     if remove_video.lower() in video.title.lower():
        #         #Removing the video from the dictionary
        #         del videos[video.get_video_id()]
        #         print(f"Video removed from list")
        #         # Will break out of the function if its found
        #         break
        # else:
        #     print("Video not found.")

    #If 0 is entered
    case "0":
        print("Exiting Application. Goodbye!")

    case _:
        print("Invalid choice. Please choose a valid choice.")

    #added to dev_main
