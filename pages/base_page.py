from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Возвращает текущий URL страницы."""
        return self.driver.current_url

    def wait_for_element_visibility(self, locator):
        """Ожидает, пока элемент станет видимым на странице"""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def click_element(self, locator):
        """Кликает по элементу, найденному по локатору"""
        self.wait_for_element_visibility(locator).click()

    def fill_field(self, locator, text):
        """Вводит текст в поле, найденное по локатору"""
        self.wait_for_element_visibility(locator).send_keys(text)

    def get_element_text(self, locator):
        """Возвращает текст элемента, найденного по локатору"""
        return self.wait_for_element_visibility(locator).text

    def scroll_to_element(self, locator):
        """Скроллит страницу к элементу, найденному по локатору"""
        element = self.wait_for_element_visibility(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_new_tab(self):
        """Переключает драйвер на новую вкладку браузера"""
        self.driver.switch_to.window(self.driver.window_handles[1])

    def is_element_visible(self, locator):
        """Проверяет, видим ли элемент на странице"""
        return self.wait_for_element_visibility(locator).is_displayed()