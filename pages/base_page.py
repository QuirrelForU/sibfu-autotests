from typing import Self
from xml.sax.xmlreader import Locator

from playwright.sync_api import Page


class BasePage:
    base_url: str

    def __init__(self, page: Page):
        self.page = page

    def open(self) -> Self:
        self.page.goto(self.base_url, wait_until="domcontentloaded")
        return self

    @property
    def logo(self) -> Locator:
        return self.page.get_by_role(
            "link", name="Сибирский федеральный университет Сибирский федеральный университет"
        )
