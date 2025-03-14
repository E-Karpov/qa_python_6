import allure
import pytest
from selenium import webdriver

from data import Urls


@allure.step('Открытие браузера / переход на страницу сервиса / закрытие браузера')
@pytest.fixture
def driver():
    """
    Фикстура для инициализации драйвера и открытия главной страницы сервиса.
    После завершения теста браузер закрывается.
    """
    driver = webdriver.Firefox()  # Инициализация драйвера Firefox
    driver.get(Urls.MAIN_PAGE_URL)  # Переход на главную страницу сервиса
    yield driver  # Возврат драйвера для использования в тестах
    driver.quit()  # Закрытие браузера после завершения теста


# Для корректного отображения аргументов в параметризированном тесте
def pytest_make_parametrize_id(val):
    """
    Функция для корректного отображения аргументов в параметризированных тестах.
    :param val: Значение параметра.
    :return: Строковое представление значения.
    """
    return repr(val)