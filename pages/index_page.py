from pages.base_page import BasePage
from pages.employee_info_page import EmployeeInfoPage
from pages.postgraduate_page import PostgraduateInfoPage
from pages.students_info_page import StudentsInfoPage


class IndexPage(BasePage):
    """Represent `Index` page."""
    base_url = "https://www.sfu-kras.ru/"

    def open_postgraduate_page(self) -> PostgraduateInfoPage:
        self.page.get_by_title("Аспиранту").click()
        return PostgraduateInfoPage(self.page)

    def open_employee_info_page(self) -> EmployeeInfoPage:
        self.page.locator("#footer-fast-nav").get_by_role("link", name="Сотруднику").click()
        return EmployeeInfoPage(self.page)

    def open_students_info_page(self) -> StudentsInfoPage:
        self.page.get_by_title("Студенту").click()
        return StudentsInfoPage(self.page)
