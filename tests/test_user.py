import pytest
from user_records import *

class TestUserCreation:
    """Test user object creation"""
    def test_user_creation(self):
        user = User("NoahClarke123", "Password123!")

        assert user.get_username() == "NoahClarke123"
        assert user.get_password() == "Password123!"

class TestUserRetrieval:
    """Test user object retrieval"""
    def test_get_username(self):
        user = User("NoahClarke123", "Password123!")
        assert user.get_username() == "NoahClarke123"
        assert user.get_username() != "NoahClarke234"

    def test_get_password(self):
        user = User("NoahClarke123", "Password123!")
        assert user.get_password() == "Password123!"
        assert user.get_password() != "Password"

class TestStartPlay:
    """Test starting plays for a user"""

    def test_start_play_valid_success(self):
        user = User("NoahClarke123", "Password123!")

        result = user.start_play(10, 25)

        assert result is True
        plays = user.get_plays(10)
        assert len(plays) == 1
        assert plays[0].get_username() == "NoahClarke123"
        assert plays[0].get_video_id() == 10
        assert plays[0].get_pos() == 25

    def test_start_play_invalid_video_id_fail(self):
        user = User("NoahClarke123", "Password123!")

        result = user.start_play(0, 25)

        assert result is False
        assert user.get_plays(1) == []

    def test_start_play_invalid_position_fail(self):
        user = User("NoahClarke123", "Password123!")

        result = user.start_play(10, -1)

        assert result is False
        assert user.get_plays(10) == []
