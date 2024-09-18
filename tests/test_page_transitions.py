#тесты на переходы на другие страницы

import allure
import pytest
from selenium import webdriver
from locators.main_page_locators import MainPagesLocators
from pages.main_page import MainPages
from pages.order_page import OrderPage
from src.config import Config
import time
import allure


class TestTransitionsPage:
    @allure.title("Переходы на страницы")
    def test_transition_yandex_dzen(self, driver):
        transition_page_yandex = MainPages(driver)
        #Переход на страницу Дзена по клику на лого Яндекс
        transition_page_yandex.redirect_tab_dzen()
        #"Проверка, что открылась страница Дзена"
        transition_page_yandex.wait_open_new_tab()
        current_url = driver.current_url
        assert transition_page_yandex.get_current_url() == Config.URL_dzen

    @allure.title("Переходы на страницы")
    def test_transition_logo_samokat(self, driver):
        transition_page_samokat = MainPages(driver)
        order_page = OrderPage(driver)
        #"Открыть страницу Заказа"
        order_page.open_page()
        #"Клик на лого Самокат"
        transition_page_samokat.click_logo_samokat()
        #"Проверка, что переход на главную страницу"
        assert transition_page_samokat.get_current_url_base() == Config.URL









