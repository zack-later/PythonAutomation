import pytest
from playwright.sync_api import sync_playwright
import os

@pytest.fixture(scope="session")
def browser():
    """Start a Playwright browser for the test session."""
    # Local headed, CI headless
    headed_flag = os.environ.get("CI", "false").lower() != "true"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headed_flag)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """Provide a fresh page for each test."""
    page = browser.new_page()
    yield page
    page.close()
