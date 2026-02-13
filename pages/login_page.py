from playwright.sync_api import Page
from pages.welcome_page import WelcomePage

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.get_started_link = page.locator("text=Get started")
        self.user_name_field = page.get_by_placeholder("Username").first
        self.password_field = page.get_by_placeholder("Password").first
        self.log_in_button = page.locator("text=Log In")
        
    def goto(self):
        self.page.goto("https://demo.suiteondemand.com/index.php?module=Users&action=Login")

    def fillusername(self, username: str):
        self.user_name_field.fill(username)
    
    def fillpassword(self, password: str):
        self.password_field.fill(password)

    def click_login_button(self):
        self.log_in_button.click()
        return WelcomePage(self.page)