import functools
import inspect
import logging
from typing import Callable, TypeVar
from mcp.types import TextContent

# Type variable for function return type
T = TypeVar('T')

def handle_es_exceptions(func: Callable[..., T]) -> Callable[..., list[TextContent]]:
    """
    Decorator to handle Elasticsearch exceptions in tool methods.
    Logs the error and returns it as a TextContent object.
    """
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        logger = logging.getLogger()
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Unexpected error in {func.__name__}: {e}")
            return [TextContent(type="text", text=f"Unexpected error in {func.__name__}: {str(e)}")]
    
    return wrapper
