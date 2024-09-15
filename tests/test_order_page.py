import pytest
from selenium import webdriver
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage
from src.config import Config
import time
from src.helpers import get_random_data_for_order


class TestOrderPage:

    order_button = ["click_order_header_button",
                    "click_order_middle_page_button"]
    telephone_number = ["+79876665566", "89109992233"]

    @pytest.mark.parametrize("order_button_method", order_button)
    @pytest.mark.parametrize("telephone_number", telephone_number)

    # Оформить заказ
    def test_order_page(self, driver, order_button_method, telephone_number):
        order_page = OrderPage(driver)

        #клик на заказать (сверху или по середине страницы)
        order_button_click = getattr(order_page, order_button_method)()
        assert driver.current_url == f'{Config.URL}order'
        name, surname, when_order_data = get_random_data_for_order()
        time.sleep(3)

        #ожидаем кноку Далее
        order_page.wait_next_button()

        #заполнить Имя
        order_page.set_name(name)
        # заполнить поле "Фамилия"
        order_page.set_surname(surname)
        # заполнить поле Станция метро и кликнуть в выпадающем списке
        time.sleep(3)
        order_page.set_metro("Выхино")
        time.sleep(3)
        #дождаться и кликнуть на соответсвующую станцию
        order_page.click_metro_station_on_list("Выхино")
        # заполнить поле Номер телефона
        order_page.set_telephone_number(telephone_number)
        time.sleep(3)
        # клик на Далее
        order_page.click_next_button()
        #ожидание кнопки Заказать (которая на странице "Про аренду")
        order_page.wait_order_nex_button()

        # заполнить поле Когда привезти самокат
        order_page.set_when_order(when_order_data)
        time.sleep(3)
        order_page.click_calendar()

        # заполнить поле срок аренды и клик на список сроков
        order_page.click_rent_period()

        order_page.wait_list_rent_options()
        order_page.click_rent_option()
        time.sleep(3)
        # клик на Заказать
        order_page.click_order_next_button()
        # ожидаем модальное окно для подтверждения заказа (кнопка Да)
        order_page.wait_yes_button()
        time.sleep(3)

        # клик на Да
        order_page.click_yes_button()
        #ожидаем модальное окно с подтверждением заказа
        order_page.wait_modal_order_confirmation()
        assert order_page.get_test_order_confirmation() == "Заказ оформлен"




