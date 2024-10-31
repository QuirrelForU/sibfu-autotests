import pytest
from playwright.sync_api import Playwright, sync_playwright
from pages.example_page import ExamplePage

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()

def test_example(page):
    page_obj = ExamplePage(page)
    page_obj.open()
    assert page_obj.get_title() == "Example Domain"
