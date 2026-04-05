#imports annotations for type hinting

#**FOR ANDRIUS - FMT2, V1, V3 in playrecord and search feature for app**
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
        if not isinstance(genre,str):
            return False

        if genre not in self._genres and Video.validate_genre(genre):
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
        if genre.lower() in self._genres and genre.lower() in Video.validate_genre(genre):
            return True
        else:
            return False


    #New thing added
    @staticmethod
    def validate_genre(genre: str) -> bool:
        """ checks if the genre is present in the static list
        args:
        genre: The genre to be checked.
        returns:
        True if the genre is present in the static list, False otherwise.
        """
        if genre.lower() in Video._VALID_GENRES:
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

    def get_description(self) -> str:
        """Get the description of the video.
        Returns:
            Description of the video.
            """
        return self.description

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
        return f"Title is {self.get_title()} and description is {self.get_description()}, Duration is {self.get_duration_seconds()} seconds, Release year is {self.get_release_year()}. Genres are {', '.join(self.get_genres())}"

    #for a developer
    def __repr__(self) -> str:
        """Return a developer-friendly string representation of the video.

        Returns:
            A formatted string with all video details and ID.
        """
        return f"Video_ID: {self.get_video_id()}, Title: {self.get_title()}, Description: {self.get_description()}, Duration: {self.get_duration_seconds()}, Release Year: {self.get_release_year()}, Genres: {self.get_genres()}"

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

    def __le__(self, other: object) -> bool | NotImplementedType:
        """Check equality between two videos based on their video IDs.
        Args:
            other: The object to compare with.
        Returns:
        True if both videos have the same ID, False otherwise.
        NotImplemented if other is not a Video instance.
        """
        if not isinstance(other, Video):
            return NotImplemented
        return self._video_id <= other._video_id

    def __ge__(self, other: object) -> bool | NotImplementedType:
        """Check inequality between two videos based on their video IDs.
        Args:
            other: The object to compare with.

        return:
        True if both videos have the same ID, False otherwise.
        NotImplemented if other is not a Video instance.
            """
        if not isinstance(other, Video):
            return NotImplemented
        return self._video_id >= other._video_id

    def __lt__(self, other: object) -> bool | NotImplementedType:
        """Check equality between two videos based on their video IDs.
        Args:
            other: The object to compare with.

        return:
        True if both videos have the same ID, False otherwise.
        NotImplemented if other is not a Video instance.
            """
        if not isinstance(other, Video):
            return NotImplemented
        return self._video_id < other._video_id


    def __gt__(self, other: object) -> bool | NotImplementedType:
        """Check inequality between two videos based on their video IDs.
        Args:
            other: The object to compare with.

        return:
        True if both videos have the same ID, False otherwise.
        NotImplemented if other is not a Video instance.
            """
        if not isinstance(other, Video):
            return NotImplemented
        return self._video_id > other._video_id

    @classmethod
    def from_dict(cls, data: dict) -> 'Video':
        """
        Creates a Video object from a dictionary.

        Returns:
            Video object based on the dict

        Raises:
            ValueError: If required fields are missing or invalid
        """
        try:
            # Validate type field if present
            if data.get("type") is not None and data.get("type") != cls.__name__:
                raise ValueError(
                    f"Invalid type value ({data.get('type')}) within dict - {cls.__name__} cannot deserialise")

            # Extract required fields
            video_id = data["video_id"]
            title = data["title"]
            description = data["description"]
            duration_seconds = data["duration_seconds"]
            release_year = data["release_year"]
            genres = data.get("genres", [])

            # Validate required fields
            if not isinstance(video_id, int):
                raise ValueError(f"video_id must be an integer, got {type(video_id)}")
            if not isinstance(title, str) or not title.strip():
                raise ValueError(f"title must be a non-empty string")
            if not isinstance(description, str) or not description.strip():
                raise ValueError(f"description must be a non-empty string")
            if not isinstance(duration_seconds, int) or duration_seconds <= 0:
                raise ValueError(f"duration_seconds must be a positive integer")
            if not isinstance(release_year, int):
                raise ValueError(f"release_year must be an integer")
            if not isinstance(genres, list):
                raise ValueError(f"genres must be a list")

            return cls(
                video_id=video_id,
                title=title,
                description=description,
                duration_seconds=duration_seconds,
                release_year=release_year,
                genres=genres
            )

        except KeyError as e:
            raise ValueError(f"JSON error occurred when building Video - cannot find key {e}")
        except Exception as e:
            raise ValueError(f"Unexpected error creating Video from dict: {str(e)}")



    def to_dict(self) -> dict:
        """Convert Video object to dictionary format for JSON serialization.

            Args:
                self: The Video object instance

            Returns:
                dict: Dictionary containing all video attributes with keys
            """
        data = {}
        data["type"] = self.__class__.__name__

        data["video_id"] = self._video_id
        data["title"] = self.title
        data["description"] = self.description
        data["duration_seconds"] = self._duration_seconds
        data["release_year"] = self._release_year
        data["genres"] = self._genres

        return data
