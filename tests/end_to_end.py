from playwright.sync_api import expect
from pages import LoginPage, WelcomePage

def test_welcome_and_login(page, base_url, credentials): 
    login_page = LoginPage(page, base_url)
    login_page.goto()
    welcome_page = login_page.login(
        credentials["username"],
        credentials["password"]

    )
    expect(page).to_have_title("Home » SuiteCRM Demo")
    welcome_page.verify_page_loaded()
