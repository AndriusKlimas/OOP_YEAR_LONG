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
