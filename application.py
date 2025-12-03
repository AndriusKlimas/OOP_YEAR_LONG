from catalogue import Video
# from user_records import User

users = []
videos = {

}
#setting up video classes and storing them in variables
video1 = Video(1, "Inception", "A mind-bending thriller", 8880, 2010, ["scifi", "thriller"])
video2 = Video(2, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
video3 = Video(3, "The Godfather", "Crime family saga", 10500, 1972, ["drama", "crime"])
video4 = Video(4, "Toy Story", "Toys come to life", 4860, 1995, ["animation", "comedy"])
video5 = Video(5, "UP", "Ballon building", 16732, 2008, ["animation", "drama"])
# users = User
#Mnayally adding videos to the dictionary
videos[video1._video_id] = video1
videos[video2._video_id] = video2
videos[video3._video_id] = video3
videos[video4._video_id] = video4
videos[video5._video_id] = video5


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
        #Peint all videos currently in the dictionary
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
        # going through dictionary looking through the values stored in each key for the one seached for
        for video in videos.values():
            #calling the method check_genre from class to check the genre is their
            if video.check_genre(search_genre):
                #If it is their then print the info for the video that had the genre in it
                print(video)

    #of 4 is entered
    case "4":
        print("Feature coming soon!")

    #If 5 is entered
    case "5":
        print("Feature coming soon!")

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
        videos[new_video._video_id] = new_video
        print("Video added to list")
        print(videos[new_video._video_id])


    #If 7 is entered
    case "7":
        #Need to work on as multiple videos may have same name
        remove_video = input("Please enter the name of the video you would like to remove: ")
        # going through dictionary looking through the values stored in each key for the one seached for
        for video in videos.values():
            # If the search gets a ping back then it will move on, all lower case as user may spell it with caps or without
            if remove_video.lower() in video.title.lower():
                #Removing the video from the dictionary
                del videos[video._video_id]
                print(f"Video removed from list")
                # Will break out of the function if its found
                break
        else:
            print("Video not found.")

    #If 0 is entered
    case "0":
        print("Exiting Application. Goodbye!")

    case _:
        print("Invalid choice. Please choose a vlaid choice.")

    #added to dev_main
