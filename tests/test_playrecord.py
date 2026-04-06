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