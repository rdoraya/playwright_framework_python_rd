import pytest
from base.base_ui import BaseUI
from pages.google_page import GooglePage
from utils.logger import get_logger

logger = get_logger()

@pytest.mark.ui
class TestGoogleUI(BaseUI):

    def test_google_search(self):
        logger.info("Starting Google UI Test")
        google = GooglePage(self.page)
        google.open()
        google.search("Playwright Python")
        assert google.verify_results()
        logger.info("Google search test passed")
