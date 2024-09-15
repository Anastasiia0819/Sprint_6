#тесты на переходы на другие страницы

import pytest
from selenium import webdriver
from locators.transitions_page_locators import TransitionsPageLocators
from pages.trabsitions_page import TransitionsPage
from src.config import Config
import time


class TestTransitionsPage:

    def test_transition_yandex_dzen(self, driver):
        transition_page_yandex = TransitionsPage(driver)
        transition_page_yandex.redirect_tab_dzen()
        transition_page_yandex.wait_open_new_tab()
        assert driver.current_url == Config.URL_dzen, f"Ожидался URL: {Config.URL_dzen}, но был: {driver.current_url}"

    def test_transition_logo_samokat(self, driver):
        transition_page_samokat = TransitionsPage(driver)
        driver.get(f"{Config.URL}order")
        time.sleep(3)
        transition_page_samokat.click_logo_samokat()
        time.sleep(3)
        assert driver.current_url == Config.URL









