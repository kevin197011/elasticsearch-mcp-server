from abc import ABC, abstractmethod
from typing import Dict, Optional

class IndexClientInterface(ABC):
    @abstractmethod
    def list_indices(self) -> Dict:
        """List all indices."""
        pass

    @abstractmethod
    def get_index(self, index: str) -> Dict:
        """Returns information (mappings, settings, aliases) about one or more indices."""
        pass

    @abstractmethod
    def create_index(self, index: str, body: Optional[Dict] = None) -> Dict:
        """Create a new index."""
        pass
    
    @abstractmethod
    def delete_index(self, index: str) -> Dict:
        """Delete an index."""
        pass
