from __future__ import annotations

class PlayRecord:

    record_counter: int = 1

    def __init__(self, username: str, video_id: int, position_in_seconds: int):
        self._play_id = PlayRecord.record_counter
        self._username = username
        self._video_id = video_id
        self._position_in_seconds = position_in_seconds

        PlayRecord.record_counter += 1

    def __str__(self):
        return f"Username: {self.get_username()} Position in Seconds: {self.get_pos()}"

    def __repr__(self):
        return f"{self.__class__.__name__} Play ID: {self.get_play_id()} Username: {self.get_username()} Video ID: {self.get_video_id()} Position in Seconds: {self.get_pos()} "

    def __eq__(self, other: object) -> bool | NotImplemented:
        if not isinstance(other, User):
            return NotImplemented

        return self._username == other._username

    def __ne__(self, other: object) -> bool | NotImplemented:
        if not isinstance(other, User):
            return True

    def get_play_id(self) -> int:
        return self._play_id

    def get_video_id(self) -> int:
        return self._video_id

    def get_username(self) -> str:
        return self._username

    def get_pos(self) -> int:
        return self._position_in_seconds


class User:
    _play_history = {}

    def __init__(self, username: str, password: str):
        self._username = username
        self.__password = password

    def get_username(self):
        return self._username

    def __str__(self):
        return f"Username: {self.get_username()} Password = ********"

    def __repr__(self):
        return f"{self.__class__.__name__}\nUsername: {self.get_username()}\nPassword: ********"

    def __format__(self, format_spec: str):
        match format_spec:
            case "short":
                return f"Username: {self.get_username()}"
            case "long":
                return f"Username: {self.get_username()} Password: ********"
            case _:
                print("Invalid option selected")
                return repr(self)

    def __eq__(self, other: object) -> bool | NotImplemented:
        if not isinstance(other, User):
            return NotImplemented

        return self._username == other._username

    def __ne__(self, other: object) -> bool | NotImplemented:
        if not isinstance(other, User):
            return True

        return self._username != other._username

    #defines a function called start_play which takes in self, video_id and position in seconds as pos
    def start_play(self, video_id: int, pos: int = 0):
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
        if old_pass != self.__password:
            print("Password entered does not match current password")
            return False

        if not User.validate_password(new_pass):
            print("Password entered does not meet the requirements")
            return False

        self.__password = new_pass
        return True