class Video:
    VALID_GENRES = ['Action', 'Comedy', 'Drama', 'Horror', 'Romance', 'Sci-Fi', 'Documentary']

    def __init__(self, _video_id : int, title:str, description:str, _duration_seconds:int, _release_year:int, _genres:list = []):
        self.genres = _genres
        self._video_id = _video_id
        self.title = title
        self.description = description
        self._duration_seconds = _duration_seconds
        self._release_year = _release_year

    # def check_genre(self, genre:str) -> bool:
    @staticmethod
    def return_valid_genres() -> list:
        return list(Video.VALID_GENRES)


    def add_genre(self, genre:str) -> bool:
        if genre not in self.genres and genre in Video.VALID_GENRES:
            self.genres.append(genre)
            return True
        else:
            return False