#!/usr/bin/env python3
import sys

sys.path.append("../")
import logging
from fastmcp import FastMCP
from elasticsearch_mcp_server.tools.index import IndexTools
from elasticsearch_mcp_server.tools.document import DocumentTools
from elasticsearch_mcp_server.tools.cluster import ClusterTools
from elasticsearch_mcp_server.tools.alias import AliasTools

class ElasticsearchMCPServer:
    def __init__(self):
        self.name = "elasticsearch_mcp_server"
        self.mcp = FastMCP(self.name)
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(self.name)
        
        # Initialize tools
        self._register_tools()

    def _register_tools(self):
        """Register all MCP tools."""
        # Initialize tool classes
        index_tools = IndexTools(self.logger)
        document_tools = DocumentTools(self.logger)
        cluster_tools = ClusterTools(self.logger)
        alias_tools = AliasTools(self.logger)
        
        # Register tools from each module
        index_tools.register_tools(self.mcp)
        document_tools.register_tools(self.mcp)
        cluster_tools.register_tools(self.mcp)
        alias_tools.register_tools(self.mcp)

    def run(self):
        """Run the MCP server."""
        self.mcp.run()

def main():
    server = ElasticsearchMCPServer()
    server.run()

if __name__ == '__main__':
    main()
