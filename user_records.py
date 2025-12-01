class User:
    _play_history = {}

    def __init__(self, username: str, password: str):
        self._username = username
        self.__password = password

    def get_username(self):
        return self._username

    def __str__(self):
