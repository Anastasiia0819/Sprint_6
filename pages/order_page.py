from selenium import webdriver
import pytest
from locators.order_page_locators import OrderPageLocators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    #клик на Заказать вверху страницы
    def click_order_header_button(self):
        self.driver.find_element(*OrderPageLocators.order_header_button).click()

    # клик на Заказать по середине страницы
    def click_order_middle_page_button(self):
        self.driver.find_element(*OrderPageLocators.order_middle_page_button).click()

    # заполнить поле "Имя"
    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.name_field).send_keys(name)

    #заполнить поле "Фамилия"
    def set_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.surname_field).send_keys(surname)

    # заполнить поле Станция метро
    def set_metro(self, metro):
        self.driver.find_element(*OrderPageLocators.metro_field).send_keys(metro)
        self.driver.find_element(*OrderPageLocators.choice_station_metro).click()

    # заполнить поле Номер телефона
    def set_telephone_number(self, number):
        self.driver.find_element(*OrderPageLocators.telephon_number_field).send_keys(number)

    # клик на Далее
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.next_button).click()

    # заполнить поле Когда привезти самокат
    def set_when_order(self, data_order):
        self.driver.find_element(*OrderPageLocators.when_order_field).send_keys(data_order)

    # заполнить поле срок аренды
    def set_rent_period(self):
        self.driver.find_element(*OrderPageLocators.rental_period_field).click()
        self.driver.find_element(*OrderPageLocators.choice_period).click()

    # клик на Заказать
    def click_order_next_button(self):
        self.driver.find_element(*OrderPageLocators.order_next_button)




