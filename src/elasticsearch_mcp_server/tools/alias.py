from fastmcp import FastMCP
from typing import Dict, List
from elasticsearch_mcp_server.tools.base import handle_es_exceptions

class AliasTools:
    def register_tools(self, mcp: FastMCP):
        @mcp.tool()
        async def list_aliases() -> List[Dict]:
            """List all aliases in the Elasticsearch cluster."""
            return self.es_client.cat.aliases()

        @mcp.tool()
        async def get_alias(index: str) -> Dict:
            """
            Get alias information for a specific index.

            Args:
                index: Name of the index
            """
            return self.es_client.indices.get_alias(index=index)
