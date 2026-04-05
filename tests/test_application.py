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