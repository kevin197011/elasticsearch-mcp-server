from fastmcp import FastMCP
from typing import Dict
from elasticsearch_mcp_server.tools.base import handle_es_exceptions

class ClusterTools:
    def register_tools(self, mcp: FastMCP):
        """Register cluster-related tools."""
        
        @mcp.tool()
        async def get_cluster_health() -> Dict:
            """
            Get health status of the Elasticsearch cluster.
            Returns information about the number of nodes, shards, etc.
            """
            return self.es_client.cluster.health()

        @mcp.tool()
        async def get_cluster_stats() -> Dict:
            """
            Get statistics from a cluster wide perspective. 
            The API returns basic index metrics (shard numbers, store size, memory usage) and information 
            about the current nodes that form the cluster (number, roles, os, jvm versions, memory usage, cpu and installed plugins).
            https://www.elastic.co/guide/en/elasticsearch/reference/8.17/cluster-stats.html
            """
            return self.es_client.cluster.stats()
