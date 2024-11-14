from playwright.sync_api import Page


class IndexPage:
    URL = "https://www.sfu-kras.ru/"
    MAIN_LOGO_SELECTOR = "xpath=//*[@class='main-logo-image']"  # Define the selector as a class variable

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        """
        Navigates to the index page and waits until the main logo image is visible.
        """
        self.page.goto(self.URL, wait_until="domcontentloaded")
        self.page.get_by_role("link", name="Siberian Federal University").is_visible()

    def is_visible(self) -> bool:
        return self.page.get_by_role("link", name="Siberian Federal University").is_visible()

    def get_title(self):
        """
        Retrieves the title of the current page.
        """
        return self.page.title()
