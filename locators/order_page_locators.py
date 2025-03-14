from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Форма заказа самоката

    # Первая страница формы
    NAME_FIELD = (By.XPATH, "//input[@placeholder = '* Имя']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder = '* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD = (By.XPATH, "//input[@placeholder = '* Станция метро']")
    METRO = (By.XPATH, ".//div[text() = 'Парк культуры']")
    TELEPHONE_FIELD = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text() = 'Далее']")

    # Вторая страница формы
    DELIVER_ORDER_FIELD = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD_FIELD = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    RENT_PERIOD_THREE_DAYS = (By.XPATH, ".//div[text() = 'трое суток']")
    BLACK_COLOR_SCOOTER_CHECK = (By.ID, 'black')
    GRAY_COLOR_SCOOTER_CHECK = (By.ID, 'grey')
    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder= 'Комментарий для курьера']")
    BACK_BUTTON = (By.XPATH, ".//button[text() = 'Назад']")
    ORDER_BUTTON = (By.XPATH, "(.//button[text() = 'Заказать'])[2]")

    # Подтверждение заказа
    NO_BUTTON = (By.XPATH, ".//button[text() = 'Нет']")
    YES_BUTTON = (By.XPATH, ".//button[text() = 'Да']")

    # Окно заказа
    ORDER_PLACED_TEXT = (By.XPATH, ".//div[text() = 'Заказ оформлен']")
    VIEW_STATUS_BUTTON = (By.XPATH, ".//button[text() = 'Посмотреть статус']")