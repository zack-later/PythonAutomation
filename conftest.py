import os
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

# Directories for artifacts
ARTIFACTS_DIR = Path("artifacts")
SCREENSHOTS_DIR = ARTIFACTS_DIR / "screenshots"
VIDEOS_DIR = ARTIFACTS_DIR / "videos"
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
VIDEOS_DIR.mkdir(parents=True, exist_ok=True)

load_dotenv()

@pytest.fixture(scope="session")
def browser():
    """Start a Playwright browser session."""
    # Local: headed for debugging; CI: always headless
    headed_flag = os.environ.get("CI", "false").lower() != "true"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=not headed_flag,
            args=["--start-maximized"] if headed_flag else []
        )
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def credentials():
    return{
        "username": os.getenv("TEST_USERNAME"),
        "password": os.getenv("TEST_PASSWORD")
    }

@pytest.fixture(scope="function")
def page(browser, request):
    """Provide a fresh page for each test with automatic screenshots/videos."""
    is_local = os.environ.get("CI", "false").lower() != "true"

    # Enable video recording only in CI
    context = browser.new_context(
        record_video_dir=str(VIDEOS_DIR) if not is_local else None
    )
    page = context.new_page()

    # Pause for Inspector locally
    if is_local:
        page.pause()

    yield page

    # Take a screenshot for every test
    screenshot_path = SCREENSHOTS_DIR / f"{request.node.name}.png"
    page.screenshot(path=str(screenshot_path))

    # Close page and context (video gets saved on context close)
    page.close()
    context.close()