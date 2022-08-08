from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # For Windows
    link = "http:\\suninjuly.github.io\\registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_first_name = browser.find_element(
        By.CSS_SELECTOR, "div.first_block .form-control.first")
    input_first_name.send_keys("Name")

    input_last_name = browser.find_element(
        By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input")
    input_last_name.send_keys("Last name")

    input_email = browser.find_element(
        By.CSS_SELECTOR, "div.form-group.third_class > input")
    input_email.send_keys("email")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
