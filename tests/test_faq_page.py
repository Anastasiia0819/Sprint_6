import pytest
from selenium import webdriver
from pages.faq_page import QuestionsPages
import time
from locators.faq_page_locators import QuestionsPagesLocators
import allure


class TestFaq:

    @pytest.mark.parametrize("question_locator, answer_locator, expected_answer",
                             [(QuestionsPagesLocators.question_1, QuestionsPagesLocators.answer_1_text, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
                              (QuestionsPagesLocators.question_2, QuestionsPagesLocators.answer_2_text, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
                              (QuestionsPagesLocators.question_3, QuestionsPagesLocators.answer_3_text, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
                              (QuestionsPagesLocators.question_4, QuestionsPagesLocators.answer_4_text, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
                              (QuestionsPagesLocators.question_5, QuestionsPagesLocators.answer_5_text, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
                              (QuestionsPagesLocators.question_6, QuestionsPagesLocators.answer_6_text, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
                              (QuestionsPagesLocators.question_7, QuestionsPagesLocators.answer_7_text, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
                              (QuestionsPagesLocators.question_8, QuestionsPagesLocators.answer_8_text, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")],
                             ids=[u"Тест вопроса 1", u"Тест вопроса 2", u"Тест вопроса 3", u"Тест вопроса 4", u"Тест вопроса 5", u"Тест вопроса 6", u"Тест вопроса 7", u"Тест вопроса 8"])

    @allure.feature('Раздел: Вопросы о важном')
    def test_check_first_question(self, driver, question_locator, answer_locator, expected_answer):
        #создать объект класса раздела с вопросами
        faq_page = QuestionsPages(driver)
        with allure.step("ожидание загрузки кнопки Загрузка"):
            faq_page.wait_for_title_faq()
        with allure.step("скролл до загололвка"):
            faq_page.scroll_question_title()
        time.sleep(3)

        with allure.step("клик и проверка на наличие ответа"):
            faq_page.click_question(question_locator)
        time.sleep(3)
        with allure.step("Проверка текста ответа"):
            actual_answer_text = faq_page.get_text_answer(answer_locator)
            assert actual_answer_text == expected_answer




