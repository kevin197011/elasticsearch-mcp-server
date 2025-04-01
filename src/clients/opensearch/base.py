from opensearchpy import OpenSearch
from typing import Dict
from ..base import SearchClientBase

class BaseOpenSearchClient(SearchClientBase):
    """Base OpenSearch client with connection management."""
    
    def __init__(self, config: Dict):
        """
        Initialize the OpenSearch client.
        
        Args:
            config: Configuration dictionary with connection parameters
        """
        super().__init__(config)
        self.logger.info("Initializing OpenSearch client")
        
        # Extract configuration
        hosts = config.get("hosts", ["localhost:9200"])
        username = config.get("username")
        password = config.get("password")
        verify_certs = config.get("verify_certs")
        
        # Create client
        self.client = OpenSearch(
            hosts=hosts,
            http_auth=(username, password) if username and password else None,
            verify_certs=verify_certs
        )
        
        self.logger.info(f"OpenSearch client initialized with hosts: {hosts}")
    
    def close(self):
        """Close the OpenSearch client connection."""
        self.logger.info("Closing OpenSearch client connection")
        self.client.close()
