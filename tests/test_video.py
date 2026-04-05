import pytest
from catalogue import Video


class TestVideoCreation:
    """Test Video object creation and retrieval"""

    def test_video_creation_success(self):
        """Test creating a valid Video object"""
        video = Video(1, "Inception", "A mind-bending thriller", 8880, 2010, ["scifi", "action"])

        assert video.get_video_id() == 1
        assert video.get_title() == "Inception"
        assert video.get_description() == "A mind-bending thriller"
        assert video.get_duration_seconds() == 8880
        assert video.get_release_year() == 2010
        assert video.get_genres() == ["scifi", "action"]


class TestVideoRetrieval:
    """Test Video object retrieval"""

    def test_get_title(self):
        """Test the get_title() method"""
        video = Video(2, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])

        assert video.get_title() == "The Matrix"

    def test_get_description(self):
        """Test the get_description() method"""
        video = Video(2, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])

        assert video.get_description() == "A hacker discovers reality"

    def test_return_valid_genres_is_copy(self):
        """Test that return_valid_genres() returns a copy, not the original"""
        result1 = Video.return_valid_genres()
        result2 = Video.return_valid_genres()

        # Modify one and check the other isn't affected
        result1.append("fake_genre")

        assert "fake_genre" not in result2
        assert len(result2) == 10


class TestAddGenre:
    """Test adding genres to a video"""
    def test_add_genre_valid_genre_success(self):
        """Test adding a valid genre successfully"""
        video = Video(1, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
        result = video.add_genre("horror")

        assert result is True
        assert "horror" in video.get_genres()

    def test_add_genre_invalid_genre_fail(self):
        """Test adding a valid genre fails"""
        video = Video(1, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
        result = video.add_genre("fake_genre")

        assert result is False
        assert "fake_genre" not in video.get_genres()

    def test_add_genre_duplicate_fails(self):
        """Test adding a duplicate genre"""
        video = Video(1, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
        result = video.add_genre("action")

        assert result is False
        assert video.get_genres() == ["scifi", "action"]

    def test_add_genre_number_fail(self):
        """Test adding a genre number fails"""
        video = Video(1, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
        result = video.add_genre(123)

        assert result is False
        assert 123 not in video.get_genres()

    def test_add_multiple_genres(self):
        """Test adding multiple genres"""
        video = Video(1, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
        result = video.add_genre("horror")
        result_1 = video.add_genre("DramA")

        assert result is True
        assert result_1 is True
        assert "horror" in video.get_genres()
        assert "drama" in video.get_genres()

    def test_add_genre_case_insensitive(self):
        """Test adding a genre case insensitive"""
        video = Video(1, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
        result = video.add_genre("HoRRor")

        assert result is True
        assert "horror" in video.get_genres()

    def test_add_genre_with_whitespace(self):
        """Test adding a genre with whitespace"""
        video = Video(1, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
        result = video.add_genre("  horror  ")

        assert result is True
        assert "horror" in video.get_genres()

class TestCheckGenre:
    """Test checking a genre in the Video object """

    def test_check_genre_exists(self):
        """Test checking a genre in the Video object """
        video = Video(1, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
        result = video.check_genre("action")

        assert result is True

    def test_check_genre_invalid(self):
        """Test checking a genre not in the Video object """
        video = Video(1, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
        result = video.check_genre("horror")

        assert result is False

    def test_check_genre_case_insensitive(self):
        """Test checking if check genre is case insensitive """
        video = Video(1, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
        result = video.check_genre("ActiOn")

        assert result is True

    def test_check_genre_invalid_genre(self):
        """Test checking for an invalid genre"""
        video = Video(4, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
        result = video.check_genre("fake_genre")

        assert result is False

    def test_check_genre_empty_genres(self):
        """Test checking genre when video has no genres"""
        video = Video(5, "The Matrix", "A hacker discovers reality", 8160, 1999, [])
        result = video.check_genre("action")

        assert result is False

    def test_check_genre_multiple_genres(self):
        """Test checking different genres in a video with multiple genres"""
        video = Video(6, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action", "thriller"])

        assert video.check_genre("scifi") is True
        assert video.check_genre("action") is True
        assert video.check_genre("thriller") is True
        assert video.check_genre("comedy") is False

    def test_check_genre_with_spaces(self):
        """Test checking genre with whitespace"""
        video = Video(7, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
        result = video.check_genre("  action  ")

        assert result is True
