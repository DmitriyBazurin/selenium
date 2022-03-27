
from selenium import webdriver
import time
import unittest


link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

class TestPage(unittest.TestCase):
    def test_page1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('[placeholder="Input your name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        input2.send_keys("Petrov")
        time.sleep(1)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be absolute value of a number")
        
    def test_page2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('[placeholder="Input your name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        input2.send_keys("Petrov")
        time.sleep(1)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be absolute value of a number")
        
if __name__ == "__main__":
        unittest.main()



