from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Форма заказа самоката

    # Первая страница формы
    name_field = (By.XPATH, "//input[@placeholder = '* Имя']")
    last_name_field = (By.XPATH, "//input[@placeholder = '* Фамилия']")
    address_field = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")
    metro_station_field = (By.XPATH, "//input[@placeholder = '* Станция метро']")
    metro = (By.XPATH, ".//div[text() = 'Парк культуры']")
    telephone_field = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, "//button[text() = 'Далее']")

    # Вторая страница формы
    deliver_order_field = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    rent_period_field = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    rent_period_three_days = (By.XPATH, ".//div[text() = 'трое суток']")
    black_color_scooter_check = (By.ID, 'black')
    gray_color_scooter_check = (By.ID, 'grey')
    comment_field = (By.XPATH, ".//input[@placeholder= 'Комментарий для курьера']")
    back_button = (By.XPATH, ".//button[text() = 'Назад']")
    order_button = (By.XPATH, "(.//button[text() = 'Заказать'])[2]")

    # Подтверждение заказа
    no_button = (By.XPATH, ".//button[text() = 'Нет']")
    yes_button = (By.XPATH, ".//button[text() = 'Да']")

    # Окно заказа
    order_placed_text = (By.XPATH, ".//div[text() = 'Заказ оформлен']")
    view_status_button = (By.XPATH, ".//button[text() = 'Посмотреть статус']")