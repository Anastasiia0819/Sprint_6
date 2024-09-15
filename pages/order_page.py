from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
import pytest
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class OrderPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    #клик на Заказать вверху страницы
    def click_order_header_button(self):
        self.driver.find_element(*OrderPageLocators.order_header_button).click()

    # клик на Заказать по середине страницы
    def click_order_middle_page_button(self):
        order_middle_page_button = self.driver.find_element(*OrderPageLocators.order_middle_page_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", order_middle_page_button)
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(OrderPageLocators.order_middle_page_button))
        order_middle_page_button.click()

    #ожидаем кнопку Далее
    def wait_next_button(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(OrderPageLocators.next_button))

    # заполнить поле "Имя"
    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.name_field).send_keys(name)

    #заполнить поле "Фамилия"
    def set_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.surname_field).send_keys(surname)

    # заполнить поле Станция метро
    def set_metro(self, metro):
        self.driver.find_element(*OrderPageLocators.metro_field).send_keys(metro) #ввели название станции

    # Ожидание появления выпадающего списка и кликнуть на соответсвующую станцию
    def click_metro_station_on_list(self, metro):
        list_metro_station = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_all_elements_located(OrderPageLocators.list_station))
        for station in list_metro_station:
            if station.text == metro:
                station.click() #кликнуть

    # заполнить поле Номер телефона
    def set_telephone_number(self, number):
        self.driver.find_element(*OrderPageLocators.telephon_number_field).send_keys(number)

    # клик на Далее
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.next_button).click()

    #ожидание кнопки Заказать (которая на странице "Про аренду")
    def wait_order_nex_button(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(OrderPageLocators.order_next_button))

    # заполнить поле Когда привезти самокат
    def set_when_order(self, data_order):
        self.driver.find_element(*OrderPageLocators.when_order_field).send_keys(data_order)

    #клик на календарь
    def click_calendar(self):
        self.driver.find_element(*OrderPageLocators.data_calendar).click()

    # клик на поле срок аренды
    def click_rent_period(self):
        #rent_field = self.driver.find_element(*OrderPageLocators.rental_period_field)
        #self.driver.execute_script("arguments[0].click();", rent_field)
        self.driver.find_element(*OrderPageLocators.rental_period_field).click()

    #ожидание списка с опциями срока аренды
    def wait_list_rent_options(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_all_elements_located(OrderPageLocators.list_period_option))

    #кликнуть на одно из значений списка (например,"сутки")
    def click_rent_option(self):
        self.driver.find_element(*OrderPageLocators.choice_period).click()

    # клик на Заказать
    def click_order_next_button(self):
        self.driver.find_element(*OrderPageLocators.order_next_button).click()

    #ожидаем модальное окно для подтверждения заказа (кнопка Да)
    def wait_yes_button(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(OrderPageLocators.yes_button))

    # клик на Да
    def click_yes_button(self):
        self.driver.find_element(*OrderPageLocators.yes_button).click()

    #ожидание загрузки модального окна с подтвеждением заказа
    def wait_modal_order_confirmation(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(OrderPageLocators.order_done))

    #получить текст "Заказ оформлен"
    def get_test_order_confirmation(self):
        full_order_done_text = self.driver.find_element(*OrderPageLocators.order_done).text
        print(f"Текст, найденный на странице: {full_order_done_text}")
        text_for_check = full_order_done_text.splitlines()[0]
        return text_for_check

    #клик на логотип Самокат
    def click_logo_samokat(self):
        self.driver.find_element(*OrderPageLocators.samokat_logo).click()

    # клик на логотип Яндекс
    def click_logo_yandex(self):
        self.driver.find_element(*OrderPageLocators.yandex_logo).click()



