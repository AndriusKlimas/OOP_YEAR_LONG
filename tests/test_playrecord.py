import pytest
from user_records import *

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

class TestValidatePositionInSeconds:
    """Test position_in_seconds validation for PlayRecord"""

    def test_validate_position_valid_success(self):
        assert PlayRecord.validate_position_in_seconds(25) is True

    def test_validate_position_zero_valid_success(self):
        assert PlayRecord.validate_position_in_seconds(0) is True

    def test_validate_position_negative_fail(self):
        assert PlayRecord.validate_position_in_seconds(-1) is False

    def test_validate_position_none_fail(self):
        assert PlayRecord.validate_position_in_seconds(None) is False

class TestBetterPractice:
    """Test rich comparison behavior for PlayRecord"""

    def test_eq_same_object_true(self):
        playrecord = PlayRecord("NoahClarke123", 10, 25)

        assert playrecord == playrecord

    def test_eq_different_objects_false(self):
        playrecord1 = PlayRecord("NoahClarke123", 10, 25)
        playrecord2 = PlayRecord("NoahClarke123", 10, 25)

        assert (playrecord1 == playrecord2) is False

    def test_ne_different_objects_true(self):
        playrecord1 = PlayRecord("NoahClarke123", 10, 25)
        playrecord2 = PlayRecord("NoahClarke123", 10, 25)

        assert playrecord1 != playrecord2

    def test_lt_compares_by_play_id(self):
        first = PlayRecord("NoahClarke123", 10, 25)
        second = PlayRecord("NoahClarke123", 10, 30)

        assert first < second
        assert (second < first) is False

    def test_gt_compares_by_play_id(self):
        first = PlayRecord("NoahClarke123", 10, 25)
        second = PlayRecord("NoahClarke123", 10, 30)

        assert second > first
        assert (first > second) is False

    def test_le_compares_by_play_id(self):
        first = PlayRecord("NoahClarke123", 10, 25)
        second = PlayRecord("NoahClarke123", 10, 30)

        assert first <= second
        assert first <= first

    def test_ge_compares_by_play_id(self):
        first = PlayRecord("NoahClarke123", 10, 25)
        second = PlayRecord("NoahClarke123", 10, 30)

        assert second >= first
        assert second >= second

    def test_str_includes_username_and_position(self):
        playrecord = PlayRecord("NoahClarke123", 10, 25)

        result = str(playrecord)

        assert "Username: NoahClarke123" in result
        assert "Position in Seconds: 25" in result

    def test_repr_includes_class_and_key_fields(self):
        playrecord = PlayRecord("NoahClarke123", 10, 25)

        result = repr(playrecord)

        assert "PlayRecord" in result
        assert "Play ID:" in result
        assert "Username: NoahClarke123" in result
        assert "Video ID: 10" in result
        assert "Position in Seconds: 25" in result

class TestPlayRecordFromDict:
    """Test PlayRecord from_dict method"""

    def test_from_dict_valid_data(self):
        """Test creating playrecord from valid dictionary"""
        data = {"username": "Noah", "video_id": 1, "position_in_seconds": 25}

        playrecord = PlayRecord.from_dict(data)
        assert playrecord.get_username() == "Noah"
        assert playrecord.get_video_id() == 1
        assert playrecord.get_pos() == 25

    def test_from_dict_invalid_username(self):
        """Test from_dict raises error for invalid username"""

        data = {"username": None, "video_id": 1, "position_in_seconds": 25}

        with pytest.raises(InvalidPlayRecordError):
            PlayRecord.from_dict(data)

    def test_from_dict_invalid_vidid(self):
        """Test from_dict raises error for invalid video id"""
        data = {"username": "Noah", "video_id": "Test", "position_in_seconds": 25}

        with pytest.raises(ValueError):
            PlayRecord.from_dict(data)

