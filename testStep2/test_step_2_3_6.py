from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math
import os


try:

    link = "http://suninjuly.github.io/redirect_accept.html"

    browser = webdriver.Chrome(
        executable_path='../resources/chromedriver'
    )
    browser.implicitly_wait(5) # метод неявного ожидания. Ожидаем 5 секунд, с запросом каждые 0.5 секунды (по дефолту)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser.get(link)

    trollface_button = browser.find_element(By.CSS_SELECTOR, "button.trollface ")
    trollface_button.click()

    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)

    inputField = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    inputField.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



finally:
    time.sleep(10)
    browser.quit()