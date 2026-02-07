"""
ConfigManager Singleton

This Singleton ensures a single instance of ConfigManager is used throughout 
the application, centralizing configuration settings.
"""


class ConfigManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConfigManager, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.settings = {
            "DEFAULT_TASK_PRIORITY": "Medium",
            "ENABLE_NOTIFICATIONS": True,
            "RATE_LIMIT": 50
        }

    def get_setting(self, key):
        """Get a configuration setting by key."""
        return self.settings.get(key)

    def set_setting(self, key, value):
        """Set a configuration setting."""
        self.settings[key] = value

    def get_all_settings(self):
        """Return all configuration settings."""
        return self.settings.copy()
