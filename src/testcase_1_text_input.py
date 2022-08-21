import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestCase1:

    URL = 'http://www.uitestingplayground.com/'

    # SEARCH_INPUT = (By.PARTIAL_LINK_TEXT, 'Text Input')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self):
        search_input = self.browser.find_element(By.LINK_TEXT, "Text Input")
        search_input.send_keys(Keys.RETURN)
        self.browser.implicitly_wait(10)

    def text_input(self, phrase):
        findField = self.browser.find_element(By.CLASS_NAME, 'form-control')
        findField.send_keys(phrase)
        self.browser.implicitly_wait(10)
        findBtn = self.browser.find_element(By.ID, "updatingButton")
        findBtn.send_keys(Keys.RETURN)
        return findBtn.text

    @pytest.mark.xfail
    def x_text_input(self, phrase):
        self.browser.refresh()
        findField = self.browser.find_element(By.CLASS_NAME, 'form-control')
        findField.send_keys(phrase)
        self.browser.implicitly_wait(10)
        findBtn = self.browser.find_element(By.ID, "updatingButton")
        findBtn.send_keys(Keys.RETURN)
        return findBtn.text