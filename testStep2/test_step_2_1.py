from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    link = "http://suninjuly.github.io/get_attribute.html"

    selector_value = "[id = 'treasure']"
    browser = webdriver.Chrome(
        executable_path='../resources/chromedriver'
    )
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.CSS_SELECTOR, selector_value)

    x = x_element.get_attribute("valuex")

    print(x)



    y = calc(x)

    print("y = " + y)


    inputField = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    inputField.send_keys(y)
    input2 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    input2.click()
    input3 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    input3.click()
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(10)




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

