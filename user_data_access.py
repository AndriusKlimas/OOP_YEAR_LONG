from abc import ABC, abstractmethod
from user_records import User
import json
import logging


class IUserDataAccess(ABC):
    """Abstract class to store and retrieve user data from database

    """
    @abstractmethod
    def load(self) -> dict[str, User]:
        """Load users from file

        Returns:
            dict[str, User]: Dict of users

        Raises:
            FileNotFoundError: If user data file not exists
        """
        pass


    @abstractmethod
    def store(self, data: dict[str, User]) -> None:
        """Store user data to database

        Args:
            data (dict[str, User]): Dict of users

        """
        pass

