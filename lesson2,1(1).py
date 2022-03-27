from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element_by_id("treasure")
    x = chest.get_attribute('valuex')
    y = calc(x)

    chest_open = browser.find_element_by_tag_name('input')
    chest_open.send_keys(y)
    
    
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radiobtn = browser.find_element_by_id('robotsRule')
    radiobtn.click()

    sbm = browser.find_element_by_tag_name('button')
    sbm.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла