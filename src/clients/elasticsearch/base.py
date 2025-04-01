"""
Base Elasticsearch client implementation.
"""
from elasticsearch import Elasticsearch
from typing import Dict
import logging
from ..base import SearchClientBase

class BaseElasticsearchClient(SearchClientBase):
    """Base Elasticsearch client with connection management."""
    
    def __init__(self, config: Dict):
        """
        Initialize the Elasticsearch client.
        
        Args:
            config: Configuration dictionary with connection parameters
        """
        super().__init__(config)
        self.logger.info("Initializing Elasticsearch client")
        
        # Extract configuration
        hosts = config.get("hosts", ["localhost:9200"])
        username = config.get("username")
        password = config.get("password")
        verify_certs = config.get("verify_certs")
        
        # Create client
        self.client = Elasticsearch(
            hosts=hosts,
            basic_auth=(username, password) if username and password else None,
            verify_certs=verify_certs
        )
        
        self.logger.info(f"Elasticsearch client initialized with hosts: {hosts}")
    
    def close(self):
        """Close the Elasticsearch client connection."""
        self.logger.info("Closing Elasticsearch client connection")
        self.client.close()
