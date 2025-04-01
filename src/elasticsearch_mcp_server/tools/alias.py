from fastmcp import FastMCP
from mcp.types import TextContent

class AliasTools:
    def register_tools(self, mcp: FastMCP):
        @mcp.tool()
        async def list_aliases() -> list[TextContent]:
            """List all aliases in the Elasticsearch cluster."""
            try:
                return self.es_client.cat.aliases(format="json")
            except Exception as e:
                self.logger.error(f"Error listing aliases: {e}")
                return [TextContent(type="text", text=f"Error: {str(e)}")]

        @mcp.tool()
        async def get_alias(index: str) -> list[TextContent]:
            """
            Get alias information for a specific index.

            Args:
                index: Name of the index
            """
            try:
                return self.es_client.indices.get_alias(index=index)
            except Exception as e:
                self.logger.error(f"Error getting alias information: {e}")
                return [TextContent(type="text", text=f"Error: {str(e)}")]
