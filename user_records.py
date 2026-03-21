#imports annotations for type hinting
from __future__ import annotations
from functools import total_ordering
from types import NotImplementedType

class InvalidUserError(Exception):
    pass

#creates a class for the play records
class PlayRecord:

    record_counter: int = 1

    def __init__(self, username: str, video_id: int, position_in_seconds: int):
        """ sets up the constructor for the PlayRecord class

        Args:
            username (str): The username for the user
            video_id (int): Video id of the video in the play record
            position_in_seconds (int): Position in seconds of the video
        """
        self._play_id = PlayRecord.record_counter
        self._username = username
        self._video_id = video_id
        self._position_in_seconds = position_in_seconds

        #the play id increases each time it is called
        PlayRecord.record_counter += 1

    def __str__(self) -> str:
        """ sets up the str method for the playrecord class

        Returns:
            statement including username and position_in_seconds
        """
        return f"Username: {self._username} Position in Seconds: {self.get_pos()}"

    def __repr__(self) -> str:
        """ sets up the repr method for the playrecord class

        Returns:
            statement including class name, play_id, username, video_id and position_in_seconds
        """
        return f"{self.__class__.__name__} Play ID: {self.get_play_id()} Username: {self._username} Video ID: {self.get_video_id()} Position in Seconds: {self.get_pos()} "

    def __eq__(self, other: object) -> bool | NotImplementedType:
        """ Compares two PlayRecord objects

        Compares the play_id in both objects
        Args:
            other (object): The other PlayRecord object to check against

        Returns:
             NotImplemented if other is not a PlayRecord;
             True if other's play_id equals this play_id; False if the play_ids differ.
        """
        if not isinstance(other, PlayRecord):
            return NotImplemented

        return self._play_id == other._play_id

    def __ne__(self, other: object) -> bool | NotImplementedType:
        """Compares two PlayRecord objects for inequality by delegating to __eq__.

        This avoids duplicating the equality logic. If __eq__ returns NotImplemented,
        we propagate it so Python can try reflected operations.
        """
        eq_result = self.__eq__(other)
        if eq_result is NotImplemented:
            return NotImplemented
        return not eq_result

    def get_play_id(self) -> int:

        """ gets the play_id of the play record

        Returns:
            play_id of play record
        """
        return self._play_id

    def get_video_id(self) -> int:
        """ gets the video_id of the video in the play record

        Returns:
            video_id for video in play record
        """
        return self._video_id

    def get_pos(self) -> int:
        """ gets the position in seconds

        Returns:
            position in seconds for this user
        """
        return self._position_in_seconds

    def get_username(self) -> str:
        """ gets the username of the user

        Returns:
            username for the user
        """
        return self._username


