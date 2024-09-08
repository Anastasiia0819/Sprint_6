from selenium.webdriver.common.by import By


class QuestionsPagesLocators:
    question_title = [By.XPATH, ".//div[contains (@class, 'Home_FourPart')]/div[contains (@class, 'Home_SubHeader')]"] #заголовок "Вопросы о важном"
    question_1 = [By.ID, 'accordion__heading-0'] #первая стрелочка с вопросом
    answer_1_text = [By.ID, ".//div[@id = 'accordion__panel-8']/p"]
    question_2 = [By.ID, "accordion__heading-1"]
    answer_2_text = [By.ID, ".//div[@id = 'accordion__panel-9']/p"]
    question_3 = [By.ID, "accordion__heading-2"]
    answer_3_text = [By.ID, ".//div[@id = 'accordion__panel-10']/p"]
    question_4 = [By.ID, "accordion__heading-3"]
    answer_4_text = [By.ID, ".//div[@id = 'accordion__panel-11']/p"]
    question_5 = [By.ID, "accordion__heading-4"]
    answer_5_text = [By.ID, ".//div[@id = 'accordion__panel-12']/p"]
    question_6 = [By.ID, "accordion__heading-5"]
    answer_6_text = [By.ID, ".//div[@id = 'accordion__panel-13']/p"]
    question_7 = [By.ID, "accordion__heading-6"]
    answer_7_text = [By.ID, ".//div[@id = 'accordion__panel-14']/p"]
    question_8 = [By.ID, "accordion__heading-7"]
    answer_8_text = [By.ID, ".//div[@id = 'accordion__panel-15']/p"]
