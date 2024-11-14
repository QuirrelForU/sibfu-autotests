from playwright.sync_api import Page


class EmployeeInfoPage:
    URL = "https://www.sfu-kras.ru/gateways/staff"

    def __init__(self, page: Page):
        self.page = page

    def is_visible(self) -> bool:
        return self.page.get_by_role("heading", name="Сотруднику").is_visible()
