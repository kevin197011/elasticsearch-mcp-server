import logging
import functools
from fastmcp import FastMCP
from typing import List, Type, Callable, TypeVar
from elasticsearch import Elasticsearch
from elasticsearch_mcp_server.tools.base import handle_es_exceptions

T = TypeVar('T')

def with_exception_handling(tool_instance: object, mcp: FastMCP) -> None:
    """
    Register tools from a tool instance with automatic exception handling applied to all tools.
    
    This function temporarily replaces mcp.tool with a wrapped version that automatically
    applies the handle_es_exceptions decorator to all registered tool methods.
    
    Args:
        tool_instance: The tool instance that has a register_tools method
        mcp: The FastMCP instance used for tool registration
    """
    # Save the original tool method
    original_tool = mcp.tool
    
    @functools.wraps(original_tool)
    def wrapped_tool(*args, **kwargs):
        # Get the original decorator
        decorator = original_tool(*args, **kwargs)
        
        # Return a new decorator that applies both the exception handler and original decorator
        def combined_decorator(func):
            # First apply the exception handling decorator
            wrapped_func = handle_es_exceptions(func)
            # Then apply the original mcp.tool decorator
            return decorator(wrapped_func)
        
        return combined_decorator
    
    try:
        # Temporarily replace mcp.tool with our wrapped version
        mcp.tool = wrapped_tool
        
        # Call the registration method on the tool instance
        tool_instance.register_tools(mcp)
    finally:
        # Restore the original mcp.tool to avoid affecting other code that might use mcp.tool
        # This ensures that our modification is isolated to just this tool registration
        # and prevents multiple nested decorators if register_all_tools is called multiple times
        mcp.tool = original_tool


class ToolsRegister:
    """
    A class responsible for creating and registering all tool classes.
    This centralizes the tool registration process and reduces duplication.
    """
    
    def __init__(self, logger: logging.Logger, es_client: Elasticsearch, mcp: FastMCP):
        """
        Initialize the tools registrar.
        
        Args:
            logger: Logger instance for logging
            es_client: Elasticsearch client instance for API calls
            mcp: FastMCP instance for tool registration
        """
        self.logger = logger
        self.es_client = es_client
        self.mcp = mcp
        
    def register_all_tools(self, tool_classes: List[Type]):
        """
        Create instances of all tool classes and register their tools.
        
        Args:
            tool_classes: List of tool classes to instantiate and register
        """
        for tool_class in tool_classes:
            # Create an instance of the tool class without initialization parameters
            tool_instance = tool_class()
            
            # Set logger and es_client attributes directly
            tool_instance.logger = self.logger
            # Pass the raw Elasticsearch client instead of the wrapper
            tool_instance.es_client = self.es_client
            
            # Register tools with automatic exception handling
            with_exception_handling(tool_instance, self.mcp)
            
            self.logger.info(f"Registered tools from {tool_class.__name__}")