#creates a class for the Users
@total_ordering
class User:

    def __init__(self, username: str, password: str):
        """ sets up the constructor for the user class
        
        Args:
            username (str): The username for the user
            password (str): The password for the user

        """

        if not User.validate_password(password):
            raise InvalidUserError("Password does not meet the requirements")

        self._username = username

        if not User.validate_username(username):
            raise InvalidUserError("Username does not meet the requirements")

        self.__password = password
        self._play_history = {}

    def get_username(self) -> str:
        """ gets the username of the user

        Returns:
            username for the user
        """
        return self._username

    def get_history(self) -> dict[int, list[PlayRecord]]:
        """ gets the play history of the user

        Returns:
            dictionary of the play history for that user (video_id as key, list of PlayRecords as value)
        """
        #creates a new dictionary to store the copied history
        history_copy = {}
        #loops through each video_id in the play history
        for vid_id in self._play_history:
            #creates a copy of the list of play records for this video_id
            history_copy[vid_id] = list(self._play_history[vid_id])
        #returns the copied dictionary
        return history_copy


    def __str__(self) -> str:
        """ sets up the str method for the user class

        Returns:
            statement including username and password (hidden)
        """
        return f"Username: {self._username} Password = ********"

    def __repr__(self) -> str:
        """ sets up the repr method for the user class

        Returns:
            statement including class name, username and password (hidden)
        """
        return f"{self.__class__.__name__}\nUsername: {self._username}\nPassword: ********\nPLay History: {self._play_history}"

    def __format__(self, format_spec: str) -> str:
        """ sets up the format method for the user class

        Args:
            format_spec (str): Which type of format to use

        Returns:
            short format statement if format_spec is "short";
            long format statement if format_spec is "long";
            repr if invalid option is given
        """
        match format_spec:
            case "short":
                return f"Username: {self._username}"
            case "long":
                return f"Username: {self._username} Password: ********"
            case _:
                print("Invalid option selected")
                return repr(self)

    def __eq__(self, other: object) -> bool | NotImplementedType:
        """ Compares two User objects

        Compares the username in both objects
        Args:
            other (object): The other User object to check against

        Returns:
             NotImplemented if other is not a User;
             True if other's username equals this username; False if the usernames differ.
        """
        if not isinstance(other, User):
            return NotImplemented

        return self._username == other._username

    def __ne__(self, other: object) -> bool | NotImplementedType:
        """Compares two User objects for inequality by delegating to __eq__.

        This avoids duplicating the equality logic. If __eq__ returns NotImplemented,
        we propagate it so Python can try reflected operations.
        """
        eq_result = self.__eq__(other)
        if eq_result is NotImplemented:
            return NotImplemented
        return not eq_result

    def __lt__(self, other: object) -> bool | NotImplementedType:
        """Compares two User objects and ranks them based on their username


        Args:
            other (object): The other User object to check against

        Returns:
            Whichever object is less than the other
        """
        if not isinstance(other, User):
            return NotImplemented

        return self._username < other._username

    def __hash__(self) -> int:
        """ Changes the unique identifier for the User class (username) to a number


        Returns:
            hashed version of username
        """
        return hash(self._username)

    #defines a function called start_play which takes in self, video_id and position in seconds as pos
    def start_play(self, video_id: int, pos: int = 0) -> bool:
        """creates a play record using info from the user class

         Args:
             video_id (int): The video id of the video_id the user wants to watch
             pos (int): The position of the video in seconds

         Returns:
             True if the video id and position are valid, False otherwise
         """

        if video_id <= 0 or pos < 0:
            return False
        else:
            play_record = PlayRecord(self._username, video_id, pos)
            if video_id not in self._play_history:
                #if not, creates a new empty list for this video_id
                self._play_history[video_id] = []
            #adds this play record to the list for this video_id
            self._play_history[video_id].append(play_record)
            #returns true
            return True

    #defines a function called get_plays
    def get_plays(self, video_id: int) -> list:
        """gets a list of all the users play records for a specific video_id

        Args:
            video_id (int): The video id of the video_id the user wants to search for

        Returns:
            The plays list created of all the play records for the video
        """
        #creates an empty list called plays
        plays = []
        #validates that the video_id is valid (above 0)
        if video_id <= 0:
            #lets the user know if it isnt valid
            print("Invalid video ID entered")
            #returns the empty list
            return plays
        #if the video_id exists in the play history dictionary
        if video_id in self._play_history:
            #gets the list of play records for this video_id
            plays = self._play_history[video_id]
        #returns the list
        return plays

    @staticmethod
    def validate_password(password: str) -> bool:
        """Validates if the password entered has at least 8 characters, has a digit and has an uppercase and lowercase

        Args:
            password (str | None): the password that hs been entered

        Returns:
            True if password meets all criteria, False otherwise
        """
        if password is None:
            return False

        if len(password) < 8:
            return False

        upper_check = any((c.isupper() for c in password))
        if not upper_check:
            print("No uppercase letters included")
            return False

        lower_check = any((c.islower() for c in password))
        if not lower_check:
            print("No lowercase letters included")
            return False

        digit_check = any((c.isdigit() for c in password))
        if not digit_check:
            print("No digits included")
            return False

        return True

    def change_password(self, username: str, old_pass: str, new_pass: str) -> bool:
        """Changes the users current password

        Args:
            username (str): The current username
            old_pass (str): The users current password
            new_pass (str): The password the user wants to change to

        Returns:
            True if old password is equal to current password and if new password passes validation , False otherwise
        """
        if username is None:
            print("Username cannot be None")
            return False
        if old_pass is None:
            print("Old password cannot be None")
            return False
        if new_pass is None:
            print("New password cannot be None")
            return False

        if len(username.strip()) == 0:
            print("Username cannot be empty")
            return False

        if username != self._username:
            print("Invalid username entered")
            return False

        if old_pass != self.__password:
            print("New password must not contain the username")
            return False

        if not User.validate_password(new_pass):
            print("Password entered does not meet the requirements")
            return False

        return True

    @staticmethod
    def validate_username(username: str) -> bool:
        """Validates if the username entered is empty or not

        Args:
            username (str | None): the password that hs been entered

        Returns:
            True if password meets all criteria, False otherwise
            """
        if not username:
            return False

        return True
