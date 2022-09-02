from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math


try:
    link = "http://suninjuly.github.io/selects1.html"


    browser = webdriver.Chrome(
        executable_path='../resources/chromedriver'
    )
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "[id = 'num1']")
    y_element = browser.find_element(By.CSS_SELECTOR, "[id = 'num2']")
    x = x_element.text
    y = y_element.text

    result = int(x) + int(y)
    print(result)

    result_in_css = "[value='" + str(result) + "']"
    print(result_in_css)


    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.CSS_SELECTOR, result_in_css).click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    time.sleep(1)
    button.click()
    button.click()

    time.sleep(10)


    #select = Select(browser.find_element(By.TAG_NAME, "select"))
    #select.select_by_value(result) # ищем элемент с текстом "Python"



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()