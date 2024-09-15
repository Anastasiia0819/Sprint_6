from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
import pytest
from locators.transitions_page_locators import TransitionsPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TransitionsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    #клик на логотип Самокат
    def click_logo_samokat(self):
        self.driver.find_element(*TransitionsPageLocators.samokat_logo).click()

    # клик на логотип Яндекс
    def click_logo_yandex(self):
        self.driver.find_element(*TransitionsPageLocators.yandex_logo).click()

    # Переключение на новую вкладку
    def redirect_tab_dzen(self):
        #Получаем список всех вкладок
        window_handles = self.driver.window_handles
        # исходное окно
        original_window = self.driver.current_window_handle
        #убедиться, что нет уже открытых окон
        assert len(self.driver.window_handles) == 1
        #клик на лого яндекса
        self.driver.find_element(*TransitionsPageLocators.yandex_logo).click()
        #ожидание 2-ой вкладки
        WebDriverWait(self.driver, 30).until(expected_conditions.number_of_windows_to_be(2))
        #Проходим цикл, пока не найдем новое окно
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

    #ожидание редиректа (проаверка лого)
    def wait_open_new_tab(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(TransitionsPageLocators.search_field))


