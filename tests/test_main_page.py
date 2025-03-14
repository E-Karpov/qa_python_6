import allure
import pytest

from data import Questions, Urls
from locators.main_page_locators import MainPageHeaderLocators, MainPageLocators
from locators.dzen_page_locators import DzenPageLocators
from pages.main_page import MainPage, MainPageHeader
from pages.dzen_page import DzenPage


class TestMainPage:

    @allure.title('Проверка перехода на главную страницу Яндекс.Самокат через логотип "Самокат"')
    @allure.description('''
        Проверяем, что клик по логотипу "Самокат" в хедере возвращает на главную страницу Яндекс.Самокат.
        Ожидаем, что URL соответствует главной странице и отображается заголовок "Учебный проект".
    ''')
    def test_return_to_main_page_via_scooter_logo(self, driver):
        """
        Тест проверяет переход на главную страницу Яндекс.Самокат через логотип "Самокат".
        Шаги:
        1. Кликнуть на кнопку "Заказать" в хедере.
        2. Кликнуть на логотип "Самокат".
        3. Проверить, что текущий URL соответствует главной странице.
        4. Проверить, что отображается заголовок "Учебный проект".
        """
        header_page = MainPageHeader(driver)
        header_page.click_order_button()
        header_page.click_scooter_logo()
        current_url = header_page.get_current_url()
        title_is_displayed = header_page.is_order_title_displayed()
        assert current_url == Urls.MAIN_PAGE_URL and title_is_displayed

    @allure.title('Проверка перехода на главную страницу Дзен через логотип "Яндекс"')
    @allure.description('''
        Проверяем, что клик по логотипу "Яндекс" в хедере открывает главную страницу Дзен в новой вкладке.
        Ожидаем, что URL соответствует главной странице Дзен и отображается кнопка "Главная".
    ''')
    def test_redirect_to_dzen_via_yandex_logo(self, driver):
        """
        Тест проверяет переход на главную страницу Дзен через логотип "Яндекс".
        Шаги:
        1. Кликнуть на логотип "Яндекс" в хедере.
        2. Переключиться на новую вкладку.
        3. Проверить, что текущий URL соответствует главной странице Дзен.
        4. Проверить, что отображается кнопка "Главная".
        """
        header_page = MainPageHeader(driver)
        dzen_page = DzenPage(driver)
        header_page.click_yandex_logo()
        header_page.switch_to_new_tab()

        # Ожидаем загрузки страницы Дзен по наличию кнопки "Главная"
        dzen_page.wait_for_page_to_load(DzenPageLocators.MAIN_BUTTON_DZEN, timeout=20)

        current_url = header_page.get_current_url()
        assert current_url == Urls.DZEN_URL and dzen_page.is_main_button_displayed()

    @allure.title('Проверка корректности ответов в разделе "Вопросы о важном"')
    @allure.description('''
        Проверяем, что текст ответов в разделе "Вопросы о важном" соответствует ожидаемым значениям.
        Ожидаем, что каждый ответ совпадает с данными из Questions.expected_question_text.
    ''')
    @pytest.mark.parametrize('question_locator, question_text_locator, expected_question_text',
                             zip(MainPageLocators.QUESTIONS, MainPageLocators.QUESTIONS_TEXT, Questions.EXPECTED_QUESTION_TEXT))
    def test_faq_section_answers(self, driver, question_locator, question_text_locator, expected_question_text):
        """
        Тест проверяет корректность ответов в разделе "Вопросы о важном".
        Шаги:
        1. Принять куки.
        2. Для каждого вопроса:
           - Кликнуть на вопрос.
           - Получить текст ответа.
           - Проверить, что текст ответа соответствует ожидаемому.
        """
        home_page = MainPage(driver)
        home_page.accept_cookies()
        text = home_page.get_answer_text(question_locator, question_text_locator)
        assert text == expected_question_text