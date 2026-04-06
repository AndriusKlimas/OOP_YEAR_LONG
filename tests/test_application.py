import pytest

from application import *

class TestAndriusCode:
    def test_admin_check_returns_true(self):
        """Test checking admin user"""
        result = admin_check("admin")
        assert result is True

    def test_admin_check_returns_false(self):
        """Test checking admin user"""
        result = admin_check("lulu")
        assert result is False

    def test_admin_check_num_returns_false(self):
        """Test checking admin user"""
        result = admin_check(123)
        assert result is False

    @pytest.fixture
    def videos(self):
        """Sample videos dictionary"""
        v1 = Video(1, "Inception", "A mind-bending thriller", 8880, 2010, ["scifi", "thriller"])
        v2 = Video(2, "The Matrix", "A hacker discovers reality", 8160, 1999, ["scifi", "action"])
        v3 = Video(3, "Toy Story", "Toys come to life", 4860, 1995, ["animation", "comedy"])
        v4 = Video(4, "Inception", "Different version", 9000, 2010, ["scifi", "thriller"])

        return {
            "Inception": [v1, v4],
            "The Matrix": [v2],
            "Toy Story": [v3]
        }

    def test_video_search_found(self, videos):
        """Test finding a video"""
        result = video_search(videos, "Inception")
        assert result is not None








class TestNoahCode:
    def test_sec_to_min_basic_conversion(self):
        """Test basic conversion of seconds to minutes and seconds"""
        result = sec_to_min(120)
        assert result == "2 minutes and 0 seconds"

    def test_sec_to_min_zero_success(self):
        result = sec_to_min(0)

        assert result == "0 minutes and 0 seconds"

    def test_sec_to_min_exact_minute_success(self):
        result = sec_to_min(180)

        assert result == "3 minutes and 0 seconds"

    def test_parse_videos_reads_project_file(self):
        """Use existing videos.json from project"""
        videos = parse_videos("videos.json")

        assert isinstance(videos, dict)
        assert len(videos) > 0

        # check first video object has expected methods
        first_title = list(videos.keys())[0]
        first_video = videos[first_title][0]
        assert first_video.get_title() == first_title

    def test_parse_users_reads_project_file(self):
        """Use existing users.json from project"""
        users = parse_users("users.json")

        assert isinstance(users, list)
        assert len(users) > 0

        # check first user object has expected method
        first_user = users[0]
        assert first_user.get_username() is not None


    def test_create_default_videos_returns_dict(self):
        """Test default videos creation"""
        videos = create_default_videos()

        assert isinstance(videos, dict)

    def test_create_default_videos_contains_expected_titles(self):
        videos = create_default_videos()

        assert "Inception" in videos
        assert "The Matrix" in videos
        assert "The Godfather" in videos
        assert "Toy Story" in videos
        assert "Up" in videos

    def test_create_default_videos_up_has_two_records(self):
        videos = create_default_videos()

        assert len(videos["Up"]) == 2


    def test_create_default_users_returns_dict(self):
        """Test default users creation"""
        users = create_default_users()

        assert isinstance(users, dict)

    def test_create_default_users_contains_expected_users(self):
        users = create_default_users()

        assert "NoahClarke123" in users
        assert "Film_Critic1" in users
        assert "Bob_iscool" in users
        assert "Jedibob212" in users
        assert "IronManFan3" in users
        assert "admin" in users

    def test_create_default_users_values_are_user_objects(self):
        users = create_default_users()

        for username, user in users.items():
            assert user.get_username() == username

    def test_create_default_users_has_seeded_play_history(self):
        users = create_default_users()

        noah_history = users["NoahClarke123"].get_history()
        assert 1 in noah_history
        assert 4 in noah_history
        assert len(noah_history[1]) >= 1
        assert len(noah_history[4]) >= 1

