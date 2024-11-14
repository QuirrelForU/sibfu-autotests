from playwright.sync_api import Page


class PostgraduateInfoPage:
    URL = "https://research.sfu-kras.ru/asp"

    def __init__(self, page: Page):
        self.page = page

    def is_visible(self) -> bool:
        return self.page.get_by_role(
            "heading", name="Аспирантура Сибирского федерального университета"
            ).is_visible()
