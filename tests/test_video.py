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

    def test_get_title(self):
        """Test the get_title() method"""
        video = Video(2, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])

        assert video.get_title() == "The Matrix"

    def test_get_description(self):
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


