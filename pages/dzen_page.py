from pages.base_page import BasePage
from locators.dzen_page_locators import DzenPageLocators
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DzenPage(BasePage):
    @allure.step('Проверить, что кнопка "Главная" отображается на странице Дзен')
    def is_main_button_displayed(self):
        """Проверяет, отображается ли кнопка "Главная" на странице Дзен.
        Возвращает элемент, если он найден и видим в течение 5 секунд.
        """
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(DzenPageLocators.main_button_dzen)
        )