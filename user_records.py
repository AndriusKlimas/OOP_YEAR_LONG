from __future__ import annotations

class PlayRecord:

    record_counter: int = 1

    def __init__(self, username: str, video_id: int, position_in_seconds: int):
        self._play_id = PlayRecord.record_counter
        self._username = username
        self._video_id = video_id
        self._position_in_seconds = position_in_seconds

        PlayRecord.record_counter += 1

    def __eq__(self, other: object) -> bool | NotImplemented:
        if not isinstance(other, User):
            return NotImplemented

        return self._username == other._username

    def __ne__(self, other: object) -> bool | NotImplemented:
        if not isinstance(other, User):
            return True

    def get_play_id(self):
        return self._play_id




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


    def start_play(self, video_id: int, pos: int = 0):
        if video_id <= 0 or pos < 0:
            return False
        else:
            play_record = PlayRecord(PlayRecord.record_counter, self._username, video_id, pos)
            self._play_history[play_record.get_play_id()] = play_record
            return True
