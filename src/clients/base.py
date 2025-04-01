"""
Base classes and interfaces for search clients.
"""
from abc import ABC, abstractmethod
import logging
from typing import Dict

class SearchClientBase(ABC):
    """Base abstract class for search clients with common functionality."""
    
    def __init__(self, config: Dict):
        """
        Initialize the base search client.
        
        Args:
            config: Configuration dictionary with connection parameters
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        self.config = config
    
    @abstractmethod
    def close(self):
        """Close the client connection."""
        pass
