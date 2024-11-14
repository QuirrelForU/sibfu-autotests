from pages.index_page import IndexPage


def test_page_is_visible(page):
    index_page = IndexPage(page)
    index_page.navigate()
    assert index_page.is_visible()

def test_page_title(page):
    index_page = IndexPage(page)
    index_page.navigate()
    expected_title = "Сибирский федеральный университет"  # Replace with the actual expected title
    actual_title = index_page.get_title()
    assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'."
