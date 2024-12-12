from xml.sax.xmlreader import Locator

from pages.base_page import BasePage


class Element:
    """
    Descriptor for Playwright Locator elements.
    """

    def __init__(
        self,
        locator: str | None = None,
        text: str | None = None,
        label: str | None = None,
        exact: bool = True,
    ):
        self.locator = locator
        self.text = text
        self.label = label
        self.exact = exact

    def __set_name__(self, owner, name):
        self.attribute_name = name

    def __get__(self, instance: BasePage, owner):
        if instance is None:
            raise BaseException(
                "Please provide a locator"
            )
        if self.locator:
            return instance.page.locator(self.locator)
        elif self.text:
            return instance.page.get_by_text(self.text, exact=self.exact)
        elif self.label:
            return instance.page.get_by_label(self.label, exact=self.exact)

    def __set__(self, instance, value):
        raise AttributeError(
            "Can't set attribute directly. Use methods to interact with the element."
        )
