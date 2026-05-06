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

class TextUserDataAccess(IUserDataAccess):

    def load(self) -> dict[str, User]:
        """Load user data from text file
        Returns:
            dict[str, User]: Dict of users
        """
        us = {}
        u1 = User("NoahClarke123", "Password123!")
        u2 = User("Film_Critic1", "ILoveMovies0000")
        u3 = User("Bob_iscool", "iamBob05$")
        u4 = User("Jedibob212", "Sidius66")
        u5 = User("IronManFan3", "TonyStark44!")
        u6 = User("admin", "Password1!")

        for u in (u1, u2, u3, u4, u5, u6):
            us[u.get_username()] = u

        # Seed play history in the same internal structure as JSON-loaded users.
        u1.start_play(1, 120)
        u1.start_play(4, 950)

        u2.start_play(2, 3400)
        u2.start_play(3, 5200)

        u3.start_play(5, 600)
        u4.start_play(6, 1800)
        u5.start_play(1, 60)

        logger.info(f"Successfully loaded {len(us)} default users their play history")
        return us

    def store(self, users: dict[str, User]) -> None:
        """Store users to default dictionary"""
        pass