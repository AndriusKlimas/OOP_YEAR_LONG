from abc import ABC, abstractmethod
from user_records import User
import json
import logging

logger = logging.getLogger(__name__)

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


class JSONUserDataAccess(IUserDataAccess):

    def __init__(self, filename: str):
        """Initialises JSON data access

        Args:
            filename(str): Path to JSON file

        Raises:
            FileNotFoundError: If user data file not exists

        """

        try:
            with open(filename, "r") as file:
                pass
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filename}")

        self._filename = filename


    def load(self) -> dict[str, User]:
        """Load user data from JSON file

        Returns:
            dict[str, User]: Dict of users

        Raises:
            ValueError: If JSON is malformed or doesnt contain user data
        """
        try:
            with open(self._filename, "r") as file:
                users_list = json.load(file)

            users_dict = {}
            for i, user_data in enumerate(users_list, start=1):
                try:
                    user = User.from_dict(user_data)
                    users_dict[user.get_username()] = user
                except Exception as e:
                    print(f"Invalid user record #{i} in {self._filename}: {e}")
                    logger.error(f"Invalid user record #{i} in {self._filename}: {e}")
                    continue

            logger.info(f"Successfully loaded {len(users_dict)} users from {self._filename}")
            return users_dict

        except Exception as e:
            logger.error(f"Error loading users from {self._filename}: {e}")
            raise


    def store(self, users: dict[str, User]) -> None:
        """Store users to JSON file

        Args:
        users: Dict of users

        """
        try:
            users_list = [user.to_dict() for user in users.values()]
            with open(self._filename, "w") as file:
                json.dump(users_list, file, indent=2)
            logger.info(f"Successfully saved {len(users_list)} to file {self._filename}")
        except Exception as e:
            logger.error(f"Error saving users to {self._filename}: {e}")
            raise
