from user_records import *
import pytest

class TestUserCreation:
    """Test user object creation"""
    def test_user_creation(self):
        user = User("NoahClarke123", "Password123!")

        assert user.get_username() == "NoahClarke123"
        assert user.get_password() == "Password123!"

    # No tests for the failed validation situations in User creation

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
        # No assert for PlayRecord id
        assert plays[0].get_username() == "NoahClarke123"
        assert plays[0].get_video_id() == 10
        assert plays[0].get_pos() == 25

    def test_start_play_invalid_video_id_fail(self):
        user = User("NoahClarke123", "Password123!")

        result = user.start_play(0, 25)

        assert result is False

        # This assert looks to be getting a different id to what you've (intentionally) failed to start playing.
        # This means the assert isn't really doing much here - the data isn't relevant. You're right that you can't
        # just use get_plays() to get the value (because of the validation) but if you got a copy of the play_records
        # dictionary, you can check that it doesn't have any list for video_id = 0
        assert user.get_plays(1) == []

    def test_start_play_invalid_position_fail(self):
        user = User("NoahClarke123", "Password123!")

        result = user.start_play(10, -1)

        assert result is False
        # This version makes sense as it's looking for the same video_id that you attempted to play
        assert user.get_plays(10) == []

    # Another test that could be included is does the method add a new play record to an *existing* list - you know there
    # are records for video_id 10, so you start a new play on that video and confirm that you now have two play records for that id.

class TestGetPlays:
    """Test getting plays for a user"""

    def test_get_plays_valid_success(self):
        user = User("NoahClarke123", "Password123!")
        user.start_play(10, 25)
        user.start_play(10, 40)
        user.start_play(11, 5)

        plays = user.get_plays(10)

        assert len(plays) == 2
        # The asserts should be confirming all parts are correct - check the id and the position are correct in both entries
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
    # These are good candidates for parameterised testing - the logic of the tests is consistent across all cases,
    # the only thing that changes is the data for the test input and expected result
    def test_change_password_valid_success(self):
        user = User("NoahClarke123", "Password123!")

        result = user.change_password("NoahClarke123", "Password123!", "NewPass123!")

        assert result is True
        # This is the original password again - I'm not sure if the test is written this way because of an oversight,
        # or because the underlying logic is broken (it never actually changes the password) and you wanted the test to pass
        assert user.get_password() == "Password123!"

    def test_change_password_invalid_username_fail(self):
        user = User("NoahClarke123", "Password123!")

        result = user.change_password("WrongUser", "Password123!", "NewPass123!")

        # These are good asserts for this situation
        assert result is False
        assert user.get_password() == "Password123!"

    def test_change_password_wrong_old_password_fail(self):
        user = User("NoahClarke123", "Password123!")

        result = user.change_password("NoahClarke123", "WrongPass123!", "NewPass123!")

        # Good asserts
        assert result is False
        assert user.get_password() == "Password123!"

    def test_change_password_invalid_new_password_fail(self):
        user = User("NoahClarke123", "Password123!")

        result = user.change_password("NoahClarke123", "Password123!", "short")

        assert result is False
        assert user.get_password() == "Password123!"

    # Another test you could include would be to investigate the case-insensitivity of the username (the case of the
    # username should not matter)

class TestValidatePassword:
    """Test password validation"""
    # These are a good example of where to use parameterised testing - it would mean writing one test and running it
    # with 5 sets of parameters as the test logic is identical for all test cases.
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
    # Parameterised tests would be useful here
    def test_validate_username_valid_success(self):
        assert User.validate_username("NoahClarke123") is True

    def test_validate_username_empty_fail(self):
        assert User.validate_username("") is False

    def test_validate_username_none_fail(self):
        assert User.validate_username(None) is False

