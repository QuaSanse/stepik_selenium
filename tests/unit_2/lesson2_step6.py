import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    """
        Задание на execute_script
    """
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(0.5)

    # Посчитать математическую функцию от x
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(
        By.CSS_SELECTOR, "span.nowrap#input_value")
    x = x_element.text
    y = calc(x)

    # Ввести ответ в текстовое поле
    input_search = browser.find_element(By.ID, "answer")
    input_search.clear()
    input_search.send_keys(y)
    time.sleep(0.5)

    # Проскроллить страницу вниз
    button_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", button_submit)

    # Отметить checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    time.sleep(0.5)

    # Выбрать radiobutton "Robots rule!"
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_radio.click()
    time.sleep(0.5)

    # Нажать на кнопку Submit

    button_submit.click()
    time.sleep(0.5)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
