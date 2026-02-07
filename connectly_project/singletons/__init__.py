# Singletons package for centralized resources
from .config_manager import ConfigManager
from .logger_singleton import LoggerSingleton

__all__ = ['ConfigManager', 'LoggerSingleton']
