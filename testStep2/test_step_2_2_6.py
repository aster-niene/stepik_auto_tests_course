from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"

    browser = webdriver.Chrome(
        executable_path='../resources/chromedriver'
    )
    browser.get(link)


    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")

    x = x_element.text
    print("x = " + x)

    y = calc(x)

    print("y = " + y)

    inputField = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    inputField.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    input2 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    input2.click()
    input3 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    input3.click()
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

