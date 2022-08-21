import pwd
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestCase4:

    URL = 'http://www.uitestingplayground.com/'

    # SEARCH_INPUT = (By.PARTIAL_LINK_TEXT, 'Text Input')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self):
        search_input = self.browser.find_element(By.LINK_TEXT, "Sample App")
        search_input.send_keys(Keys.RETURN)
        self.browser.implicitly_wait(10)

    # Positive -> Add code to compare the button color from blue to green
    def sampleApp(self):

        try:
            login_status = self.browser.find_element(By.ID, 'loginstatus').get_attribute('class')
            loginBtn = self.browser.find_element(By.ID, 'login').text
            if login_status == 'text-info' and loginBtn == "Log In":
                pass
            else:
                return False
        except:
            return False

        try:
            user_field = self.browser.find_element(By.NAME, 'UserName')
            user_field.send_keys('Test1234')
            pwd_field = self.browser.find_element(By.NAME, 'Password')
            pwd_field.send_keys('pwd')
            self.browser.find_element(By.ID, 'login').click()

        except:
            return False
        
        try:
            login_status = self.browser.find_element(By.ID, 'loginstatus').get_attribute('class')
            loginBtn = self.browser.find_element(By.ID, 'login').text
            if login_status == 'text-success' and loginBtn == "Log Out":
                return True
            else:
                return False
        except:
            return False


    # Negative
    @pytest.mark.xfail
    def x_sampleApp(self):
        self.browser.refresh()
        findField = self.browser.find_element(By.CLASS_NAME, 'form-control')
        findField.send_keys()
        self.browser.implicitly_wait(10)
        findBtn = self.browser.find_element(By.ID, "updatingButton")
        findBtn.send_keys(Keys.RETURN)
        return findBtn.text
