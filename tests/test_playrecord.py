import pytest
from user_records import PlayRecord

class TestPlayRecordCreation:
    """Test play record object creation"""

    def test_playrecord_creation(self):
        playrecord = PlayRecord("NoahClarke123", 10, 25)

        assert playrecord.get_username() == "NoahClarke123"
        assert playrecord.get_video_id() == 10
        assert playrecord.get_pos() == 25
        assert playrecord.get_play_id() > 0

class TestPlayRecordRetrieval:
    """Test play record object retrieval"""

    def test_get_username(self):
        playrecord = PlayRecord("NoahClarke123", 10, 25)

        assert playrecord.get_username() == "NoahClarke123"
        assert playrecord.get_username() != "NoahClarke234"

    def test_get_video_id(self):
        playrecord = PlayRecord("NoahClarke123", 10, 25)

        assert playrecord.get_video_id() == 10
        assert playrecord.get_video_id() != 11

    def test_get_pos(self):
        playrecord = PlayRecord("NoahClarke123", 10, 25)

        assert playrecord.get_pos() == 25
        assert playrecord.get_pos() != 30

class TestValidateUsername:
    """Test username validation for PlayRecord"""

    def test_validate_username_valid_success(self):
        assert PlayRecord.validate_username("NoahClarke123") is True

    def test_validate_username_none_fail(self):
        assert PlayRecord.validate_username(None) is False

class TestValidateVideoID:
    """Test video ID validation for PlayRecord"""

    def test_validate_video_id_valid_success(self):
        assert PlayRecord.validate_video_id(10) is True

    def test_validate_video_id_zero_valid_success(self):
        assert PlayRecord.validate_video_id(0) is True

    def test_validate_video_id_negative_fail(self):
        assert PlayRecord.validate_video_id(-1) is False

    def test_validate_video_id_none_fail(self):
        assert PlayRecord.validate_video_id(None) is False



