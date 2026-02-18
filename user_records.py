#imports annotations for type hinting
from __future__ import annotations

from types import NotImplementedType

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

    def __str__(self):
        """ sets up the str method for the playrecord class

        Returns:
            statement including username and position_in_seconds
        """
        return f"Username: {self._username} Position in Seconds: {self.get_pos()}"

    def __repr__(self):
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

    def get_username(self):
        """ gets the username of the user

        Returns:
            username for the user
        """
        return self._username


#creates a class for the Users
class User:

    def __init__(self, username: str, password: str):
        """ sets up the constructor for the user class
        
        Args:
            username (str): The username for the user
            password (str): The password for the user
        """
        self._username = username
        self.__password = password
        self._play_history = {}

    def get_username(self):
        """ gets the username of the user

        Returns:
            username for the user
        """
        return self._username

    def get_history(self):
        """ gets the play history of the user

        Returns:
            dictionary of the play history for that user
        """
        return dict(self._play_history)


    def __str__(self):
        """ sets up the str method for the user class

        Returns:
            statement including username and password (hidden)
        """
        return f"Username: {self._username} Password = ********"

    def __repr__(self):
        """ sets up the repr method for the user class

        Returns:
            statement including class name, username and password (hidden)
        """
        return f"{self.__class__.__name__}\nUsername: {self._username}\nPassword: ********\nPLay History: {self._play_history}"

    def __format__(self, format_spec: str):
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

    def __hash__(self):
        """ Changes the unique identifier for the User class (username) to a number


        Returns:
            hashed version of username
        """
        return hash(self._username)

    #defines a function called start_play which takes in self, video_id and position in seconds as pos
    def start_play(self, video_id: int, pos: int = 0):
        """creates a play record using info from the user class

         Args:
             video_id (int): The video id of the video_id the user wants to watch
             pos (int): The position of the video in seconds

         Returns:
             True if the video id and position are valid, False otherwise
         """

        #validates that the video_id is valid (above 0) and the position in seconds is valid (0 or above)
        if video_id <= 0 or pos < 0:
            #if not, returns false
            return False
        #If hey are both valid
        else:
            #creates a variable called play_record, which is a created play record. takes the username, video id and position in seconds
            play_record = PlayRecord(self._username, video_id, pos)
            #adds this record into the play history dictionary and sets the play_id as the key
            self._play_history[play_record.get_play_id()] = play_record
            #returns true
            return True

    #defines a function called get_plays
    def get_plays(self, video_id: int):
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
        #if it is valid, loops through all of the values of the dictionary
        for p in self._play_history.values():
            #if the video_id supplied mathces a video_id in the dictionary
            if p.get_video_id() == video_id:
                #append the plays list with this entry
                plays.append(p)
        #returns the list
        return plays

    @staticmethod
    def validate_password(password: str):
        """Validates if the password entered has at least 8 characters, has a digit and has an uppercase and lowercase

        Args:
            password (str): the password that hs been entered

        Returns:
            True if password meets all criteria, False otherwise
        """
        if len(password) < 8:
            print("Password must contain at least 8 characters")
            return False

        if not password.isdigit():
            print("Password must contain at least one digit!")
            return False

        if not password.isupper():
            print("Password must contain at least one uppercase!")
            return False

        if not password.islower():
            print("Password must contain at least one lower!")
            return False

        return True

    def change_password(self, old_pass: str, new_pass: str):
        """Changes the users current password

        Args:
            old_pass (str): The users current password
            new_pass (str): The password the user wants to change to

        Returns:
            True if old password is equal to current password and if new password passes validation , False otherwise
        """
        if old_pass != self.__password:
            print("Password entered does not match current password")
            return False

        if not User.validate_password(new_pass):
            print("Password entered does not meet the requirements")
            return False

        self.__password = new_pass
        return True