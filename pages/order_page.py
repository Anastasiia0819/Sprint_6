from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
import pytest
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
import allure
from pages.base_page import BasePage
from src.config import Config


class OrderPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("open page('https://qa-scooter.praktikum-services.ru/order')")
    #открыть страницу
    def open_page(self):
        self.navigate(Config.URL_order)


    #ожидаем кнопку Далее
    @allure.step("ожидаем кнопку Далее")
    def wait_next_button(self):
        self.wait_for_element_visible(OrderPageLocators.next_button)

    # заполнить поле "Имя"
    @allure.step("заполнить поле Имя")
    def set_name(self, name):
        self.enter_text(OrderPageLocators.name_field, name)

    #заполнить поле "Фамилия"
    @allure.step('заполнить поле "Фамилия"')
    def set_surname(self, surname):
        self.enter_text(OrderPageLocators.surname_field, surname)

    # заполнить поле Станция метро
    @allure.step("заполнить поле Станция метро")
    def set_metro(self, metro):
        self.enter_text(OrderPageLocators.metro_field, metro) #ввели название станции

    # Ожидание появления выпадающего списка и кликнуть на соответсвующую станцию
    @allure.step("Ожидание появления выпадающего списка и кликнуть на соответсвующую станцию")
    def click_metro_station_on_list(self, metro):
        list_metro_station = self.wait_for_elements_visible(OrderPageLocators.list_station)
        for station in list_metro_station:
            if station.text == metro:
                station.click() #кликнуть

    # заполнить поле Номер телефона
    @allure.step("заполнить поле Номер телефона")
    def set_telephone_number(self, number):
        self.enter_text(OrderPageLocators.telephon_number_field, number)

    # клик на Далее
    @allure.step("клик на Далее")
    def click_next_button(self):
        self.click_element(OrderPageLocators.next_button)

    #ожидание кнопки Заказать (которая на странице "Про аренду")
    @allure.step('ожидание кнопки Заказать (которая на странице "Про аренду")')
    def wait_order_nex_button(self):
        self.wait_for_element_visible(OrderPageLocators.order_next_button)

    # заполнить поле Когда привезти самокат
    @allure.step("заполнить поле Когда привезти самокат")
    def set_when_order(self, data_order):
        self.enter_text(OrderPageLocators.when_order_field, data_order)

    #клик на календарь
    @allure.step("клик на календарь")
    def click_calendar(self):
        self.click_element(OrderPageLocators.data_calendar)

    # клик на поле срок аренды
    @allure.step("клик на поле срок аренды")
    def click_rent_period(self):
        self.click_element(OrderPageLocators.rental_period_field)

    #ожидание списка с опциями срока аренды
    @allure.step("ожидание списка с опциями срока аренды")
    def wait_list_rent_options(self):
        self.wait_for_element_visible(OrderPageLocators.list_period_option)

    #кликнуть на одно из значений списка (например,"сутки")
    @allure.step('кликнуть на одно из значений списка (например,"сутки")')
    def click_rent_option(self):
        self.click_element(OrderPageLocators.choice_period)

    # клик на Заказать
    @allure.step("клик на Заказать")
    def click_order_next_button(self):
        self.click_element(OrderPageLocators.order_next_button)

    #ожидаем модальное окно для подтверждения заказа (кнопка Да)
    @allure.step("ожидаем модальное окно для подтверждения заказа (кнопка Да)")
    def wait_yes_button(self):
        self.wait_for_element_visible(OrderPageLocators.yes_button)

    # клик на Да
    @allure.step("клик на Да")
    def click_yes_button(self):
        self.click_element(OrderPageLocators.yes_button)

    #ожидание загрузки модального окна с подтвеждением заказа
    @allure.step("ожидание загрузки модального окна с подтвеждением заказа")
    def wait_modal_order_confirmation(self):
        self.wait_for_element_visible(OrderPageLocators.order_done)

    #получить текст "Заказ оформлен"
    @allure.step('получить текст "Заказ оформлен"')
    def get_test_order_confirmation(self):
        full_order_done_text = self.find_element(OrderPageLocators.order_done).text
        print(f"Текст, найденный на странице: {full_order_done_text}")
        text_for_check = full_order_done_text.splitlines()[0]
        return text_for_check





