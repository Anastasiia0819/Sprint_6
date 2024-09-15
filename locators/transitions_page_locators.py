from selenium.webdriver.common.by import By


class TransitionsPageLocators:
    samokat_logo = [By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]"] #лого Самокат
    yandex_logo = [By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]"]#лого Яндекс
    search_field = [By.XPATH, ".//a[@aria-label = 'Логотип Бренда']"] #поисковая строка на дзене