import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))

try:
    """
        Задание: принимаем alert
    """
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    time.sleep(0.5)

    # Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(0.5)

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    # Посчитать математическую функцию от x
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    # Ввести ответ в текстовое поле
    input_search = browser.find_element(By.ID, "answer")
    input_search.clear()
    input_search.send_keys(y)
    time.sleep(0.5)

    # Нажать кнопку
    button_submit = browser.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    button_submit.click()

    # ждем загрузки страницы
    time.sleep(5)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
