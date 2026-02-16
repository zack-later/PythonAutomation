from playwright.sync_api import Page
from pages.welcome_page import WelcomePage


class LoginPage():
    LOGIN_PATH = "index.php?module=Users&action=Login"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.get_started_link = page.locator("text=Get started")
        self.user_name_field = page.get_by_placeholder("Username").first
        self.password_field = page.get_by_placeholder("Password").first
        self.log_in_button = page.locator("text=Log In")
        
    def goto(self):
        self.page.goto(f"{self.base_url}{self.LOGIN_PATH}")

    def login(self, username: str, password:str):
        self.user_name_field.fill(username)
        self.password_field.fill(password)
        self.log_in_button.click()
        return WelcomePage(self.page)