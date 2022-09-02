from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:

    link = "http://suninjuly.github.io/explicit_wait2.html"

    browser = webdriver.Chrome(
        executable_path='../resources/chromedriver'
    )
    browser.implicitly_wait(5) # метод неявного ожидания. Ожидаем 5 секунд, с запросом каждые 0.5 секунды (по дефолту)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[id='price']"), "$100"))
    # тормозим браузер, до тех пор пока не появится ожидаемое нами хначение
    book_button = browser.find_element(By.CSS_SELECTOR, "[id='book']")
    book_button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)

    inputField = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    inputField.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "[id='solve']")
    button.click()


finally:
    time.sleep(10)
    browser.quit()


