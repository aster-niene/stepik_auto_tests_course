from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math
import os


try:

    link = "http://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome(
        executable_path='../resources/chromedriver'
    )
    browser.get(link)

    firstName = browser.find_element(By.CSS_SELECTOR, "[name = 'firstname']")
    firstName.send_keys("Ivan")

    lastName = browser.find_element(By.CSS_SELECTOR, "[name = 'lastname']")
    lastName.send_keys("Ulianov")

    email = browser.find_element(By.CSS_SELECTOR, "[name = 'email']")
    email.send_keys("mail@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '../file.txt')  # добавляем к этому пути имя файла


    fileSelect = browser.find_element(By.CSS_SELECTOR, "[name = 'file']") # находим элемент добавления файла
    fileSelect.send_keys(file_path) # загружаем в элемент добавления файла наш файл

    submit = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    submit.click()



finally:
    time.sleep(10)
    browser.quit()
