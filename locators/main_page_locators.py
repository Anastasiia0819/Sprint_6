from selenium.webdriver.common.by import By


class MainPagesLocators:

    main_title = (By.XPATH, ".//div[contains(@class, 'Home_Header__iJKdX')]") #заголовок "Самокат на пару дней"
    question_title = (By.XPATH, ".//div[contains (@class, 'Home_FourPart')]/div[contains (@class, 'Home_SubHeader')]") #заголовок "Вопросы о важном"
    list_question = (By.XPATH, ".//div[@class = 'accordion']")
    question_1 = (By.ID, 'accordion__heading-0') #первая стрелочка с вопросом
    answer_1_text = (By.XPATH, ".//div[@id = 'accordion__panel-0']/p")

    question_2 = (By.ID, "accordion__heading-1")
    answer_2_text = (By.XPATH, ".//div[@id = 'accordion__panel-1']/p")

    question_3 = (By.ID, "accordion__heading-2")
    answer_3_text = (By.XPATH, ".//div[@id = 'accordion__panel-2']/p")

    question_4 = (By.ID, "accordion__heading-3")
    answer_4_text = (By.XPATH, ".//div[@id = 'accordion__panel-3']/p")

    question_5 = (By.ID, "accordion__heading-4")
    answer_5_text = (By.XPATH, ".//div[@id = 'accordion__panel-4']/p")

    question_6 = (By.ID, "accordion__heading-5")
    answer_6_text = (By.XPATH, ".//div[@id = 'accordion__panel-5']/p")

    question_7 = (By.ID, "accordion__heading-6")
    answer_7_text = (By.XPATH, ".//div[@id = 'accordion__panel-6']/p")

    question_8 = (By.ID, "accordion__heading-7")
    answer_8_text = (By.XPATH, ".//div[@id = 'accordion__panel-7']/p")

    samokat_logo = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")  # лого Самокат
    yandex_logo = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]") #лого Яндекс
    logo_dzen = (By.XPATH, ".//a[@aria-label = 'Логотип Бренда']")
    permission_weather = By.XPATH, ".//div[@class ='Tooltip-Backdrop']"

    order_header_button = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[contains (@class, 'Button_Button')]") #кнопка "Заказать" в верху страницы
    order_middle_page_button = (By.XPATH, ".//button[contains(@class, 'Button_Middle') and contains(text(), 'Заказать')]" )#кнопка "Заказать" по середине страницы

