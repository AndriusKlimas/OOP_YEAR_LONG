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

