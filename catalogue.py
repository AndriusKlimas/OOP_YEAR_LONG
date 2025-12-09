#imports annotations for type hinting
from __future__ import annotations

from types import NotImplementedType


#Creating the class
class Video:
    #Created a class variable to stare all valid genres
    VALID_GENRES = ["action", "comedy", "drama", "horror", "romance", "scifi", "documentary", "animation", "thriller", "crime"]

    #creating a constructor
    def __init__(self, _video_id : int, title:str, description:str, _duration_seconds:int, _release_year:int, _genres:list = []):
        """ set up the video class cunstructor
        args:
            _video_id (int): unique identifier for the video
            title (str): title of the video
            description (str): description of the video
            _duration_seconds (int): duration of the video in seconds
            _release_year (int): release year of the video
            _genres (list): list of genres for the video
        """
        self._genres = _genres
        self._video_id = _video_id
        self.title = title
        self.description = description
        self._duration_seconds = _duration_seconds
        self._release_year = _release_year

    #method to get title
    def get_title(self) -> str:
        """ returning a private class variable

        return: (str) title of the video
        """
        return self.title

    #Creating a static method
    @staticmethod
    #setting a method called return_valid_genres
    def return_valid_genres() -> list:
        """ returning all valid genres in a duplicate list

        return: (list) list of all valid genres
        """
        #returning a copy list of all valid genres
        return list(Video.VALID_GENRES)

    #method to add genre
    def add_genre(self, genre:str) -> bool:
        """
        args:
            genre (str): genre to be added
        return:
            bool: True if genre was added, False otherwise
        """
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
        """ checking if a genre is in the video and a valid genre
        args:
            genre (str): genre to be checked
        return:
            bool: True if genre is in the video, False otherwise

        """
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
        """ getting the private class variable video id

        return:
            returns the video id (int)
        """
        return self._video_id

    # for good practice to return private variables
    def get_duration_seconds(self) -> int:
        """ geting the private class variable duration seconds

        return:
            returns the duration in seconds (int)
        """
        return self._duration_seconds

    # for good practice to return private variables
    def get_release_year(self) -> int:
        """ getting the private class variable release year

        return:
            returns the release year (int)
        """
        return self._release_year

    # for good practice to return private variables
    def get_genres(self) -> list:
        """ getting the private class variable genres

        return:
            returns the genres (list)
        """
        return list(self._genres)

    #to print out the info about the video
    def __str__(self) -> str:
        """ to print out info for user

        return:
            returns the string representation of the video
        """
        return f"Title is {self.title} and description is {self.description}, Duration is {self.get_duration_seconds()} seconds, Release year is {self.get_release_year()}. Genres are {', '.join(self.get_genres())}"

    #for a developer
    def __repr__(self) -> str:
        """ to print out info for developer

        return:
            returns the developer representation of the video
        """
        return f"Video_ID: {self.get_video_id()}, Title: {self.title}, Description: {self.description}, Duration: {self.get_duration_seconds()}, Release Year: {self.get_release_year()}, Genres: {self.get_genres()}"

    #defining equality method
    def __hash__(self) -> int:
        """ getting the hash value of the video

        return:
            returns the hash value of the video
        """
        return hash((self.get_video_id()))

    #defining format method
    def __format__(self, format_spec: str) -> str:
        """ formatting the video info
        args:
            format_spec (str): format specification

        return:
            returns the formatted string representation of the video
        """
        match format_spec:
            case "short":
                return f"{self.title}, {self.get_release_year()}, {self.get_duration_seconds()} seconds)"
            case "long":
                return f"Title: {self.title}\nDescription: {self.description}\nDuration: {self.get_duration_seconds()} seconds\nRelease Year: {self.get_release_year()}\nGenres: {', '.join(self.get_genres())}"
            case _:
                return "Please enter a valid format"

    def __eq__(self, other: object) -> bool | NotImplementedType:
        """ checking equality between two videos
        args:
            other (object): other object to compare with
        return:
            bool: True if equal, False otherwise

        """
        if not isinstance(other, Video):
            return NotImplemented

        return self._video_id == other._video_id

    def __ne__(self, other: object) -> bool | NotImplementedType:

        """ checking inequality between two videos
        args:
            other (object): other object to compare with
        return:
            bool: True if not equal, False otherwise
        """
        if not isinstance(other, Video):
            return True

        return self._video_id != other._video_id