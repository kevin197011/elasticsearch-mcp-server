from typing import Dict
from .index import ElasticsearchIndexClient
from .document import ElasticsearchDocumentClient
from .cluster import ElasticsearchClusterClient
from .alias import ElasticsearchAliasClient

class ElasticsearchClient(ElasticsearchIndexClient,
                         ElasticsearchDocumentClient,
                         ElasticsearchClusterClient,
                         ElasticsearchAliasClient):
    """
    Elasticsearch client that implements all required interfaces.
    
    This class uses multiple inheritance to combine all specialized client implementations
    into a single unified client, inheriting all methods from the specialized clients.
    """
    
    def __init__(self, config: Dict):
        """
        Initialize the Elasticsearch client.
        
        Args:
            config: Configuration dictionary with connection parameters
        """
        super().__init__(config)
        
        # Log initialization
        self.logger.info("Initialized the Elasticsearch client")
