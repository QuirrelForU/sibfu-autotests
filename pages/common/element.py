from playwright.sync_api import Locator


class Element:
    """
    Descriptor for Playwright Locator elements.
    Usage:
        first_name = Element("input[name='first_name']")
    """

    def __init__(self, locator: str):
        self.locator = locator
        self.private_name = f"_{locator.replace('=', '_').replace('[', '_').replace(']', '_')}"

    def __set_name__(self, owner, name):
        self.attribute_name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self  # Accessed through the class, return the descriptor itself
        # Retrieve the Locator from the Playwright Page instance
        locator_obj: Locator = instance.page.locator(self.locator)
        return locator_obj

    def __set__(self, instance, value):
        raise AttributeError(
            "Can't set attribute directly. Use methods to interact with the element."
        )
