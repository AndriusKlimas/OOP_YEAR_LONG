from abc import ABC, abstractmethod
from catalogue import Video
import json
import logging

from video_serivice import VideoService

logger = logging.getLogger(__name__)


class JSONVideoDataAccess():
