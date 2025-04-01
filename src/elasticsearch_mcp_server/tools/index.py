from fastmcp import FastMCP
from typing import Dict
from elasticsearch_mcp_server.tools.base import handle_es_exceptions

class IndexTools:
    def register_tools(self, mcp: FastMCP):
        @mcp.tool()
        async def list_indices() -> Dict:
            """List all indices."""
            return self.es_client.cat.indices()

        @mcp.tool()
        async def get_mapping(index: str) -> Dict:
            """
            Get the mapping for an index.
            
            Args:
                index: Name of the index
            """
            return self.es_client.indices.get_mapping(index=index)

        @mcp.tool()
        async def get_settings(index: str) -> Dict:
            """
            Get the settings for an index.
            
            Args:
                index: Name of the index
            """
            return self.es_client.indices.get_settings(index=index)
