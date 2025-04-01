from abc import ABC, abstractmethod
from typing import Dict, Optional

class AliasClientInterface(ABC):
    @abstractmethod
    def list_aliases(self) -> Dict:
        """Get all aliases."""
        pass

    @abstractmethod
    def get_alias(self, index: str) -> Dict:
        """Get aliases for the specified index or all indices."""
        pass
    
    @abstractmethod
    def put_alias(self, index: str, name: str, body: Dict) -> Dict:
        """Creates or updates an alias for the specified index."""
        pass
    
    @abstractmethod
    def delete_alias(self, index: str, name: str) -> Dict:
        """Delete an alias for the specified index."""
        pass
