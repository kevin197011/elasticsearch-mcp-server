from typing import Dict
from .base import BaseElasticsearchClient
from ..interfaces.cluster import ClusterClientInterface

class ElasticsearchClusterClient(BaseElasticsearchClient, ClusterClientInterface):
    def get_cluster_health(self) -> Dict:
        """Returns basic information about the health of the cluster."""
        return self.client.cluster.health()
    
    def get_cluster_stats(self) -> Dict:
        """Returns high-level overview of cluster statistics."""
        return self.client.cluster.stats()
