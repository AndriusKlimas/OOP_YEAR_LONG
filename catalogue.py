class Video:
    valid_genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Romance', 'Sci-Fi', 'Documentary']

    def __init__(self, _video_id : int, title:str, description:str, _duration_seconds:int, _release_year:int, _genres:list = []):
        self.genres = _genres
        self._video_id = _video_id
        self.title = title
        self.description = description
        self._duration_seconds = _duration_seconds
        self._release_year = _release_year

    # def check_genre(self, genre:str) -> bool:
    @staticmethod
