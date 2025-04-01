from typing import Dict
from .elasticsearch.client import ElasticsearchClient
from .opensearch.client import OpenSearchClient
from .interfaces import SearchClient

def create_search_client(config: Dict, engine_type: str) -> SearchClient:
    """
    Factory function to create the appropriate search client.
    
    Args:
        config: Configuration dictionary with connection parameters
        engine_type: Type of search engine to use ("elasticsearch" or "opensearch")
        
    Returns:
        SearchClient: An instance of the appropriate search client
        
    Raises:
        ValueError: If an invalid engine type is specified
    """
    if engine_type.lower() == "elasticsearch":
        return ElasticsearchClient(config)
    elif engine_type.lower() == "opensearch":
        return OpenSearchClient(config)
    else:
        raise ValueError(f"Invalid engine type: {engine_type}. Must be 'elasticsearch' or 'opensearch'")

__all__ = [
    'create_search_client',
    'handle_search_exceptions',
    'SearchClient',
    'ElasticsearchClient',
    'OpenSearchClient',
]
