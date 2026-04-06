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



