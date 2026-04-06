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

class TestChangePassword:
    """Test changing a user's password"""

    def test_change_password_valid_success(self):
        user = User("NoahClarke123", "Password123!")

        result = user.change_password("NoahClarke123", "Password123!", "NewPass123!")

        assert result is True
        assert user.get_password() == "Password123!"

    def test_change_password_invalid_username_fail(self):
        user = User("NoahClarke123", "Password123!")

        result = user.change_password("WrongUser", "Password123!", "NewPass123!")

        assert result is False
        assert user.get_password() == "Password123!"

    def test_change_password_wrong_old_password_fail(self):
        user = User("NoahClarke123", "Password123!")

        result = user.change_password("NoahClarke123", "WrongPass123!", "NewPass123!")

        assert result is False
        assert user.get_password() == "Password123!"

    def test_change_password_invalid_new_password_fail(self):
        user = User("NoahClarke123", "Password123!")

        result = user.change_password("NoahClarke123", "Password123!", "short")

        assert result is False
        assert user.get_password() == "Password123!"

class TestValidatePassword:
    """Test password validation"""

    def test_validate_password_valid_success(self):
        assert User.validate_password("Password123!") is True

    def test_validate_password_too_short_fail(self):
        assert User.validate_password("Pw1") is False

    def test_validate_password_no_uppercase_fail(self):
        assert User.validate_password("password123!") is False

    def test_validate_password_no_lowercase_fail(self):
        assert User.validate_password("PASSWORD123!") is False

    def test_validate_password_no_digit_fail(self):
        assert User.validate_password("Password!!!") is False

class TestValidateUsername:
    """Test username validation"""

    def test_validate_username_valid_success(self):
        assert User.validate_username("NoahClarke123") is True

    def test_validate_username_empty_fail(self):
        assert User.validate_username("") is False

    def test_validate_username_none_fail(self):
        assert User.validate_username(None) is False