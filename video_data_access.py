from abc import ABC, abstractmethod
from catalogue import Video
import json
import logging

from video_serivice import VideoService

logger = logging.getLogger(__name__)


class JSONVideoDataAccess():
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