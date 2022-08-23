import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestCase2:

    URL = 'http://www.uitestingplayground.com/'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self):
        search_input = self.browser.find_element(By.LINK_TEXT, "Click")
        search_input.send_keys(Keys.RETURN)
        self.browser.implicitly_wait(10)

    # Positive
    def click(self):
        findField = self.browser.find_element(By.ID, 'badButton')
        findField.click()
        self.browser.implicitly_wait(10)
        return findField.get_attribute("class")

    # Negative

    @pytest.mark.xfail
    def x_click(self):
        pass
