from xml.sax.xmlreader import Locator

from pages.base_page import BasePage
from pages.common.element import Element


class RequestDiplomaPage(BasePage):
    """Represent `RequestDiploma` page."""
    base_url = "https://forms.sfu-kras.ru/podtverzhdenie-diploma"

    @property
    def logo(self) -> Locator:
        return self.page.get_by_role("heading", name="Запрос о подтверждении подлинности диплома")

    # Name
    last_name = Element(label="Фамилия *")
    first_name = Element(label="Имя *")
    surname = Element(label="Отчество *")
    previous_full_name = Element(label=("Предыдущее ФИО"))

    # Birthdate
    birth_day = Element(locator="#edit-submitted-data-rozhdeniya-day")
    birth_month = Element(locator="#edit-submitted-data-rozhdeniya-month")
    birth_year = Element(locator="#edit-submitted-data-rozhdeniya-year")

    # Contacts and other
    email = Element(label="E-mail *")
    phone = Element(label="Телефон *")
    university = Element(label="Институт/филиал СФУ *")
    specialty = Element(locator="#edit_submitted_napravlenie_select_chosen")

    correspondence_course = Element(text="Заочная", exact=True)
    full_time_course = Element(text="Очная", exact=True)
    half_cour = Element(text="Очно-заочная")

    admission_year = Element(label="Год поступления *")
    graduation_year = Element(label="Год окончания обучения *")

    document_type = Element(label="Вид документа *")
    diploma_registration = Element(label="Регистрационный номер диплома *")
    diploma_series = Element(label="Серия, номер диплома *")
    diploma_day = Element(locator="#edit-submitted-data-vydachi-day")
    diploma_month = Element(locator="#edit-submitted-data-vydachi-month")
    diploma_year = Element(locator="#edit-submitted-data-vydachi-year")

    personal_data_checkbox = Element(
        label="Я даю согласие на обработку моих персональных данных (Подробнее)"
    )

    @property
    def send_button(self) -> Locator:
        return self.page.get_by_role("button", name="Отправить запрос")
