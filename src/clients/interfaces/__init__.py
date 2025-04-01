"""
Export all client interfaces and define a combined interface.
"""
from .index import IndexClientInterface
from .document import DocumentClientInterface
from .cluster import ClusterClientInterface
from .alias import AliasClientInterface

class SearchClient(IndexClientInterface, DocumentClientInterface, 
                  ClusterClientInterface, AliasClientInterface):
    """Complete search client interface combining all functionality."""
    
    def close(self):
        """Close the client connection."""
        pass

__all__ = [
    'IndexClientInterface',
    'DocumentClientInterface',
    'ClusterClientInterface',
    'AliasClientInterface',
    'SearchClient'
]
