#тесты на переходы на другие страницы
import allure
import pytest
from selenium import webdriver
from locators.transitions_page_locators import TransitionsPageLocators
from pages.trabsitions_page import TransitionsPage
from src.config import Config
import time
import allure


class TestTransitionsPage:
    @allure.feature("Переходы на страницы")
    def test_transition_yandex_dzen(self, driver):
        transition_page_yandex = TransitionsPage(driver)
        with allure.step("Переход на страницу Дзена по клику на лого Яндекс"):
            transition_page_yandex.redirect_tab_dzen()
        with allure.step("Проверка, что открылась страница Дзена"):
            transition_page_yandex.wait_open_new_tab()
            assert driver.current_url == Config.URL_dzen, f"Ожидался URL: {Config.URL_dzen}, но был: {driver.current_url}"

    @allure.feature("Переходы на страницы")
    def test_transition_logo_samokat(self, driver):
        transition_page_samokat = TransitionsPage(driver)
        with allure.step("Открыть страницу Заказа"):
            driver.get(f"{Config.URL}order")
            time.sleep(3)
        with allure.step("Клик на лого Самокат"):
            transition_page_samokat.click_logo_samokat()
            time.sleep(3)
        with allure.step("Проверка, что переход на главную страницу"):
            assert driver.current_url == Config.URL









