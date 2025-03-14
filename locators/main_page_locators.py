from selenium.webdriver.common.by import By


class MainPageHeaderLocators:
    # Хедер
    LOGO_YANDEX = (By.XPATH, ".//a[@class = 'Header_LogoYandex__3TSOI']")
    LOGO_SCOOTER = (By.XPATH, ".//a[@class = 'Header_LogoScooter__3lsAR']")
    ORDER_BUTTON = (By.XPATH, "(.//button[text() = 'Заказать'])[1]")
    ORDER_STATUS_BUTTON = (By.XPATH, ".//button[text() = 'Статус заказа']")
    NUMBER_ORDER_FIELD = (By.XPATH, ".//input[@class = 'Input_Input__1iN_Z Header_Input__xIoUq']")
    GO_BUTTON = (By.XPATH, ".//button[text() = 'Go!']")
    TRACK_FIELD = (By.XPATH, ".//input[@placeholder='Введите номер заказа']")
    VIEW_BUTTON = (By.XPATH, ".//button[text() = 'Посмотреть']")
    HEADER_PAGE_TITLE = (By.XPATH, ".//div[text() = 'Учебный тренажер']")


class MainPageLocators:
    # Главная страница Яндекс Самокат
    HOME_PAGE_TITLE = (By.XPATH, ".//div[@class = 'Home_Header__iJKdX']")
    ORDER_BUTTON = (By.XPATH, "(//button[text() = 'Заказать'])[2]")
    ACCEPT_COOKIES_BUTTON = (By.XPATH, "//button[@id = 'rcc-confirm-button']")
    QUESTIONS_TITLE = (By.XPATH, "//div[text() = 'Вопросы о важном']")

    # Вопросы о важном
    QUESTIONS = [
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
    QUESTIONS_TEXT = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")
    ]