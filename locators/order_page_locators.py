from selenium.webdriver.common.by import By

class OrderPageLocators:
    order_header_button = [By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[contains (@class, 'Button_Button')]"] #кнопка "Заказать" в верху страницы
    order_middle_page_button = [By.XPATH, './/div[contains(@class,"Home_FinishButton")]/button']#кнопка "Заказать" по середине страницы
    name_field = [By.XPATH, ".//input[@placeholder = '* Имя']"] #заполнить поле Имя
    surname_field = [By.XPATH, ".//input[@placeholder = '* Фамилия']"] #заполнить поле Фамилия
    adress_field = [By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"] #заполнить поле Адрес
    metro_field = [By.XPATH, ".//input[@placeholder = '* Станция метро']"] #заполнить поле Метро - ввести название станции ( .//input[@class="select-search__input"])
    choice_station_metro = [By.XPATH, f"//[@class='select-search__select']//[text()='{metro}']"] #
    telephon_number_field = [By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']"] #заполнить поле Номер телефона
    next_button = [By.XPATH, ".//div[contains(@class, 'Order_NextButton')]/button[contains(@class, 'Button_Button')]"] # кнопка "Далее" после заполнения данных покупателя
    about_rent_title = [By.XPATH, ".//div[contains(@class, 'Order_Header')]"] # заголовок "Про аренду"
    when_order_field = [By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"] #поле "Когда" вставить дату
    rental_period_field = [By.CLASS_NAME, "Dropdown-placeholder" ] #клик на поле срок аренды
    choice_period = [By.XPATH, ".//div[@class = 'Dropdown-option' and text()='сутки']"] #выбрать период
    collor_field = [By.ID, "black"] #выбор цвета самоката
    order_next_button = [By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button[text() = 'Заказать']"]#кнопка Заказать / подтверждение заполненных полей заказа
    modal_order_title = [By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]"] #залоголовк в модальном окне(для подтверждения заказа)
    yes_button = [By.XPATH, ".//button[text() = 'Да']"]# кнопка Да на модальном окне подтвеждения заказа
    order_done = [By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]"]#заказ оформлен (модальное окно) и текст "Заказ оформлен"
    samokat_logo = [By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]"] #лого Самокат
    yandex_logo = [By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]"]#лого Яндекс




