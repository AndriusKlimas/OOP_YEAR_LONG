#imports annotations for type hinting
from __future__ import annotations

from types import NotImplementedType
from typing import List, Optional


#Creating the class
class Video:
    #Created a class variable to stare all valid genres
    _VALID_GENRES = ["action", "comedy", "drama", "horror", "romance", "scifi", "documentary", "animation", "thriller", "crime"]

    #creating a constructor
    def __init__(
        self,video_id: int,title: str,description: str,duration_seconds: int,release_year: int,genres: Optional[List[str]] = None) -> None:
        """Initialize a Video object.

        Args:
            video_id: Unique identifier for the video.
            title: Title of the video.
            description: Description of the video.
            duration_seconds: Duration of the video in seconds.
            release_year: Release year of the video.
            genres: Optional list of genres; defaults to an empty list.
        """
        self._genres: List[str] = list(genres) if genres is not None else []

        if not Video.validate_id(video_id):
            print("Invalid video id.")
            exit()
        self._video_id: int = video_id

        if not Video.validate_title(title):
            print("Invalid title.")
            exit()
        self.title: str = title

        if not Video.validate_description(description):
            print("Invalid description.")
            exit()
        self.description: str = description

        if not Video.validate_duration_seconds(duration_seconds):
            print("Invalid duration seconds.")
            exit()
        self._duration_seconds: int = duration_seconds

        if not Video.validate_release_year(release_year):
            print("Invalid release year.")
            exit()
        self._release_year: int = release_year

    #method to get title
    def get_title(self) -> str:
        """Return the title of the video.

        Returns:
            The title of the video.
        """
        return self.title

    #Creating a static method
    @staticmethod
    def return_valid_genres() -> List[str]:
        """Return a list of all valid genres.

        Returns:
            A copy of the list of all valid genres.
        """
        return list(Video._VALID_GENRES)

    #method to add genre
    def add_genre(self, genre: str) -> bool:
        """Add a genre to the video if it is valid and not already present.

        Args:
            genre: The genre to be added.

        Returns:
            True if the genre was successfully added, False otherwise.
        """
        if genre not in self._genres and genre in Video._VALID_GENRES:
            self._genres.append(genre.lower())
            return True
        else:
            return False

    #method to check genre
    def check_genre(self, genre: str) -> bool:
        """Check if a genre is present in the video.

        Args:
            genre: The genre to be checked.

        Returns:
            True if the genre is in the video, False otherwise.
        """
        if genre.lower() in self._genres and genre.lower() in Video._VALID_GENRES:
            return True
        else:
            return False

    #for good practice to return private variables
    def get_video_id(self) -> int:
        """Get the unique identifier of the video.

        Returns:
            The video ID.
        """
        return self._video_id

    # for good practice to return private variables
    def get_duration_seconds(self) -> int:
        """Get the duration of the video in seconds.

        Returns:
            The duration in seconds.
        """
        return self._duration_seconds

    # for good practice to return private variables
    def get_release_year(self) -> int:
        """Get the release year of the video.

        Returns:
            The release year.
        """
        return self._release_year

    # for good practice to return private variables
    def get_genres(self) -> List[str]:
        """Get the list of genres for the video.

        Returns:
            A copy of the genres list.
        """
        return list(self._genres)

    @staticmethod
    def validate_id(video_id: int) -> bool:
        """Validate if a video ID is valid.

        A valid video ID must be a non-negative integer.

        Args:
            video_id: The video ID to validate.

        Returns:
            True if the video ID is valid, False otherwise.
        """
        if video_id is None:
            return False
        if video_id < 0:
            return False
        if not isinstance(video_id, int):
            return False
        return True

    @staticmethod
    def validate_title(title: str) -> bool:
        """Validate if a title is valid.

        A valid title must not be None.

        Args:
            title: The title to validate.

        Returns:
            True if the title is valid, False otherwise.
        """
        if title is None:
            return False
        return True

    @staticmethod
    def validate_description(description: str) -> bool:
        """Validate if a description is valid.

        A valid description must not be None.

        Args:
            description: The description to validate.

        Returns:
            True if the description is valid, False otherwise.
        """
        if description is None:
            return False
        return True

    @staticmethod
    def validate_duration_seconds(duration_seconds: int) -> bool:
        """Validate if a duration in seconds is valid.

        A valid duration must be a non-negative integer.

        Args:
            duration_seconds: The duration in seconds to validate.

        Returns:
            True if the duration is valid, False otherwise.
        """
        if duration_seconds is None:
            return False
        if duration_seconds < 0:
            return False
        return True

    @staticmethod
    def validate_release_year(release_year: int) -> bool:
        """Validate if a release year is valid.

        A valid release year must be a non-negative integer.

        Args:
            release_year: The release year to validate.

        Returns:
            True if the release year is valid, False otherwise.
        """
        if release_year is None:
            return False
        if release_year < 0:
            return False
        return True


    #to print out the info about the video
    def __str__(self) -> str:
        """Return a user-friendly string representation of the video.

        Returns:
            A formatted string with video information.
        """
        return f"Title is {self.title} and description is {self.description}, Duration is {self.get_duration_seconds()} seconds, Release year is {self.get_release_year()}. Genres are {', '.join(self.get_genres())}"

    #for a developer
    def __repr__(self) -> str:
        """Return a developer-friendly string representation of the video.

        Returns:
            A formatted string with all video details and ID.
        """
        return f"Video_ID: {self.get_video_id()}, Title: {self.title}, Description: {self.description}, Duration: {self.get_duration_seconds()}, Release Year: {self.get_release_year()}, Genres: {self.get_genres()}"

    #defining equality method
    def __hash__(self) -> int:
        """Get the hash value of the video.

        Returns:
            The hash value based on the video ID.
        """
        return hash((self.get_video_id()))

    #defining format method
    def __format__(self, format_spec: str) -> str:
        """Format the video information based on the format specification.

        Args:
            format_spec: The format specification ("short" or "long").

        Returns:
            A formatted string representation of the video.
        """
        match format_spec:
            case "short":
                return f"{self.title}, {self.get_release_year()}, {self.get_duration_seconds()} seconds)"
            case "long":
                return f"Title: {self.title}\nDescription: {self.description}\nDuration: {self.get_duration_seconds()} seconds\nRelease Year: {self.get_release_year()}\nGenres: {', '.join(self.get_genres())}"
            case _:
                return "Please enter a valid format"

    def __eq__(self, other: object) -> bool | NotImplementedType:
        """Check equality between two videos based on their video IDs.

        Args:
            other: The object to compare with.

        Returns:
            True if both videos have the same ID, False otherwise.
            NotImplemented if other is not a Video instance.
        """
        if not isinstance(other, Video):
            return NotImplemented

        return self._video_id == other._video_id

    def __ne__(self, other: object) -> bool | NotImplementedType:
        """Check inequality between two videos based on their video IDs.

        Args:
            other: The object to compare with.

        Returns:
            True if the videos have different IDs, False otherwise.
            NotImplemented if other is not a Video instance.
        """
        if not isinstance(other, Video):
            return NotImplemented

        return self._video_id != other._video_id