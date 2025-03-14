from pages.base_page import BasePage
from locators.dzen_page_locators import DzenPageLocators
import allure


class DzenPage(BasePage):
    @allure.step('Проверить, что кнопка "Главная" отображается на странице Дзен')
    def is_main_button_displayed(self):
        """Проверяет, отображается ли кнопка 'Главная' на странице Дзен."""
        return self.wait_for_element_visibility(DzenPageLocators.MAIN_BUTTON_DZEN).is_displayed()