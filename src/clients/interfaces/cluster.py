from abc import ABC, abstractmethod
from typing import Dict

class ClusterClientInterface(ABC):
    @abstractmethod
    def get_cluster_health(self) -> Dict:
        """Returns basic information about the health of the cluster."""
        pass
    
    @abstractmethod
    def get_cluster_stats(self) -> Dict:
        """Returns high-level overview of cluster statistics."""
        pass
