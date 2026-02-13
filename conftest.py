import pytest
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run tests in headed mode locally"
    )

@pytest.fixture(scope="session")
def browser(request):
    """Start a Playwright browser for the test session."""
    # Determine if user requested headed mode
    headed_flag = request.config.getoption("--headed")

    # Force headless in CI (no DISPLAY available)
    import os
    if os.environ.get("CI", "false").lower() == "true":
        headed_flag = False

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
