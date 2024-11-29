import pytest

from pages.index_page import IndexPage


@pytest.fixture
def index_page(page) -> IndexPage:
    """Initialize `IndexPage` page."""
    return IndexPage(page).open()
