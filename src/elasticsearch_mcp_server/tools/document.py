from fastmcp import FastMCP
from typing import Dict
from elasticsearch_mcp_server.tools.base import handle_es_exceptions

class DocumentTools:
    def register_tools(self, mcp: FastMCP):
        """Register document-related tools."""
        
        @mcp.tool()
        async def search_documents(index: str, body: dict) -> Dict:
            """
            Search documents in a specified index using a custom query.
            
            Args:
                index: Name of the index to search
                body: Elasticsearch query DSL
            """
            return self.es_client.search(index=index, body=body)
