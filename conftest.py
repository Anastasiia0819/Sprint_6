import pytest
from selenium import webdriver
from src.config import Config


@pytest.fixture
def driver():
    firefox = webdriver.Firefox()
    firefox.maximize_window()
    firefox.get(Config.URL)
    yield firefox
    firefox.quit()



