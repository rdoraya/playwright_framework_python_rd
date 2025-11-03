import requests
import os
from dotenv import load_dotenv
from utils.config_loader import load_config

class BaseAPI:
    def setup_method(self, method):
        """Initialize base_url in setup_method instead of __init__ to avoid pytest warnings"""
        load_dotenv()  # Ensure .env is loaded
        # Use config_loader for consistent config management
        config = load_config()
        # Get API base from config (which handles defaults properly)
        self.base_url = config.get("api_base", "https://jsonplaceholder.typicode.com")

    def get(self, endpoint, params=None, headers=None):
        return requests.get(f"{self.base_url}{endpoint}", params=params, headers=headers)

    def post(self, endpoint, data=None, json=None, headers=None):
        return requests.post(f"{self.base_url}{endpoint}", data=data, json=json, headers=headers)
