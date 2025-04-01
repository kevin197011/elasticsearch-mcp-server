from fastmcp import FastMCP
from mcp.types import TextContent

class DocumentTools:
    def register_tools(self, mcp: FastMCP):
        """Register document-related tools."""
        
        @mcp.tool()
        async def search_documents(index: str, body: dict) -> list[TextContent]:
            """
            Search documents in a specified index using a custom query.
            
            Args:
                index: Name of the index to search
                body: Elasticsearch query DSL
            """
            self.logger.info(f"Searching in index: {index} with query: {body}")
            try:
                return self.es_client.search(index=index, body=body)
            except Exception as e:
                self.logger.error(f"Error searching documents: {e}")
                return [TextContent(type="text", text=f"Error: {str(e)}")]
