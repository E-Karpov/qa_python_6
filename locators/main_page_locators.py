from selenium.webdriver.common.by import By


class MainPageHeaderLocators:
    # Хедер
    logo_yandex = (By.XPATH, ".//a[@class = 'Header_LogoYandex__3TSOI']")
    logo_scooter = (By.XPATH, ".//a[@class = 'Header_LogoScooter__3lsAR']")
    order_button = (By.XPATH, "(.//button[text() = 'Заказать'])[1]")
    order_status_button = (By.XPATH, ".//button[text() = 'Статус заказа']")
    number_order_field = (By.XPATH, ".//input[@class = 'Input_Input__1iN_Z Header_Input__xIoUq']")
    go_button = (By.XPATH, ".//button[text() = 'Go!']")
    track_field = (By.XPATH, ".//input[@placeholder='Введите номер заказа']")
    view_button = (By.XPATH, ".//button[text() = 'Посмотреть']")
    header_page_title = (By.XPATH, ".//div[text() = 'Учебный тренажер']")


class MainPageLocators:
    # Главная страница Яднекс.Самокат
    home_page_title = (By.XPATH, ".//div[@class = 'Home_Header__iJKdX']")
    order_button = (By.XPATH, "(//button[text() = 'Заказать'])[2]")
    accept_cookies_button = (By.XPATH, "//button[@id = 'rcc-confirm-button']")
    questions_title = (By.XPATH, "//div[text() = 'Вопросы о важном']")

    # Вопросы о важном
    questions = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
    ]

    # Ответы на "Вопросы о важном"
    questions_text = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")
    ]