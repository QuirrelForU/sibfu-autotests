from playwright.sync_api import expect

from pages.index_page import IndexPage


def test_page_is_visible(index_page: IndexPage):
    expect(index_page.logo).to_be_visible()


def test_page_title(index_page: IndexPage):
    expected_title = "Сибирский федеральный университет"
    actual_title = index_page.page.title()
    assert actual_title == expected_title


def test_postgraduate_section(index_page: IndexPage):
    postgraduate_page = index_page.open_postgraduate_page()
    expect(postgraduate_page.logo).to_be_visible()


def test_employee_section(index_page: IndexPage):
    employee_info_page = index_page.open_employee_info_page()
    expect(employee_info_page.logo).to_be_visible()


def test_students_section(index_page: IndexPage):
    students_info_page = index_page.open_students_info_page()
    expect(students_info_page.logo).to_be_visible()
