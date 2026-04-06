import pytest

from application import *

class TestAndriusCode:
    def test_admin_check_is_admin(self):
        """Test checking admin user"""
        result = admin_check("admin")
        assert result is True








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



