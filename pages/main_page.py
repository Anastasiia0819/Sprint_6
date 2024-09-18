from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
import pytest
from locators.main_page_locators import MainPagesLocators
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from pages.base_page import BasePage
from src.config import Config


class MainPages(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    #Открытие главной страницы
    @allure.step('open main page("https://qa-scooter.praktikum-services.ru/")')
    def open_main_page(self):
        self.navigate(Config.URL)

    def get_current_url(self):
        return self.get_current_url_base()

    #ожидаем кнопку Заказать
    @allure.step("ожидание загрузки кнопки Загрузка")
    def wait_for_title_faq(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(MainPagesLocators.order_header_button))

    #скролл до "Вопросы о важном"
    @allure.step("скролл до загололвка")
    def scroll_question_title(self):
        question_title = self.find_element(MainPagesLocators.question_title)
        self.scroll(question_title)
        self.wait_for_element_visible(MainPagesLocators.question_title)
        self.wait_for_elements_visible(MainPagesLocators.list_question)

    #метод кликает на вопрос
    @allure.step("клик и проверка на наличие ответа")
    def click_question(self, question_locator):
        self.wait_for_element_visible(question_locator)
        self.click_element(question_locator)

    #метод получает текст из ответа
    @allure.step("Проверка текста ответа")
    def get_text_answer(self, answer_locator):
        return self.find_element(answer_locator).text


        # клик на логотип Самокат
    @allure.step("клик на логотип Самокат")
    def click_logo_samokat(self):
        self.click_element(MainPagesLocators.samokat_logo)

        # клик на логотип Яндекс
    @allure.step("клик на логотип Яндекс")
    def click_logo_yandex(self):
        self.click_element(MainPagesLocators.yandex_logo)

        # Переключение на новую вкладку Дзен
    @allure.step("Переключение на новую вкладку Дзен")
    def redirect_tab_dzen(self):
        self.redirect_tab(MainPagesLocators.yandex_logo)

        # ожидание редиректа (проверка лого)
    @allure.step("ожидание редиректа (проверка лого)")
    def wait_open_new_tab(self):
        self.wait_for_element_visible(MainPagesLocators.logo_dzen)

    #клик на Заказать вверху страницы
    @allure.step("клик на Заказать вверху страницы")
    def click_order_header_button(self):
        self.click_element(MainPagesLocators.order_header_button)

    # клик на Заказать по середине страницы
    @allure.step("клик на Заказать по середине страницы")
    def click_order_middle_page_button(self):
        order_middle_page_button = self.find_element(MainPagesLocators.order_middle_page_button)
        self.scroll(order_middle_page_button)
        self.wait_for_element_visible(MainPagesLocators.order_middle_page_button)
        self.wait_element_to_be_clickable(MainPagesLocators.order_middle_page_button)
        order_middle_page_button.click()








