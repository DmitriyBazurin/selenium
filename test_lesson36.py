import time
import math
from tkinter import NUMERIC
from selenium import webdriver
import pytest
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('num', ["895", "896", "897", "898", "899", "903", "904", "905"])
class TestQuest:
    def test_quest(self, browser, num):
        link = f"https://stepik.org/lesson/236{num}/step/1"
        browser.get(link)
    
        inp = browser.find_element_by_tag_name('textarea')
        inp.send_keys(str(math.log(int(time.time()))))
        btn = browser.find_element_by_class_name("submit-submission")
        btn.click()
        msg = browser.find_element_by_class_name('smart-hints__hint').text
        assert msg == "Correct!", 'Тест успешен'
