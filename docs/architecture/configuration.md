# Configuration System

The template includes a robust configuration system that handles loading settings from multiple sources with clear precedence rules. This page explains how the configuration system works and how to use it effectively.

## Overview

The configuration system has two main components:

1. **Configuration Definitions** (`config.py`): Defines the structure and default values of all settings
2. **Settings Management** (`settings.py`): Handles loading settings from various sources

This separation allows you to define what settings are available and their types separately from how they are loaded and accessed.

## Configuration Definitions

Settings are defined using Pydantic models, which provide type checking and validation:

```python
# config.py
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
    """Application configuration structure."""
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
```

### Adding New Settings

To add a new setting:

1. Add a new field to the `AppSettings` class
2. Specify its type
3. Add a `Field` with a default value and description
4. Update documentation as needed

For example, to add a new setting for maximum items per page:

```python
max_items_per_page: int = Field(
    default=100,
    description="Maximum number of items to return per page"
)
```

## Settings Management

The settings management system handles loading settings from various sources with a clear precedence order:

1. Direct overrides (highest precedence)
2. Environment variables
3. `.env` file values
4. Default values (lowest precedence)

```python
# settings.py (simplified)
class Settings:
    """Settings singleton with configuration loading capabilities."""
    
    _instance = None
    
    def __init__(self):
        self._settings = None
        self._env_prefix = "MYAPP_"
    
    @classmethod
    def get_instance(cls, env_file=None, **kwargs):
        """Get or create settings instance."""
        if cls._instance is None:
            cls._instance = cls()
            cls._instance._initialize(env_file=env_file, **kwargs)
        return cls._instance

    def _initialize(self, env_file=None, **kwargs):
        """Initialize settings from all sources in order of precedence."""
        config = {}
        
        # 1. Load .env file values
        if env_file and Path(env_file).exists():
            env_values = dotenv_values(env_file)
            # Process env values...
        
        # 2. Load environment variables
        for key, value in os.environ.items():
            if key.startswith(self._env_prefix):
                # Process environment variables...
        
        # 3. Apply direct overrides
        config.update(kwargs)
        
        # Create settings instance
        self._settings = AppSettings(**config)

    def __getattr__(self, name):
        """Delegate attribute access to settings instance."""
        if self._settings is None:
            raise RuntimeError("Settings not initialized")
        return getattr(self._settings, name)
```

### Using Settings

To access settings in your code:

```python
from src.package_name.core.settings import get_settings

# Get settings with defaults
settings = get_settings()
print(settings.database_url)  # sqlite:///app.db

# Override settings directly
settings = get_settings(database_url="postgresql://user:pass@localhost/db")
print(settings.database_url)  # postgresql://user:pass@localhost/db
```

### Environment Variables

Environment variables are prefixed with the project's environment prefix (set during initialization) to avoid conflicts with other applications:

```
# .env file
MYAPP_DATABASE_URL=postgresql://user:pass@localhost/db
MYAPP_DEBUG=true
MYAPP_LOG_LEVEL=DEBUG
```

Or set directly in the environment:

```bash
export MYAPP_DATABASE_URL=postgresql://user:pass@localhost/db
export MYAPP_DEBUG=true
export MYAPP_LOG_LEVEL=DEBUG
```

### Environment Prefix

The environment prefix is set during project initialization:

```
What would you like the environment variable prefix for your project to be?
```

This prefix is used for all environment variables to avoid conflicts with other applications. For example, if your prefix is `MYAPP_`, then the database URL environment variable would be `MYAPP_DATABASE_URL`.

## Configuration Validation

The configuration system validates all settings when they are loaded:

1. Type validation: Ensures values match their specified types
2. Enum validation: Ensures values for enums are valid
3. Custom validation: Additional validation logic can be added

If validation fails, an error is raised with details about the validation issue.

## Best Practices

1. **Keep settings minimal**: Only add settings that might need to change across environments
2. **Use descriptive names**: Make setting names clear and descriptive
3. **Add documentation**: Document each setting with a clear description
4. **Set sensible defaults**: Default values should work for local development
5. **Use environment variables for sensitive values**: Don't hardcode secrets
6. **Validate settings early**: Check for required settings at startup

## Example: Adding Custom Validation

You can add custom validation logic to your settings:

```python
from pydantic import BaseModel, Field, validator

class AppSettings(BaseModel):
    # ... existing settings ...
    
    max_connections: int = Field(
        default=100,
        description="Maximum number of database connections"
    )
    
    @validator("max_connections")
    def check_max_connections(cls, v):
        if v < 1:
            raise ValueError("max_connections must be at least 1")
        if v > 1000:
            raise ValueError("max_connections cannot exceed 1000")
        return v
```

## Example: Environment-Specific Settings

You can use different `.env` files for different environments:

```bash
# Development
get_settings(env_file=".env.dev")

# Testing
get_settings(env_file=".env.test")

# Production
get_settings(env_file=".env.prod")
```

This approach allows you to maintain different configurations for different environments while using the same code.
