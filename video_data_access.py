from abc import ABC, abstractmethod
from catalogue import Video
import json
import logging



logger = logging.getLogger(__name__)


class IVideoDataAccess(ABC):
    """Abstract class to store and retrieve video data from database"""

    @abstractmethod
    def load(self) -> dict[str, list[Video]]:
        """Load videos from file

        Returns:
            dict[str, list[Video]]: Dict with titles as keys and lists of Video objects as values

        Raises:
            FileNotFoundError: If video data file not exists
        """
        pass

    @abstractmethod
    def store(self, data: dict[str, list[Video]]) -> None:
        """Store video data to database

        Args:
            data (dict[str, list[Video]]): Dict with titles as keys and lists of Video objects as values
        """
        pass

class JSONVideoDataAccess(IVideoDataAccess):
    def __init__(self, filename: str):
        """Initialises JSON data access

        Args:
            filename(str): Path to JSON file

        Raises:
            FileNotFoundError: If video data file not exists
        """
        try:
            with open(filename, "r") as file:
                pass
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filename}")

        self._filename = filename

    def load(self) -> dict[str, list[Video]]:
        """Load video data from JSON file

        Returns:
            dict[str, list[Video]]: Dict with titles as keys and lists of Video objects as values

        Raises:
            ValueError: If JSON is malformed or doesn't contain video data
        """
        try:
            with open(self._filename, "r") as file:
                videos_data = json.load(file)

            videos_dict = {}
            for title, videos_list in videos_data.items():
                videos_dict[title] = []
                for i, video_data in enumerate(videos_list, start=1):
                    try:
                        video = Video.from_dict(video_data)
                        videos_dict[title].append(video)
                    except Exception as e:
                        logger.error(f"Invalid video record #{i} under '{title}' in {self._filename}: {e}")
                        continue

            logger.info(f"Successfully loaded videos from {self._filename}")
            return videos_dict

        except Exception as e:
            logger.error(f"Error loading videos from {self._filename}: {e}")
            raise

    def store(self, videos: dict[str, list[Video]]) -> None:
        """Store videos to JSON file

        Args:
            videos (dict[str, list[Video]]): Dict with titles as keys and lists of Video objects as values
        """
        try:
            videos_data = {}
            for title, videos_list in videos.items():
                videos_data[title] = [video.to_dict() for video in videos_list]

            with open(self._filename, "w") as file:
                json.dump(videos_data, file, indent=2)
            logger.info(f"Successfully saved videos to file {self._filename}")
        except Exception as e:
            logger.error(f"Error saving videos to {self._filename}: {e}")
            raise