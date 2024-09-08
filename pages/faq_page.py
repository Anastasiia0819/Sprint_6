from selenium import webdriver
import pytest
from locators.faq_page_locators import QuestionsPagesLocators


class QuestionsPages:
    def __init__(self, driver):
        self.driver = driver

    #метод кликает на вопрос
    def click_question(self):
        self.driver.find_element(*QuestionsPagesLocators.question_1).click()

    #метод проверяет, есть ли корреткный текст
    def check_text_question(self):
        return self.driver.find_element(*QuestionsPagesLocators.answer_1_text).text

    #шаг
    def question(self):
        self.click_question()
        self.check_text_question()



