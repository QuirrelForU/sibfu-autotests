import time

from playwright.sync_api import expect

from pages.request_diploma_page import RequestDiplomaPage


def test_form_visible(request_diploma_page: RequestDiplomaPage):
    """Check that user can open request_diploma_form."""
    expect(request_diploma_page.logo).to_be_visible()


def test_sending_form_request(request_diploma_page: RequestDiplomaPage):
    """Check that user can send diploma request."""
    time.sleep(2)
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
    request_diploma_page.take_by_myself.click()
    request_diploma_page.personal_data_checkbox.click()
    time.sleep(2)

    request_diploma_page.confirm_request()

    expect(request_diploma_page.validation_message).to_contain_text(
        "Поле «Скан/фото диплома» обязательно для заполнения."
    )


def test_empty_form_validation(request_diploma_page: RequestDiplomaPage):
    """Check validations in request diploma form."""
    request_diploma_page.confirm_request()
    expect(request_diploma_page.validation_message).to_contain_text(
        "Сообщение об ошибке Поле «Фамилия» обязательно для заполнения. Поле «Имя» обязательно для заполнения. Поле «Отчество» обязательно для заполнения. Поле «Дата рождения» обязательно для заполнения. Поле «E-mail» обязательно для заполнения. Поле «Телефон» обязательно для заполнения. Поле «Институт/филиал СФУ» обязательно для заполнения. Поле «Направление подготовки / специальность» обязательно для заполнения. Поле «Форма обучения» обязательно для заполнения. Поле «Год поступления» обязательно для заполнения. Поле «Год окончания обучения» обязательно для заполнения. Поле «Вид документа» обязательно для заполнения. Поле «Регистрационный номер диплома» обязательно для заполнения. Поле «Дата выдачи» обязательно для заполнения. Поле «Серия, номер диплома» обязательно для заполнения. Поле «Скан/фото диплома» обязательно для заполнения. Поле «По готовности документ будет получен» обязательно для заполнения. Поле «Персональные данные» обязательно для заполнения."
        )
