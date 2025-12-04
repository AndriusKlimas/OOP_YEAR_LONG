class Video:
    #Created a class variable to stare all valid genres
    VALID_GENRES = ["action", "comedy", "drama", "horror", "romance", "scifi", "documentary", "animation", "thriller", "crime"]

    def __init__(self, _video_id : int, title:str, description:str, _duration_seconds:int, _release_year:int, _genres:list = []):
        self._genres = _genres
        self._video_id = _video_id
        self.title = title
        self.description = description
        self._duration_seconds = _duration_seconds
        self._release_year = _release_year

    def get_title(self):
        return self.title

    #Creating a static method
    @staticmethod
    #setting a method called return_valid_genres
    def return_valid_genres() -> list:
        #returning a copy list of all valid genres
        return list(Video.VALID_GENRES)

    #method to add genre
    def add_genre(self, genre:str) -> bool:
        #checking if the genre is not in the video, and if it is in the valid genres
        if genre not in self._genres and genre in Video.VALID_GENRES:
            #adding it to the video if it is not in the list and in valid genres
            self._genres.append(genre.lower())
            #returning TRUE
            return True
        #else
        else:
            #returning FALSE
            return False

    #method to check genre
    def check_genre(self, genre:str) -> bool:
        #checking if the genre is in the video and if it is in the valid genres
        if genre.lower() in self._genres and genre.lower() in Video.VALID_GENRES:
            #returning True
            return True
        #else
        else:
            #Returning false
            return False


    def __str__(self) -> str:
        return f"Title is {self.title} and description is {self.description}, Duration is {self._duration_seconds} seconds, Release year is {self._release_year}. Genres are {', '.join(self._genres)}"

    def __repr__(self) -> str:
        return f"Video_ID: {self._video_id}, Title: {self.title}, Description: {self.description}, Duration: {self._duration_seconds}, Release Year: {self._release_year}, Genres: {self._genres}"

    def __hash__(self) -> int:
        return hash((self._video_id))

    def __format__(self, format_spec: str):
        match format_spec:
            case "short":
                return f"{self.title}, {self._release_year}, {self._duration_seconds} seconds)"
            case "long":
                return f"Title: {self.title}\nDescription: {self.description}\nDuration: {self._duration_seconds} seconds\nRelease Year: {self._release_year}\nGenres: {', '.join(self._genres)}"
            case _:
                return "Please enter a valid format"

