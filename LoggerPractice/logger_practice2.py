import logging
import logging.config
import os
import yaml

def setup_logger(
    name:str,
    level=logging.INFO,
    log_to_file: bool = False,
    log_file: str = "app.log",
    config_path: str = None
) -> logging.Logger:
    """
    Configure and return a Logger with the specified name and logging level.
    Optional file logging and YAML/JSON config support.

    Args:
        name (str): The name of the Logger.
        Level (int): The Logging Level (default is Logging.INFO).
        log_to_file (bool): Whether to log to a file (default is False).
        log_file (str): The file to Log to if log_to_file is True (default is "app.log").
        config_path (str): YAML or JSON config file path for logging configuration (default is None).

    Returns:
        logging.Logger: Configured Logger instance.    
    """

    if config_path and os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            if config_path.endswith((".yaml",".yml")):
                config = yaml.safe_load(f)
            elif config_path.endswith(".json"):
                import json
                config = json.load(f)
            else:
                raise ValueError("Unsupported config file type (only YAML/JSON supported).")
            
        logging.config.dictConfig(config)
        logger = logging.getLogger(name)
        return logger
    
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.hasHandlers():

        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        if log_to_file:
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setLevel(level)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    return logger
    

# logger = setup_logger("myapp")
# logger.info("Logger setup complete.")


logger = setup_logger("myapp", log_to_file=True, log_file="myapp.log")
logger.info("Console + app.log")