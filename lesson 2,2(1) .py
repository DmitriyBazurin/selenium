from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    num = browser.find_element_by_id('input_value').text
    y = int(num)
    answer = calc(y)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
    result = browser.find_element_by_id('answer')
    result.send_keys(answer)

    check = browser.find_element_by_id('robotCheckbox')
    check.click()

    rad = browser.find_element_by_id('robotsRule')
    rad.click()

    button.click()
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()