#imports annotations for type hinting
from __future__ import annotations

#Creating the class
class Video:
    #Created a class variable to stare all valid genres
    VALID_GENRES = ["action", "comedy", "drama", "horror", "romance", "scifi", "documentary", "animation", "thriller", "crime"]

    #creating a constructor
    def __init__(self, _video_id : int, title:str, description:str, _duration_seconds:int, _release_year:int, _genres:list = []):
        self._genres = _genres
        self._video_id = _video_id
        self.title = title
        self.description = description
        self._duration_seconds = _duration_seconds
        self._release_year = _release_year

    #method to get title
    def get_title(self) -> str:
        return self.title

    #Creating a static method
    @staticmethod
    #setting a method called return_valid_genres
    def return_valid_genres() -> list:
        #returning a copy list of all valid genres
        return list(Video.VALID_GENRES)

    #method to add genre
    def add_genre(self, genre:str) -> bool:
        #checking if the genre is not in the video, and if it is in the valid genres
        if genre not in self._genres and genre in Video.VALID_GENRES:
            #adding it to the video if it is not in the list and in valid genres
            self._genres.append(genre.lower())
            #returning TRUE
            return True
        #else
        else:
            #returning FALSE
            return False

    #method to check genre
    def check_genre(self, genre:str) -> bool:
        #checking if the genre is in the video and if it is in the valid genres
        if genre.lower() in self._genres and genre.lower() in Video.VALID_GENRES:
            #returning True
            return True
        #else
        else:
            #Returning false
            return False

    #for good practice to return private variables
    def get_video_id(self) -> int:
        return self._video_id

    # for good practice to return private variables
    def get_duration_seconds(self) -> int:
        return self._duration_seconds

    # for good practice to return private variables
    def get_release_year(self) -> int:
        return self._release_year

    # for good practice to return private variables
    def get_genres(self) -> list:
        return list(self._genres)

    #to print out the info about the video
    def __str__(self) -> str:
        return f"Title is {self.title} and description is {self.description}, Duration is {self.get_duration_seconds()} seconds, Release year is {self.get_release_year()}. Genres are {', '.join(self.get_genres())}"

    #for a developer
    def __repr__(self) -> str:
        return f"Video_ID: {self.get_video_id()}, Title: {self.title}, Description: {self.description}, Duration: {self.get_duration_seconds()}, Release Year: {self.get_release_year()}, Genres: {self.get_genres()}"

    #defining equality method
    def __hash__(self) -> int:
        return hash((self.get_video_id()))

    #defining format method
    def __format__(self, format_spec: str) -> str:
        match format_spec:
            case "short":
                return f"{self.title}, {self.get_release_year()}, {self.get_duration_seconds()} seconds)"
            case "long":
                return f"Title: {self.title}\nDescription: {self.description}\nDuration: {self.get_duration_seconds()} seconds\nRelease Year: {self.get_release_year()}\nGenres: {', '.join(self.get_genres())}"
            case _:
                return "Please enter a valid format"

    def __eq__(self, other: object) -> bool | NotImplemented:
        """sets up the eq method for the video class

        This method checks that the video id is equal to the video id of the other entered

        """
        if not isinstance(other, Video):
            return NotImplemented

        return self._video_id == other._video_id

    def __ne__(self, other: object) -> bool | NotImplemented:
        """sets up the ne method for the video class

        This method checks that the video id is not equal to the video id of the other entered

        """
        if not isinstance(other, Video):
            return True

        return self._video_id != other._video_id