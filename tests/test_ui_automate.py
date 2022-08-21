from re import search
from turtle import textinput
import pytest

from src.testcase_1_text_input import TestCase1
from src.testcase_2_click import TestCase2
from src.testcase_3_ajaxData import TestCase3
from src.testcase_4_sampleApp import TestCase4

TestCase1.__test__ = False
TestCase2.__test__ = False
TestCase3.__test__ = False
TestCase4.__test__ = False


def test_case1(browser):
    # Set up test case data
    PHRASE = 'Text1234'

    # Search for the phrase
    search_page = TestCase1(browser)
    search_page.load()
    search_page.search()
    ret_text = search_page.text_input(PHRASE)

    assert ret_text == PHRASE


def test_case2(browser):
    search_page = TestCase2(browser)
    search_page.load()
    search_page.search()
    # -> Add code to compare the button color from blue to green
    ret_text = search_page.click()

    assert ret_text == "btn btn-success"


def test_case3(browser):
    search_page = TestCase3(browser)
    search_page.load()
    search_page.search()
    ret_text = search_page.ajaxData()

    assert ret_text == True


def test_case4(browser):
    search_page = TestCase4(browser)
    search_page.load()
    search_page.search()
    ret_text = search_page.sampleApp()

    assert ret_text == True
