"""Configuration definitions for application settings.

This module defines all available configuration options and their defaults.
Add new settings by adding new fields with type hints and Field definitions.
"""

from pydantic import BaseModel, Field
from enum import Enum


class LogLevel(str, Enum):
    """Valid log levels."""

    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'


class AppSettings(BaseModel):
    """Application configuration structure.

    Add new settings as needed by adding new fields with type hints
    and Field definitions.
    """

    # Application settings
    log_level: LogLevel = Field(default=LogLevel.INFO, description='Application logging level')