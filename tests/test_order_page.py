import pytest
from selenium import webdriver
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage
from pages.main_page import MainPages
from src.config import Config
import time
from src.helpers import get_random_data_for_order
import allure
from src.data import order_button, telephone_numbers


class TestOrderPage:

    @pytest.mark.parametrize("order_button_method", order_button,  ids=[u"Кнопка Заказать в хедере", u"Кнопка Заказать в середине страницы"])
    @pytest.mark.parametrize("telephone_number", telephone_numbers, ids=[u"Телефон: +79876665566", u"Телефон: 89109992233"])
    @allure.title("Оформление заказа")
    # Оформить заказ
    def test_order_page(self, driver, order_button_method, telephone_number):
        order_page = OrderPage(driver)
        main_page = MainPages(driver)
        main_page.open_main_page()
        #клик на заказать (сверху или по середине страницы)
        order_button_click = getattr(main_page, order_button_method)()
        current_url = main_page.get_current_url()
        expected_url = Config.URL_order
        assert current_url == expected_url
        name, surname, when_order_data = get_random_data_for_order()
        #ожидаем кноку Далее
        order_page.wait_next_button()
        #заполнить Имя
        order_page.set_name(name)
        # заполнить поле "Фамилия"
        order_page.set_surname(surname)
        # заполнить поле Станция метро и кликнуть в выпадающем списке
        order_page.set_metro("Выхино")
        #дождаться и кликнуть на соответсвующую станцию
        order_page.click_metro_station_on_list("Выхино")
        # заполнить поле Номер телефона
        order_page.set_telephone_number(telephone_number)
        # клик на Далее
        order_page.click_next_button()
        #ожидание кнопки Заказать (которая на странице "Про аренду")
        order_page.wait_order_nex_button()
        # заполнить поле Когда привезти самокат
        order_page.set_when_order(when_order_data)
        order_page.click_calendar()

        # заполнить поле срок аренды и клик на список сроков
        order_page.click_rent_period()

        order_page.wait_list_rent_options()
        order_page.click_rent_option()
        # клик на Заказать
        order_page.click_order_next_button()
        # ожидаем модальное окно для подтверждения заказа (кнопка Да)
        order_page.wait_yes_button()
        # клик на Да - подтверждение заказа
        order_page.click_yes_button()
        #ожидаем модальное окно с подтверждением заказа
        order_page.wait_modal_order_confirmation()
        assert order_page.get_test_order_confirmation() == "Заказ оформлен"




