from playwright.sync_api import Page, expect


class StudentsInfoPage:
    URL = "https://www.sfu-kras.ru/gateways/students"

    def __init__(self, page: Page):
        self.page = page

    def is_visible(self) -> None:
        expect(self.page.get_by_role("heading", name="Студенту")).to_be_visible()
