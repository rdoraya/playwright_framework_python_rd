from playwright.sync_api import sync_playwright

class BaseUI:
    def setup_method(self, method):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.firefox.launch(headless=True)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def teardown_method(self, method):
        try:
            self.context.close()
            self.browser.close()
        finally:
            self.playwright.stop()
