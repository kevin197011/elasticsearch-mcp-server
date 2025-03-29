from typing import Any
from ..es_client import ElasticsearchClient
from mcp.types import TextContent


class AliasTools(ElasticsearchClient):
    def register_tools(self, mcp: Any):
        """Register alias-related tools."""

        @mcp.tool(description="List all aliases in the Elasticsearch cluster")
        async def list_aliases() -> list[TextContent]:
            """List all aliases in the Elasticsearch cluster."""
            self.logger.info("Listing aliases...")
            try:
                aliases = self.es_client.cat.aliases(format="json")
                return [TextContent(type="text", text=str(aliases))]
            except Exception as e:
                self.logger.error(f"Error listing aliases: {e}")
                return [TextContent(type="text", text=f"Error: {str(e)}")]

        @mcp.tool(description="Get alias information for an index")
        async def get_alias(index: str) -> list[TextContent]:
            """
            Get alias information for a specific index.

            Args:
                index: Name of the index
            """
            self.logger.info(f"Getting alias information for index: {index}")
            try:
                response = self.es_client.indices.get_alias(index=index)
                return [TextContent(type="text", text=str(response))]
            except Exception as e:
                self.logger.error(f"Error getting alias information: {e}")
                return [TextContent(type="text", text=f"Error: {str(e)}")]
