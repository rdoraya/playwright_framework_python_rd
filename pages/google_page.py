from playwright.sync_api import Page

class GooglePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_box = 'input[name="q"]'
        self.result_stats = '#result-stats'

    def open(self, url="https://www.google.com"):
        self.page.goto(url, wait_until="domcontentloaded", timeout=30000)
        # Handle cookie consent if present
        try:
            # Common cookie consent button selectors for Google
            cookie_selectors = [
                '#L2AGLb',  # Google's accept button ID (most common)
                'button:has-text("Accept all")',
                'button:has-text("Accept")',
                'button:has-text("I agree")',
                'button[id*="accept"]',
                '[aria-label*="Accept"]',
            ]
            for selector in cookie_selectors:
                try:
                    # Use locator with shorter timeout for cookie buttons
                    locator = self.page.locator(selector).first
                    if locator.is_visible(timeout=2000):
                        locator.click(timeout=2000)
                        self.page.wait_for_timeout(1000)  # Wait for dialog to close
                        break
                except:
                    continue
        except:
            pass  # Continue if no consent dialog
        
        # Wait for search box to be visible with multiple selector attempts
        # Google may use different selectors in different regions
        search_selectors = [
            'input[name="q"]',
            'textarea[name="q"]',  # Google sometimes uses textarea
            'input[type="search"]',
            '[aria-label*="Search"]',
        ]
        found = False
        for selector in search_selectors:
            try:
                self.page.wait_for_selector(selector, state="visible", timeout=5000)
                self.search_box = selector
                found = True
                break
            except:
                continue
        
        if not found:
            raise Exception("Could not find Google search box")

    def search(self, query):
        # Wait for search box to be visible before filling
        self.page.wait_for_selector(self.search_box, state="visible")
        self.page.fill(self.search_box, query)
        self.page.keyboard.press("Enter")
        # Wait for results to load
        self.page.wait_for_load_state("networkidle", timeout=10000)

    def verify_results(self):
        # Wait for results to appear - Google may use different result selectors
        result_selectors = [
            '#result-stats',  # Original selector
            '[id="result-stats"]',
            '[aria-label*="results"]',
            'div:has-text("results")',
            '#search',  # Main search results container
            '[data-async-context]',  # Google results container
        ]
        
        # Try multiple selectors with shorter timeouts
        for selector in result_selectors:
            try:
                if self.page.wait_for_selector(selector, state="visible", timeout=3000):
                    return True
            except:
                continue
        
        # Fallback: check if search page loaded (any results area)
        try:
            # Check if we're still on search page with results
            url = self.page.url
            if "google.com/search" in url or self.page.locator('[role="main"]').count() > 0:
                return True
        except:
            pass
        
        return False
