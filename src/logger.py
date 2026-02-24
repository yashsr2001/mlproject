import logging
import sys

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Create and configure a logger instance.
    
    Args:
        name: Name of the logger (typically __name__)
        level: Logging level (default: INFO)
    
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create console handler with formatting
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    # Add handler if not already present
    if not logger.handlers:
        logger.addHandler(handler)
    
    return logger