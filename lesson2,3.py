from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element_by_class_name('btn')
    btn.click()

    time.sleep(1)

    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(1)

    num = browser.find_element_by_id('input_value').text
    y = int(num)
    answer = calc(y)

    time.sleep(1)
    
    result = browser.find_element_by_id('answer')
    result.send_keys(answer)

    btn2 = browser.find_element_by_class_name('btn')
    btn2.click()


finally:
    time.sleep(10)
    browser.quit()