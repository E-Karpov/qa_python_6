import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Заполнить поле "Имя"')
    def fill_name(self, name):
        """Заполняет поле 'Имя' на форме заказа."""
        self.fill_field(OrderPageLocators.name_field, name)

    @allure.step('Заполнить поле "Фамилия"')
    def fill_last_name(self, last_name):
        """Заполняет поле 'Фамилия' на форме заказа."""
        self.fill_field(OrderPageLocators.last_name_field, last_name)

    @allure.step('Заполнить поле "Адрес"')
    def fill_address(self, address):
        """Заполняет поле 'Адрес' на форме заказа."""
        self.fill_field(OrderPageLocators.address_field, address)

    @allure.step('Выбрать станцию метро')
    def select_metro_station(self, station):
        """Выбирает станцию метро из выпадающего списка."""
        self.click_element(OrderPageLocators.metro_station_field)
        self.fill_field(OrderPageLocators.metro_station_field, station)
        self.click_element(OrderPageLocators.metro)

    @allure.step('Заполнить поле "Телефон"')
    def fill_phone(self, phone):
        """Заполняет поле 'Телефон' на форме заказа."""
        self.fill_field(OrderPageLocators.telephone_field, phone)

    @allure.step('Нажать кнопку "Далее"')
    def click_next(self):
        """Нажимает кнопку 'Далее' для перехода к следующему шагу."""
        self.click_element(OrderPageLocators.next_button)

    @allure.step('Заполнить форму "Для кого самокат"')
    def fill_user_info(self, user):
        """Заполняет все поля формы 'Для кого самокат' и переходит к следующему шагу."""
        self.fill_name(user[1])
        self.fill_last_name(user[2])
        self.fill_address(user[3])
        self.select_metro_station(user[4])
        self.fill_phone(user[5])
        self.click_next()

    @allure.step('Заполнить поле "Дата доставки"')
    def fill_delivery_date(self, date):
        """Заполняет поле 'Дата доставки' на форме аренды."""
        self.click_element(OrderPageLocators.deliver_order_field)
        self.fill_field(OrderPageLocators.deliver_order_field, date)

    @allure.step('Выбрать срок аренды')
    def select_rental_period(self):
        """Выбирает срок аренды из выпадающего списка."""
        self.click_element(OrderPageLocators.rent_period_field)
        self.click_element(OrderPageLocators.rent_period_three_days)

    @allure.step('Выбрать цвет самоката')
    def select_scooter_color(self):
        """Выбирает цвет самоката (например, черный)."""
        self.click_element(OrderPageLocators.black_color_scooter_check)

    @allure.step('Заполнить поле "Комментарий"')
    def fill_comment(self, comment):
        """Заполняет поле 'Комментарий' на форме аренды."""
        self.fill_field(OrderPageLocators.comment_field, comment)

    @allure.step('Нажать кнопку "Заказать"')
    def click_order(self):
        """Нажимает кнопку 'Заказать' для подтверждения заказа."""
        self.click_element(OrderPageLocators.order_button)

    @allure.step('Заполнить форму "Про аренду"')
    def fill_rent_info(self, rent_data):
        """Заполняет все поля формы 'Про аренду' и подтверждает заказ."""
        self.fill_delivery_date(rent_data[6])
        self.select_rental_period()
        self.select_scooter_color()
        self.fill_comment(rent_data[7])
        self.click_order()

    @allure.step('Нажать кнопку "Нет"')
    def click_no(self):
        """Нажимает кнопку 'Нет' для отмены заказа."""
        self.click_element(OrderPageLocators.no_button)

    @allure.step('Нажать кнопку "Да"')
    def click_yes(self):
        """Нажимает кнопку 'Да' для подтверждения заказа."""
        self.click_element(OrderPageLocators.yes_button)

    @allure.step('Оформить заказ')
    def complete_order(self, user):
        """Заполняет все формы и подтверждает заказ."""
        self.fill_user_info(user)
        self.fill_rent_info(user)
        self.click_yes()

    @allure.step('Проверить отображение подтверждения заказа')
    def is_order_confirmed(self):
        """Проверяет, отображается ли сообщение об успешном оформлении заказа."""
        return self.wait_for_element_visibility(OrderPageLocators.order_placed_text).is_displayed()