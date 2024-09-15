from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
import pytest
from locators.faq_page_locators import QuestionsPagesLocators
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class QuestionsPages:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    #ожидаем кнопку Заказать
    def wait_for_title_faq(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(QuestionsPagesLocators.order_header_button))

    #скролл до "Вопросы о важном"
    def scroll_question_title(self):
        question_title = self.driver.find_element(*QuestionsPagesLocators.question_title)
        self.driver.execute_script("arguments[0].scrollIntoView();", question_title)

    #метод кликает на 1 вопрос
    def click_question(self, question_locator):
        self.driver.find_element(*question_locator).click()

    #метод получает текст из ответа
    def get_text_answer(self, answer_locator):
        return self.driver.find_element(*answer_locator).text

    #шаг
    def question(self):
        self.click_question()
        self.get_text_answer()






