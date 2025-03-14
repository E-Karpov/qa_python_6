import allure
from locators.main_page_locators import MainPageHeaderLocators, MainPageLocators
from pages.base_page import BasePage


class MainPageHeader(BasePage):
    @allure.step('Кликнуть по логотипу Яндекса')
    def click_yandex_logo(self):
        """Кликает по логотипу Яндекса в шапке страницы."""
        self.click_element(MainPageHeaderLocators.LOGO_YANDEX)

    @allure.step('Кликнуть по логотипу Самоката')
    def click_scooter_logo(self):
        """Кликает по логотипу Самоката в шапке страницы."""
        self.click_element(MainPageHeaderLocators.LOGO_SCOOTER)

    @allure.step('Кликнуть по кнопке "Заказать"')
    def click_order_button(self):
        """Кликает по кнопке 'Заказать' в шапке страницы."""
        self.click_element(MainPageHeaderLocators.ORDER_BUTTON)

    @allure.step('Кликнуть по кнопке "Статус заказа"')
    def click_order_status_button(self):
        """Кликает по кнопке 'Статус заказа' в шапке страницы."""
        self.click_element(MainPageHeaderLocators.ORDER_STATUS_BUTTON)

    @allure.step('Заполнить поле номера заказа')
    def fill_order_number_field(self, number):
        """Заполняет поле номера заказа на форме проверки статуса."""
        self.click_order_status_button()
        self.fill_field(MainPageHeaderLocators.NUMBER_ORDER_FIELD, number)

    @allure.step('Нажать кнопку "Go!"')
    def click_go_button(self):
        """Нажимает кнопку 'Go!' для проверки статуса заказа."""
        self.click_element(MainPageHeaderLocators.GO_BUTTON)

    @allure.step('Проверить статус заказа по номеру')
    def check_order_status(self, number):
        """Проверяет статус заказа по указанному номеру."""
        self.click_order_status_button()
        self.fill_order_number_field(number)
        self.click_go_button()

    @allure.step('Проверить, что заголовок "Учебный проект" отображается')
    def is_order_title_displayed(self):
        """Проверяет, отображается ли заголовок 'Учебный проект' на странице."""
        return self.wait_for_element_visibility(MainPageHeaderLocators.HEADER_PAGE_TITLE).is_displayed()

    @allure.step('Принять куки')
    def accept_cookies(self):
        """Принимает куки на странице."""
        self.click_element(MainPageLocators.ACCEPT_COOKIES_BUTTON)


class MainPage(BasePage):
    @allure.step('Принять куки на главной странице')
    def accept_cookies(self):
        """Принимает куки на главной странице."""
        self.click_element(MainPageLocators.ACCEPT_COOKIES_BUTTON)

    @allure.step('Скролл к кнопке "Заказать" и кликнуть на неё')
    def scroll_and_click_order_button(self):
        """Скроллит страницу к кнопке 'Заказать' и кликает по ней."""
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON)
        self.click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Скролл к разделу "Вопросы о важном"')
    def scroll_to_questions_section(self):
        """Скроллит страницу к разделу 'Вопросы о важном'."""
        self.scroll_to_element(MainPageLocators.QUESTIONS_TITLE)

    @allure.step('Кликнуть на вопрос в разделе "Вопросы о важном"')
    def click_question(self, question_button_locator):
        """Кликает на указанный вопрос в разделе 'Вопросы о важном'."""
        self.scroll_to_questions_section()
        self.click_element(question_button_locator)

    @allure.step('Получить текст ответа на вопрос')
    def get_answer_text(self, question_button_locator, answer_text_locator):
        """Возвращает текст ответа на выбранный вопрос."""
        self.click_question(question_button_locator)
        return self.get_element_text(answer_text_locator)