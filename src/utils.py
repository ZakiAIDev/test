

import sys
from typing import Any, Dict

import yaml
from loguru import logger


def load_data(file_path: str = "config.yml") -> Dict[str, Any]:
        """
        Load configuration from a YAML file.

        Args:
            file_path (str): Path to the YAML configuration file.

        Returns:
            dict: A dictionary containing the configuration.
        """
        try:
            with open(file_path, "r") as config_file:
                config = yaml.safe_load(config_file)
            return config
        except Exception as e:
            logger.error(f"Error loading configuration from YAML: {e}")
            sys.exit(0)

