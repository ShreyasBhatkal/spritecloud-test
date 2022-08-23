import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestCase3:

    URL = 'http://www.uitestingplayground.com/'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self):
        search_input = self.browser.find_element(By.LINK_TEXT, "AJAX Data")
        search_input.send_keys(Keys.RETURN)
        self.browser.implicitly_wait(10)

    # Positive -> Add code to compare the button color from blue to green
    def ajaxData(self):
        findField = self.browser.find_element(By.ID, 'ajaxButton')
        findField.click()
        self.browser.implicitly_wait(17)
        if self.browser.find_element(By.CLASS_NAME, 'bg-success'):
            return True
        else:
            return False

    # Negative

    @pytest.mark.xfail
    def x_ajaxData(self):
        pass
