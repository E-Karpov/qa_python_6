import allure
from data import Users
from pages.main_page import MainPage, MainPageHeader
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка оформления заказа через кнопку "Заказать" на главной странице')
    @allure.description('''
        Проверяем успешное оформление заказа с использованием данных пользователя user_2.
        Заказ оформляется через кнопку "Заказать" на главной странице.
        Ожидаем, что после подтверждения заказа отобразится сообщение об успешном оформлении.
    ''')
    def test_order_placement_via_main_page_button(self, driver):
        """
        Тест проверяет успешное оформление заказа через кнопку "Заказать" на главной странице.
        Шаги:
        1. Принять куки.
        2. Скролл к кнопке "Заказать" и кликнуть на неё.
        3. Заполнить все поля формы заказа данными пользователя user_2.
        4. Подтвердить заказ.
        5. Проверить, что отображается сообщение об успешном оформлении заказа.
        """
        home_page = MainPage(driver)
        order_page = OrderPage(driver)
        home_page.accept_cookies()
        home_page.scroll_and_click_order_button()
        order_page.complete_order(Users.USER_2)
        assert order_page.is_order_confirmed()

    @allure.title('Проверка оформления заказа через кнопку "Заказать" в хедере')
    @allure.description('''
        Проверяем успешное оформление заказа с использованием данных пользователя user_1.
        Заказ оформляется через кнопку "Заказать" в хедере.
        Ожидаем, что после подтверждения заказа отобразится сообщение об успешном оформлении.
    ''')
    def test_order_placement_via_header_button(self, driver):
        """
        Тест проверяет успешное оформление заказа через кнопку "Заказать" в хедере.
        Шаги:
        1. Принять куки.
        2. Кликнуть на кнопку "Заказать" в хедере.
        3. Заполнить все поля формы заказа данными пользователя user_1.
        4. Подтвердить заказ.
        5. Проверить, что отображается сообщение об успешном оформлении заказа.
        """
        header_page = MainPageHeader(driver)
        order_page = OrderPage(driver)
        header_page.accept_cookies()
        header_page.click_order_button()
        order_page.complete_order(Users.USER_1)
        assert order_page.is_order_confirmed()