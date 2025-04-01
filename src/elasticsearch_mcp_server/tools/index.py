from fastmcp import FastMCP
from mcp.types import TextContent
from typing import Dict

class IndexTools:
    def register_tools(self, mcp: FastMCP):
        @mcp.tool()
        async def list_indices() -> Dict:
            """List all indices."""
            try:
                return self.es_client.cat.indices()
            except Exception as e:
                self.logger.error(f"Error listing indices: {e}")
                return [TextContent(type="text", text=f"Error: {str(e)}")]

        @mcp.tool()
        async def get_mapping(index: str) -> list[TextContent]:
            """
            Get the mapping for an index.
            
            Args:
                index: Name of the index
            """
            try:
                return self.es_client.indices.get_mapping(index=index)
            except Exception as e:
                self.logger.error(f"Error getting mapping: {e}")
                return [TextContent(type="text", text=f"Error: {str(e)}")]

        @mcp.tool()
        async def get_settings(index: str) -> list[TextContent]:
            """
            Get the settings for an index.
            
            Args:
                index: Name of the index
            """
            try:
                return self.es_client.indices.get_settings(index=index)
            except Exception as e:
                self.logger.error(f"Error getting settings: {e}")
                return [TextContent(type="text", text=f"Error: {str(e)}")]
