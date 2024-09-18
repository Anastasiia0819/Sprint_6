import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    # Получение текущего URL страницы
    def get_current_url_base(self):
        return self.driver.current_url

    #проверка наличия элемента
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    def click_element(self, locator, timeout=10):
        self.find_element(locator, timeout).click()

    #вставить текст в поле
    def enter_text(self, locator, text, timeout=10):
        self.find_element(locator, timeout).send_keys(text)

    #ожидание элемента
    def wait_for_element_visible(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

        # ожидание элементов
    def wait_for_elements_visible(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_all_elements_located(locator))

    #ожидание 2-ой вкладки
    def wait_number_of_windows_to_be(self, number=2, timeout=30):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.number_of_windows_to_be(number))

    def wait_element_to_be_clickable(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    #переключение на др. вкладку
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    #скролл
    def scroll(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    #редирект на вкладку
    def redirect_tab(self, locator, timeout=30):
        # Получаем список всех вкладок
        window_handles = self.driver.window_handles
        # исходное окно
        original_window = self.driver.current_window_handle
        # убедиться, что нет уже открытых окон
        assert len(self.driver.window_handles) == 1
        # клик на лого яндекса
        #self.driver.find_element(*MainPagesLocators.yandex_logo).click()
        self.click_element(locator, timeout)
        # ожидание 2-ой вкладки
        #WebDriverWait(self.driver, 30).until(expected_conditions.number_of_windows_to_be(2))
        self.wait_number_of_windows_to_be()
        # Проходим цикл, пока не найдем новое окно
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.switch_to_window(window_handle)
                break

    def wait_for_element_visible_1(self, locator, timeout=30):
        try:
            return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException as e:
            print(f"TimeoutException: Element with locator {locator} not found.")
            raise
