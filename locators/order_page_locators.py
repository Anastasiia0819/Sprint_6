from selenium.webdriver.common.by import By


class OrderPageLocators:
    order_header_button = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[contains (@class, 'Button_Button')]") #кнопка "Заказать" в верху страницы
    order_middle_page_button = (By.XPATH, ".//button[contains(@class, 'Button_Middle') and contains(text(), 'Заказать')]") #кнопка "Заказать" по середине страницы
    name_field = (By.XPATH, ".//input[@placeholder = '* Имя']") #заполнить поле Имя
    surname_field = (By.XPATH, ".//input[@placeholder = '* Фамилия']") #заполнить поле Фамилия
    adress_field = (By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']") #заполнить поле Адрес
    metro_field = (By.XPATH, ".//input[@placeholder = '* Станция метро']") #заполнить поле Метро - ввести название станции ( .//input[@class="select-search__input"])
    list_station = (By.XPATH, "//div[@class='select-search__select']")
    choice_station_metro = (By.XPATH, "//div[@class='select-search__select']//[text()='Выхино']") #клик на введнную станцию
    telephon_number_field = (By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']") #заполнить поле Номер телефона
    next_button = (By.XPATH, ".//div[contains(@class, 'Order_NextButton')]/button[contains(@class, 'Button_Button')]") # кнопка "Далее" после заполнения данных покупателя
    about_rent_title = (By.XPATH, ".//div[contains(@class, 'Order_Header')]") # заголовок "Про аренду"
    when_order_field = (By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']") #поле "Когда" вставить дату
    data_calendar = (By.XPATH, ".//div[contains(@class, 'react-datepicker__day--015')]")
    rental_period_field = (By.XPATH, ".//div[@class = 'Dropdown-root']") #клик на поле срок аренды
    list_period_option = (By.CLASS_NAME, "Dropdown-menu") #лист с перечнем опций для срока аренды
    choice_period = (By.XPATH, ".//div[@class = 'Dropdown-option' and text()='сутки']") #выбрать период
    collor_field = (By.ID, "black") #выбор цвета самоката
    order_next_button = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button[text() = 'Заказать']")#кнопка Заказать / подтверждение заполненных полей заказа
    modal_order_confirmation_title = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]") #залоголовк в модальном окне(для подтверждения заказа)
    yes_button = (By.XPATH, ".//button[text() = 'Да']")# кнопка Да на модальном окне подтвеждения заказа
    order_done = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")#заказ оформлен (модальное окно) и текст "Заказ оформлен"




