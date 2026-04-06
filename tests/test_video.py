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
        assert video.get_title() != "The"

    def test_get_description(self):
        """Test the get_description() method"""
        video = Video(2, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])

        assert video.get_description() == "A hacker discovers reality"
        assert video.get_description() != "A hacker"

    def test_get_video_id(self):
        """Test the get_video_id() method"""
        video = Video(2, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])

        assert video.get_video_id() == 2
        assert video.get_video_id() != 4

    def test_get_duration_seconds(self):
        """Test the get_duration_seconds() method"""
        video = Video(2, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])

        assert video.get_duration_seconds() == 8160
        assert video.get_duration_seconds() != 8880

    def test_get_release_year(self):
        """Test the get_release_year() method"""
        video = Video(2, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])

        assert video.get_release_year() == 1999
        assert video.get_release_year() != 1900

    def test_get_genres(self):
        """Test the get_genres() method"""
        video = Video(2, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])

        assert video.get_genres() == ["scifi", "action"]
        assert video.get_genres() != ["scifi", "a"]



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
        video = Video(1, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
        result = video.check_genre("fake_genre")

        assert result is False

    def test_check_genre_empty_genres(self):
        """Test checking genre when video has no genres"""
        video = Video(1, "The Matrix", "A hacker discovers reality", 8160, 1999, [])
        result = video.check_genre("action")

        assert result is False

    def test_check_genre_multiple_genres(self):
        """Test checking different genres in a video with multiple genres"""
        video = Video(1, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action", "thriller"])

        assert video.check_genre("scifi") is True
        assert video.check_genre("action") is True
        assert video.check_genre("thriller") is True
        assert video.check_genre("comedy") is False

    def test_check_genre_with_spaces(self):
        """Test checking genre with whitespace"""
        video = Video(1, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
        result = video.check_genre("  action  ")

        assert result is True

class TestValidationReturnValidGenre:
    def test_return_valid_genres_is_copy(self):
        """Test that return_valid_genres() returns a copy, not the original"""
        result1 = Video.return_valid_genres()
        result2 = Video.return_valid_genres()

        # Modify one and check the other isn't affected
        result1.append("fake_genre")

        assert "fake_genre" not in result2
        assert len(result2) == 10


class TestValidateGenre:
    """Test the validate_genre() static method"""

    def test_validate_genre_valid_genre(self):
        """Test validating a valid genre"""
        result = Video.validate_genre("action")
        assert result is True

    def test_validate_genre_valid_genre_uppercase(self):
        """Test validating a valid genre with uppercase"""
        result = Video.validate_genre("ACTION")
        assert result is True

    def test_validate_genre_valid_genre_mixed_case(self):
        """Test validating a valid genre with mixed case"""
        result = Video.validate_genre("CoMeDy")
        assert result is True

    def test_validate_genre_invalid_genre(self):
        """Test validating an invalid genre"""
        result = Video.validate_genre("fake_genre")
        assert result is False

    def test_validate_genre_all_valid_genres(self):
        """Test all valid genres return True"""
        valid_genres = ["action", "comedy", "drama", "horror", "romance", "scifi", "documentary", "animation",
                        "thriller", "crime"]

        for genre in valid_genres:
            result = Video.validate_genre(genre)
            assert result is True

    def test_validate_genre_non_string_returns_false(self):
        """Test that non-string input returns False"""
        result = Video.validate_genre(123)
        assert result is False

    def test_validate_genre_with_spaces(self):
        """Test validating genre with leading/trailing spaces"""
        result = Video.validate_genre("  action  ")
        assert result is True

    def test_validate_genre_none_returns_false(self):
        """Test that None returns False"""
        result = Video.validate_genre(None)
        assert result is False

    def test_validate_genre_empty_string_returns_false(self):
        """Test that empty string returns False"""
        result = Video.validate_genre("")
        assert result is False


class TestValidateId:
    """Test the validate_id() static method"""

    def test_validate_id_valid_positive(self):
        """Test validating a valid positive video ID"""
        result = Video.validate_id(1)
        assert result is True

    def test_validate_id_valid_zero(self):
        """Test validating zero as a valid video ID"""
        result = Video.validate_id(0)
        assert result is True

    def test_validate_id_valid_large_number(self):
        """Test validating a large positive video ID"""
        result = Video.validate_id(999999)
        assert result is True

    def test_validate_id_negative_returns_false(self):
        """Test that negative video ID returns False"""
        result = Video.validate_id(-1)
        assert result is False

    def test_validate_id_none_returns_false(self):
        """Test that None returns False"""
        result = Video.validate_id(None)
        assert result is False

    def test_validate_id_string_returns_false(self):
        """Test that string input returns False"""
        result = Video.validate_id("123")
        assert result is False

    def test_validate_id_float_returns_false(self):
        """Test that float input returns False"""
        result = Video.validate_id(123.5)
        assert result is False

class TestValidateTitle:
    """Test the validate_title() static method"""
    def test_validate_title_valid(self):
        """Test validating a valid title"""
        result = Video.validate_title("example")
        assert result is True

    def test_validate_title_num_return_false(self):
        """Test that number input returns False """
        result = Video.validate_title(123)
        assert result is False

    def test_validate_title_none_returns_false(self):
        """Test that None returns False"""
        result = Video.validate_title(None)
        assert result is False

    def test_validate_title_empty_string_returns_false(self):
        """Test that empty string returns False"""
        result = Video.validate_title("")
        assert result is False

    def test_validate_title_whitespace_returns_true(self):
        """Test that whitespace string returns True"""
        result = Video.validate_title(" example ")
        assert result is True

class TestValidateDescription:
    """Test the validate_description() static method"""
    def test_validate_description_valid(self):
        """Test validating a valid title"""
        result = Video.validate_description("example")
        assert result is True

    def test_validate_description_none_returns_false(self):
        """Test that None returns False"""
        result = Video.validate_description(None)
        assert result is False

    def test_validate_description_num_return_false(self):
        """Test that number input returns False"""
        result = Video.validate_description(123)
        assert result is False

    def test_validate_description_empty_string_returns_false(self):
        """Test that empty string returns False"""
        result = Video.validate_description("")
        assert result is False

class TestValidateDuration:
    """Test the validate_duration_seconds() static method"""
    def test_validate_duration_valid(self):
        """Test validating a valid duration"""
        result = Video.validate_duration_seconds(123)
        assert result is True

    def test_validate_duration_none_returns_false(self):
        """Test that None returns False"""
        result = Video.validate_duration_seconds(None)
        assert result is False

    def test_validate_duration_string_return_false(self):
        """Test that string input returns False"""
        result = Video.validate_duration_seconds("eepy")
        assert result is False

    def test_validate_duration_negative_returns_false(self):
        """Test that negative duration returns False"""
        result = Video.validate_duration_seconds(-123)
        assert result is False
