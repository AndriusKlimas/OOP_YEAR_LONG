from catalogue import Video
from user_records import User, PlayRecord
# from user_records import User

users = {}
videos = {}
play_records = {}

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

record1 = User.start_play(user1, video1._video_id, 500)
record2 = User.start_play(user1, video3._video_id)
record3 = User.start_play(user2, video2._video_id, 1000)
record4 = User.start_play(user2, video5._video_id)
record5 = User.start_play(user3, video3._video_id, 2500)
record6 = User.start_play(user3, video1._video_id)
record7 = User.start_play(user1, video2._video_id, 600)
record8 = User.start_play(user4, video4._video_id)
record9 = User.start_play(user5, video5._video_id, 60)
record10 = User.start_play(user2, video1._video_id, 4000)

#updates the play_record dictionary with the play_history dictionary stored in User class
play_records = User.get_play_history()

def sec_to_min(seconds):
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
        #Print all videos currently in the dictionary
        #Loop through all videos in the dictionary
        for video in videos.values():
            #Print each one, one by one
            print(video)
    #If 2 is entered(stack overflow helped with searching this)
    case "2":
        #Setting a variable to sore the name of the movie
        search_video = input("Please enter the Video title you are looking for: ")
        #going through dictionary looking through the values stored in each key for the one seached for
        for video in videos.values():
            #If the search gets a ping back then it will move on, all lower case as user may spell it with caps or without
            if search_video.lower() in video.title.lower():
                #Printing that specific video with all the info needed
                print(video)
                #Will break out of the function if its found
                break
        #f not found/broken out of then it will print the below
        else:
            print("Video not found.")

    #If 3 is entered
    case "3":
        search_genre = input("Please enter the genre you would like to look for: ")
        # going through dictionary looking through the values stored in each key for the one searched for
        for video in videos.values():
            #calling the method check_genre from class to check the genre is their
            if video.check_genre(search_genre):
                #If it is their then print the info for the video that had the genre in it
                print(video)

    #of 4 is entered
    case "4":
        #creates an empty list to store the play records for the requested user
        user_records = []
        #asks the user to enter the username of the user they want to see the history of
        username = input("Please enter the username of the user you would like to show the play history for: ")
        #for loop to search through the values of each record in the play_records dictionary
        for record in play_records.values():

            if record.get_username() == username:
                user_records.append(record)
        if not user_records:
            print("Invalid username entered")
        else:
            print(f"Here is the play history for {username}")
            for r in user_records:
                vid_id = r.get_video_id()
                title = videos[vid_id].title
                print(f"{title} starting at {sec_to_min(r.get_pos())}")

    #If 5 is entered
    case "5":
        #asks the user to enter the username they wish to play a video from
        username = input("Please enter the username of the user you wish to use: ")
        #if the username enterd is found within the users dictionary
        if username in users:
            #it asks the user to enter the title of the video they wish to watch
            video = input("Please enter the title of the video: ")
            #creates a variable for when the program finds the movie they entered
            found = False
            #for loop to search through all the movie titles in the videos dictionary
            for t in videos.values():
                #if the title in the dictionary is the same as the title the user entered
                if t.title.lower() == video.lower():
                    #uses the start_play function to create a play record for the specified user in the dictionary with the video_id of the specified video
                    users[username].start_play(t._video_id)
                    'lets the user know that the user is now playing the movie they requested'
                    print(f"{users[username].get_username()} is now playing {t.title}")
                    #changes the found variable to true
                    found = True
                    #breaks from the loop
                    break
            #if the title they entered was not found in the list
            if not found:
                #lets the user know they entered an invalid title
                print("Invalid title entered")
        #if the username they entered wasnt found in the user dictionary
        else:
            #lets the user know they entered an invalid username
            print("Invalid username entered")

    #If 6 is entered
    case "6":
        genres_list = []
        print("Please enter the following details to add a new video:")
        get_video_id = max(videos.keys()) + 1
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
            genres_list.append(get_genres)
            another = input().lower()
            if another == "n":
                break
        new_video = Video(get_video_id, get_title, get_description, get_duration, get_release_year, genres_list)
        videos[new_video.get_video_id()] = new_video
        print("Video added to list")
        print(videos[new_video.get_video_id()])


    #If 7 is entered
    case "7":
        #Need to work on as multiple videos may have same name
        remove_video = input("Please enter the name of the video you would like to remove: ")
        # going through dictionary looking through the values stored in each key for the one seached for
        for video in videos.values():
            # If the search gets a ping back then it will move on, all lower case as user may spell it with caps or without
            if remove_video.lower() in video.title.lower():
                #Removing the video from the dictionary
                del videos[video.get_video_id()]
                print(f"Video removed from list")
                # Will break out of the function if its found
                break
        else:
            print("Video not found.")

    #If 0 is entered
    case "0":
        print("Exiting Application. Goodbye!")

    case _:
        print("Invalid choice. Please choose a valid choice.")

    #added to dev_main
