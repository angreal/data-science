"""Settings management implementation.

This module handles both the loading of settings from various sources and
providing singleton access to the settings instance.
"""

from typing import Any, Dict, Optional, Union
from pathlib import Path
from dotenv import dotenv_values
import os
import logging

from .config import AppSettings, LogLevel

# Set up logging
logger = logging.getLogger(__name__)


class Settings:
    """Settings singleton with configuration loading capabilities."""

    _instance: Optional['Settings'] = None

    def __init__(self):
        logger.debug('Initializing new Settings instance')
        self._settings: Optional[AppSettings] = None
        self._env_prefix = '{{ environment_prefix }}'

    @classmethod
    def get_instance(cls, env_file: Optional[Union[str, Path]] = None, **kwargs) -> 'Settings':
        """Get or create settings instance."""
        logger.debug(f'get_instance called with kwargs: {kwargs}')

        if cls._instance is None:
            logger.debug('Creating new instance')
            cls._instance = cls()
            cls._instance._initialize(env_file=env_file, **kwargs)
        elif kwargs or env_file:
            raise RuntimeError(
                'Settings already initialized. Cannot modify settings after initialization. '
                'Use Settings.reset() first if you need to create a new settings instance.'
            )
        return cls._instance

    @classmethod
    def reset(cls):
        """Reset settings instance."""
        logger.debug('Resetting Settings instance')
        cls._instance = None

    def _initialize(self, env_file: Optional[Union[str, Path]] = None, **kwargs):
        """Initialize settings from all sources in order of precedence:
        1. Direct overrides (highest precedence)
        2. Environment variables
        3. .env file values
        4. Default values (lowest precedence, from AppSettings class)
        """
        logger.debug('Starting _initialize')

        if self._settings is not None:
            raise RuntimeError('Settings already initialized')

        # Load settings in order of precedence
        config: Dict[str, Any] = {}

        # 1. Load .env file values (third precedence)
        env_path = Path(env_file) if env_file else Path('.env')
        if env_path.exists():
            logger.debug(f'Loading .env file from {env_path}')
            env_values = dotenv_values(str(env_path))
            for key, value in env_values.items():
                if key.startswith(self._env_prefix):
                    config_key = key[len(self._env_prefix) :].lower()
                    if config_key == 'log_level':
                        config[config_key] = LogLevel(value.upper())
                    else:
                        config[config_key] = value
                    logger.debug(f'Added from .env: {key} -> {config_key}={config[config_key]}')

        # 2. Load environment variables (second precedence)
        logger.debug('Loading environment variables')
        for key, value in os.environ.items():
            if key.startswith(self._env_prefix):
                config_key = key[len(self._env_prefix) :].lower()
                if config_key == 'log_level':
                    config[config_key] = LogLevel(value.upper())
                else:
                    config[config_key] = value
                logger.debug(f'Added from environ: {key} -> {config_key}={config[config_key]}')

        # 3. Apply direct overrides (highest precedence)
        logger.debug(f'Applying direct overrides: {kwargs}')
        config.update({k.lower(): v for k, v in kwargs.items()})

        logger.debug(f'Final config before AppSettings creation: {config}')

        try:
            # Create settings instance with collected values
            # Pydantic will automatically use default values from AppSettings
            # for any fields not present in config
            self._settings = AppSettings(**config)
            logger.debug(f'Successfully created AppSettings: {self._settings}')
        except Exception as e:
            logger.error(f'Failed to create AppSettings: {str(e)}')
            self._settings = None
            raise RuntimeError(f'Failed to initialize settings: {str(e)}') from e

    def __getattr__(self, name: str) -> Any:
        """Delegate attribute access to settings instance."""
        logger.debug(f'Getting attribute: {name}')
        if self._settings is None:
            logger.error('Settings accessed before initialization')
            raise RuntimeError('Settings not initialized')
        return getattr(self._settings, name)

    def __setattr__(self, name: str, value: Any) -> None:
        """Prevent modification of settings attributes while allowing internal attributes."""
        if name.startswith('_'):
            # Allow setting private attributes (like _settings, _instance)
            super().__setattr__(name, value)
        else:
            # Prevent setting public attributes
            raise AttributeError(f"Settings are immutable. Can't modify '{name}'")


def get_settings(env_file: Optional[Union[str, Path]] = None, **kwargs) -> Settings:
    """Get settings singleton instance.

    Args:
        env_file: Optional path to .env file. If not provided, defaults to ".env" in current directory
        **kwargs: Override any settings values

    Returns:
        Settings: Validated settings instance

    Example:
        >>> settings = get_settings()
        >>> print(settings.log_level)
        INFO

        >>> settings = get_settings(log_level='DEBUG')
        >>> print(settings.log_level)
        DEBUG
    """
    logger.debug(f'get_settings called with kwargs: {kwargs}')
    return Settings.get_instance(env_file=env_file, **kwargs)