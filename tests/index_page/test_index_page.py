from playwright.sync_api import expect

from pages.employee_info_page import EmployeeInfoPage
from pages.index_page import IndexPage
from pages.postgraduate_page import PostgraduateInfoPage
from pages.students_info_page import StudentsInfoPage


def test_page_is_visible(page):
    index_page = IndexPage(page)
    index_page.navigate()
    expect(page.locator(".signature-ru")).to_be_visible()


def test_page_title(page):
    index_page = IndexPage(page)
    index_page.navigate()
    expected_title = "Сибирский федеральный университет"  # Replace with the actual expected title
    actual_title = index_page.get_title()
    assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'."


def test_postgraduate_section(page):
    index_page = IndexPage(page)
    index_page.navigate()
    index_page.page.get_by_title("Аспиранту").click()
    index_page.page.wait_for_url(PostgraduateInfoPage.URL)
    postgraduate_page = PostgraduateInfoPage(page)
    assert postgraduate_page.is_visible()


def test_employee_section(page):
    index_page = IndexPage(page)
    index_page.navigate()
    index_page.page.locator("#footer-fast-nav").get_by_role("link", name="Сотруднику").click()
    index_page.page.wait_for_url(EmployeeInfoPage.URL)
    employee_info_page = EmployeeInfoPage(page)
    assert employee_info_page.is_visible()



def test_students_section(page):
    index_page = IndexPage(page)
    index_page.navigate()
    index_page.page.get_by_title("Студенту").click()
    index_page.page.wait_for_url(StudentsInfoPage.URL)
    employee_info_page = StudentsInfoPage(page)
    employee_info_page.is_visible()
