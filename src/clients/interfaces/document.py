from abc import ABC, abstractmethod
from typing import Dict, Optional

class DocumentClientInterface(ABC):
    @abstractmethod
    def search_documents(self, index: str, body: Dict) -> Dict:
        """Search for documents."""
        pass
    
    @abstractmethod
    def index_document(self, index: str, document: Dict, id: Optional[str] = None) -> Dict:
        """Creates or updates a document in the index. """
        pass
    
    @abstractmethod
    def get_document(self, index: str, id: str) -> Dict:
        """Get a document by ID."""
        pass
    
    @abstractmethod
    def delete_document(self, index: str, id: str) -> Dict:
        """Delete a document by ID."""
        pass
    
    @abstractmethod
    def delete_by_query(self, index: str, body: Dict) -> Dict:
        """Deletes documents matching the provided query."""
        pass
    
