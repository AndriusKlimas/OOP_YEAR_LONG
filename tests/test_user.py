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

class TestGetPlays:
    """Test getting plays for a user"""

    def test_get_plays_valid_success(self):
        user = User("NoahClarke123", "Password123!")
        user.start_play(10, 25)
        user.start_play(10, 40)
        user.start_play(11, 5)

        plays = user.get_plays(10)

        assert len(plays) == 2
        assert plays[0].get_video_id() == 10
        assert plays[1].get_pos() == 40

    def test_get_plays_no_history_returns_empty_list(self):
        user = User("NoahClarke123", "Password123!")

        plays = user.get_plays(10)

        assert plays == []

    def test_get_plays_invalid_video_id_returns_empty_list(self):
        user = User("NoahClarke123", "Password123!")

        plays = user.get_plays(0)

        assert plays == []
