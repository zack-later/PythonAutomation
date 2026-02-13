from playwright.sync_api import expect
from pages import LoginPage, WelcomePage

def test_welcome_and_login(page, credentials): 
    login_page = LoginPage(page)
    login_page.goto()
    login_page.fillusername(credentials["username"])
    login_page.fillpassword(credentials["password"])
    welcome_page = login_page.click_login_button()
    expect(page).to_have_title("Home » SuiteCRM Demo")
    welcome_page.verify_page_loaded()