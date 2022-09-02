from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math
import os


try:

    link = "http://suninjuly.github.io/alert_accept.html"

    browser = webdriver.Chrome(
        executable_path='../resources/chromedriver'
    )

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser.get(link)

    submitButton = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submitButton.click()

    confirm = browser.switch_to.alert
    confirm.accept()

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