import logging
import os
from dotenv import load_dotenv
from fastmcp import FastMCP
from src.tools.index import IndexTools
from src.tools.document import DocumentTools
from src.tools.cluster import ClusterTools
from src.tools.alias import AliasTools
from src.tools.register import ToolsRegister
from src.clients import create_search_client

class SearchMCPServer:
    def __init__(self, engine_type):
        # Set engine type
        self.engine_type = engine_type
        self.name = f"{self.engine_type}_mcp_server"
        self.mcp = FastMCP(self.name)
        self.logger = logging.getLogger(self.name)
        self.logger.info(f"Initializing {self.name}...")
        
        # Create the corresponding search client
        self.search_client = self._create_search_client()
        
        # Initialize tools
        self._register_tools()
    
    def _create_search_client(self):
        """
        Create search client
        
        Returns:
            SearchClient: Instance of the corresponding search client
        """
        # Load configuration from environment variables
        load_dotenv()
        
        # Use engine type (uppercase) as environment variable prefix
        prefix = self.engine_type.upper()
        
        # Get hosts as comma-separated string and split into list
        hosts_str = os.getenv(f"{prefix}_HOST", "https://localhost:9200")
        hosts = [host.strip() for host in hosts_str.split(",")]
        
        config = {
            "hosts": hosts,
            "username": os.getenv(f"{prefix}_USERNAME"),
            "password": os.getenv(f"{prefix}_PASSWORD"),
            "verify_certs": os.getenv(f"{prefix}_VERIFY_CERTS", "false").lower() == "true"
        }
        
        if not all([config["username"], config["password"]]):
            self.logger.error(f"Missing required {self.engine_type} configuration. Please check environment variables:")
            self.logger.error(f"{prefix}_USERNAME and {prefix}_PASSWORD are required")
            raise ValueError(f"Missing required {self.engine_type} configuration")
        
        self.logger.info(f"Creating {self.engine_type} client with host: {config['hosts']}")
        
        # Create the corresponding client
        return create_search_client(config, self.engine_type)

    def _register_tools(self):
        """Register all MCP tools."""
        # Create a tools register
        register = ToolsRegister(self.logger, self.search_client, self.mcp)
        
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

def run_search_server(engine_type):
    """Run search server with specified engine type."""
    server = SearchMCPServer(engine_type=engine_type)
    server.run()

def elasticsearch_mcp_server():
    """Entry point for Elasticsearch MCP server."""
    run_search_server(engine_type="elasticsearch")

def opensearch_mcp_server():
    """Entry point for OpenSearch MCP server."""
    run_search_server(engine_type="opensearch")
