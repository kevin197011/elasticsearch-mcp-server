#!/usr/bin/env python3
import logging
import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
import warnings
from fastmcp import FastMCP
from elasticsearch_mcp_server.tools.index import IndexTools
from elasticsearch_mcp_server.tools.document import DocumentTools
from elasticsearch_mcp_server.tools.cluster import ClusterTools
from elasticsearch_mcp_server.tools.alias import AliasTools
from elasticsearch_mcp_server.tools.register import ToolsRegister

class ElasticsearchMCPServer:
    def __init__(self):
        self.name = "elasticsearch_mcp_server"
        self.mcp = FastMCP(self.name)
        self.logger = logging.getLogger(self.name)
        self.es_client = self._create_elasticsearch_client()
        
        # Initialize tools
        self._register_tools()
        
    def _get_es_config(self):
        """Get Elasticsearch configuration from environment variables."""
        # Load environment variables from .env file
        load_dotenv()
        config = {
            "host": os.getenv("ELASTIC_HOST"),
            "username": os.getenv("ELASTIC_USERNAME"),
            "password": os.getenv("ELASTIC_PASSWORD")
        }
        
        if not all([config["username"], config["password"]]):
            self.logger.error("Missing required Elasticsearch configuration. Please check environment variables:")
            self.logger.error("ELASTIC_USERNAME and ELASTIC_PASSWORD are required")
            raise ValueError("Missing required Elasticsearch configuration")
        
        return config

    def _create_elasticsearch_client(self) -> Elasticsearch:
        """Create and return an Elasticsearch client using configuration from environment."""
        config = self._get_es_config()

        # Disable SSL warnings
        warnings.filterwarnings("ignore", message=".*TLS with verify_certs=False is insecure.*",)

        return Elasticsearch(
            config["host"],
            basic_auth=(config["username"], config["password"]),
            verify_certs=False
        )

    def _register_tools(self):
        """Register all MCP tools."""
        # Create a tools register
        register = ToolsRegister(self.logger, self.es_client, self.mcp)
        
        # Define all tool classes to register
        tool_classes = [
            IndexTools,
            DocumentTools,
            ClusterTools,
            AliasTools
        ]        
        # Register all tools
        register.register_all_tools(tool_classes)

    def run(self):
        """Run the MCP server."""
        self.mcp.run()

def main():
    server = ElasticsearchMCPServer()
    server.run()
