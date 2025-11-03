import pytest
from base.base_api import BaseAPI
from utils.logger import get_logger

logger = get_logger()

@pytest.mark.api
class TestAPI(BaseAPI):

    def test_get_post(self):
        logger.info("Running API test - Get Post")
        logger.info(f"Base URL: {self.base_url}")
        response = self.get("/posts/1")
        logger.info(f"Response URL: {response.url}")
        logger.info(f"Response Status: {response.status_code}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        logger.info("API test passed successfully")
