from typing import Dict
from .index import OpenSearchIndexClient
from .document import OpenSearchDocumentClient
from .cluster import OpenSearchClusterClient
from .alias import OpenSearchAliasClient

class OpenSearchClient(OpenSearchIndexClient,
                       OpenSearchDocumentClient,
                       OpenSearchClusterClient,
                       OpenSearchAliasClient):
    """
    OpenSearch client that implements all required interfaces.
    
    This class uses multiple inheritance to combine all specialized client implementations
    into a single unified client, inheriting all methods from the specialized clients.
    """
    
    def __init__(self, config: Dict):
        """
        Initialize the OpenSearch client.
        
        Args:
            config: Configuration dictionary with connection parameters
        """
        super().__init__(config)  
        self.logger.info("Initialized the OpenSearch client")
