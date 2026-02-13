from playwright.sync_api import Page, expect

class WelcomePage:
    def __init__(self, page: Page):
        self.page = page

    def verify_page_loaded(self):
        expect (self.page).to_have_title("Home » SuiteCRM Demo")