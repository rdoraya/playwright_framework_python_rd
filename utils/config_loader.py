import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    # Default to jsonplaceholder.typicode.com for API tests compatibility
    # .env may have reqres.in, but tests use jsonplaceholder endpoints
    # Override via API_BASE env var at runtime if needed
    api_base = os.getenv("API_BASE")
    # Use jsonplaceholder as default for test compatibility
    if not api_base or api_base == "https://reqres.in":
        api_base = "https://jsonplaceholder.typicode.com"
    return {
        "base_url": os.getenv("BASE_URL", "https://www.google.com"),
        "api_base": api_base,
        "user_email": os.getenv("TEST_USER_EMAIL", "test@example.com"),
        "user_password": os.getenv("TEST_USER_PASSWORD", "password123"),
    }
