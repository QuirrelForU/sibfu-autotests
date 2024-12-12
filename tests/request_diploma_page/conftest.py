import pytest

from pages.request_diploma_page import RequestDiplomaPage


@pytest.fixture
def request_diploma_page(page) -> RequestDiplomaPage:
    """Initialize `IndexPage` page."""
    return RequestDiplomaPage(page).open()
