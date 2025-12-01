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
                return "Please enter a valid format"

    def __eq__(self, other: "User"):
        if not other:
            return False
        return self._username == other._username

    def __ne__(self, other: "User"):
        if self == other:
            return False
        else:
            return True

    def start_play(self, video_id: int):