class TestValidateLogin:
    # These tests are good, but they're highlighting a problem with the code that wasn't repaired - the highlighting
    # of the users dictionary says it's the wrong type as it was expecting a dictionary of str: str, but you have str:User here

    """Test login validation"""

    def test_validate_login_valid_success(self):
        user = User("NoahClarke123", "Password123!")
        users = {"NoahClarke123": user}

        result = User.validate_login(users, "NoahClarke123", "Password123!")

        assert result == user

    def test_validate_login_wrong_password_fail(self):
        user = User("NoahClarke123", "Password123!")
        users = {"NoahClarke123": user}

        result = User.validate_login(users, "NoahClarke123", "WrongPass123!")

        assert result is None

    def test_validate_login_unknown_username_fail(self):
        user = User("NoahClarke123", "Password123!")
        users = {"NoahClarke123": user}

        result = User.validate_login(users, "OtherUser", "Password123!")

        assert result is None

class TestBetterPractice:
    # You have correctly separated the test cases across separate methods rather than clumping them together - good job!
    """Test rich comparison and hashing behaviors for User"""

    # Parameterization would save a lot of repetition here
    def test_eq_same_username_true(self):
        user1 = User("anna", "Password123")
        user2 = User("anna", "Different123")

        assert user1 == user2

    def test_eq_different_username_false(self):
        user1 = User("anna", "Password123")
        user2 = User("ben", "Password123")

        assert (user1 == user2) is False

    # No test for comparing users with the same username in different cases

    def test_ne_same_username_false(self):
        user1 = User("anna", "Password123")
        user2 = User("anna", "Different123")

        assert (user1 != user2) is False

    def test_ne_different_username_true(self):
        user1 = User("anna", "Password123")
        user2 = User("ben", "Password123")

        assert user1 != user2

    def test_lt_username_ordering(self):
        user1 = User("anna", "Password123")
        user2 = User("ben", "Password123")

        assert user1 < user2
        assert (user2 < user1) is False

    def test_total_ordering_le_gt_ge(self):
        user1 = User("anna", "Password123")
        user2 = User("anna", "Different123")
        user3 = User("ben", "Password123")

        # These should have been done separately, as they are their own individual test cases
        assert user1 <= user2
        assert user3 > user1
        assert user3 >= user1

    def test_hash_uses_username(self):
        user1 = User("anna", "Password123")
        user2 = User("anna", "Different123")
        user3 = User("ben", "Password123")

        # These should have been separate test methods as they are their own individual test cases
        assert hash(user1) == hash(user2)
        assert hash(user1) != hash(user3)

    def test_str_masks_password_and_shows_username(self):
        user = User("anna", "Password123")

        result = str(user)

        assert "Username: anna" in result
        assert "Password = ********" in result
        # VERY GOOD!!
        assert "Password123" not in result

    def test_repr_includes_class_username_and_masked_password(self):
        user = User("anna", "Password123")

        result = repr(user)

        assert "User" in result
        assert "Username: anna" in result
        assert "Password: ********" in result
        assert "Password123" not in result

class TestUserFromDict:
    """Test the from_dict() method"""

    def test_from_dict_valid_data(self):
        """Test creating user from valid dictionary"""
        data = {"username": "Noah", "password": "Password123!"}

        user = User.from_dict(data)
        assert user.get_username() == "Noah"
        assert user.get_password() == "Password123!"

    def test_from_dict_invalid_username(self):
        """Test creating user from invalid username"""
        data = {"username": None, "password": "Password123!"}

        with pytest.raises(InvalidUserError):
            User.from_dict(data)

    def test_from_dict_invalid_password(self):
        """Test creating user from invalid password"""
        data = {"username": "Noah", "password": "Test"}

        with pytest.raises(InvalidUserError):
            User.from_dict(data)

    # No test for where the field is missing - that test is pretty important as deserialisation must be robust

class TestUserToDict:
    """Test the to_dict() method"""

    def test_to_dict_returns_dict(self):
        """Test to_dict() returns dictionary"""
        data = User("Noah", "Password123!")
        result = data.to_dict()
        assert isinstance(result, dict)

    def test_to_dict_contains_all_fields(self):
        """Test to_dict contains all required fields"""
        data = User("Noah", "Password123!")
        result = data.to_dict()

        assert "username" in result
        assert "password" in result
        # No check for the type information in the dictionary

    def test_to_dict_correct_values(self):
        """Test to_dict() returns correct values"""
        data = User("Noah", "Password123!")
        result = data.to_dict()

        assert result["username"] == "Noah"
        assert result["password"] == "Password123!"