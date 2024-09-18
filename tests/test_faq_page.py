import pytest
from selenium import webdriver
from pages.main_page import MainPages
import time
from locators.main_page_locators import MainPagesLocators
import allure
from src.data import get_answer


class TestFaq:

    @pytest.mark.parametrize("question_locator, answer_locator, expected_answer",
                             [(MainPagesLocators.question_1, MainPagesLocators.answer_1_text, get_answer()[0]),
                              (MainPagesLocators.question_2, MainPagesLocators.answer_2_text, get_answer()[1]),
                              (MainPagesLocators.question_3, MainPagesLocators.answer_3_text, get_answer()[2]),
                              (MainPagesLocators.question_4, MainPagesLocators.answer_4_text, get_answer()[3]),
                              (MainPagesLocators.question_5, MainPagesLocators.answer_5_text, get_answer()[4]),
                              (MainPagesLocators.question_6, MainPagesLocators.answer_6_text, get_answer()[5]),
                              (MainPagesLocators.question_7, MainPagesLocators.answer_7_text, get_answer()[6]),
                              (MainPagesLocators.question_8, MainPagesLocators.answer_8_text, get_answer()[7])],
                             ids=[u"test_question_1", u"test_question_2", u"test_question_3", u"test_question_4", u"test_question_5", u"test_question_6", u"test_question_7", u"test_question_8"])
    @allure.title('Раздел: Вопросы о важном')
    def test_check_first_question(self, driver, question_locator, answer_locator, expected_answer):
        #создать объект класса раздела с вопросами
        faq_page = MainPages(driver)
        #ожидание загрузки кнопки Загрузка
        faq_page.wait_for_title_faq()
        #"скролл до загололвка"
        faq_page.scroll_question_title()
        #"клик и проверка на наличие ответа"
        faq_page.click_question(question_locator)
        #"Проверка текста ответа"
        actual_answer_text = faq_page.get_text_answer(answer_locator)
        assert actual_answer_text == expected_answer




