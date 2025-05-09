"""Configuration definitions for application settings.

This module defines all available configuration options and their defaults.
Add new settings by adding new fields with type hints and Field definitions.
"""

from pydantic import BaseModel, Field, ConfigDict
from typing import Union
from enum import Enum

class LogLevel(str, Enum):
    """Valid log levels."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class AppSettings(BaseModel):
    """Application configuration structure.
    
    These settings match the current defaults and structure.
    Add new settings as needed by adding new fields with type hints
    and Field definitions.
    """
    model_config = ConfigDict(
        frozen=True,
        validate_assignment=True
    )
    
    # Database settings
    database_url: str = Field(
        default="sqlite:///app.db",
        description="Database connection string"
    )
    
    # Application settings
    debug: bool = Field(
        default=False,
        description="Enable debug mode"
    )
    log_level: LogLevel = Field(
        default=LogLevel.INFO,
        description="Application logging level"
    ) 