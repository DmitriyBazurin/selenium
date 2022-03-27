from selenium import webdriver
import os
import os 



try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)

    in1 = browser.find_element_by_name('firstname')
    in1.send_keys('Dmitriy')
    in2 = browser.find_element_by_name('lastname')
    in2.send_keys('Bazurin')
    in3 = browser.find_element_by_name('email')
    in3.send_keys('ba_91@mail.ru')
    
    element = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)

    btn = browser.find_element_by_tag_name('button')
    btn.click()




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()





