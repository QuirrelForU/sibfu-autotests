from playwright.sync_api import expect

from pages.request_diploma_page import RequestDiplomaPage


def test_form_visible(request_diploma_page: RequestDiplomaPage):
    """Check that user can open request_diploma_form."""
    expect(request_diploma_page.logo).to_be_visible()


def test_sending_form_request(request_diploma_page: RequestDiplomaPage):
    """Check that user can send diploma request."""
    import ipdb
    ipdb.set_trace()
    request_diploma_page.last_name.fill("Фамилия")
    request_diploma_page.first_name.fill("Имя")
    request_diploma_page.surname.fill("Отчество")

    request_diploma_page.birth_day.select_option("12")
    request_diploma_page.birth_month.select_option("3")
    request_diploma_page.birth_year.select_option("1980")

    request_diploma_page.email.fill("example@mail.com")
    request_diploma_page.phone.fill("1234567890")
    request_diploma_page.university.select_option("7")
    request_diploma_page.specialty.click()
    request_diploma_page.specialty.get_by_text("09.03.04 Программная инженерия").click()

    request_diploma_page.full_time_course.click()
    request_diploma_page.admission_year.select_option("2000")
    request_diploma_page.graduation_year.select_option("2004")
    request_diploma_page.document_type.select_option("3")
    request_diploma_page.diploma_registration.fill("1234567")
    request_diploma_page.diploma_series.fill("123456")

    request_diploma_page.diploma_day.select_option("15")
    request_diploma_page.diploma_month.select_option("3")
    request_diploma_page.diploma_year.select_option("2004")
    import ipdb
    ipdb.set_trace()

