"""
OpenSearch cluster operations implementation.
"""
from typing import Dict
from .base import BaseOpenSearchClient
from ..interfaces.cluster import ClusterClientInterface

class OpenSearchClusterClient(BaseOpenSearchClient, ClusterClientInterface):
    """Implementation of cluster operations for OpenSearch."""
    
    def get_cluster_health(self) -> Dict:
        """Get cluster health information from OpenSearch."""
        self.logger.debug("Getting cluster health")
        return self.client.cluster.health()
    
    def get_cluster_stats(self) -> Dict:
        """Get cluster statistics from OpenSearch."""
        self.logger.debug("Getting cluster stats")
        return self.client.cluster.stats()
