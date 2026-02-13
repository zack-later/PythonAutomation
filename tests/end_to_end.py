from playwright.sync_api import expect
from pages import LoginPage, WelcomePage

def test_welcome_and_login(page): 
    login_page = LoginPage(page)
    login_page.goto()
    login_page.fillusername("will")
    login_page.fillpassword("will")
    welcome_page = login_page.click_login_button()
    expect(page).to_have_title("Home » SuiteCRM Demo")
    welcome_page.verify_page_loaded()

from pages.login_page import LoginPage

def test_login_flow(page):
    """
    Example E2E test:
    - Navigate to login page
    - Fill credentials
    - Click login
    - Verify landing on WelcomePage
    """
    # Initialize the page object
    login = LoginPage(page)

    # Go to login page
    login.goto()

    # Fill in username and password
    login.fillusername("admin")
    login.fillpassword("password")

    # Click login button (returns WelcomePage)
    welcome = login.click_login_button()

    # Example verification: check some element on welcome page
    assert welcome.welcome_message.is_visible(), "Welcome message should be visible"
