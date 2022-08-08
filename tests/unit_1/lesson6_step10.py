from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http:\\suninjuly.github.io\\registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_first_name = browser.find_element(
        By.CSS_SELECTOR, "div.first_block div.first_class input")
    input_first_name.send_keys("Name")
    time.sleep(0.5)

    input_last_name = browser.find_element(
        By.CSS_SELECTOR, "div.first_block .form-control.second")
    input_last_name.send_keys("Last name")
    time.sleep(0.5)

    input_email = browser.find_element(
        By.CSS_SELECTOR, "div.first_block .form-control.third")
    input_email.send_keys("test@yandex.ru")
    time.sleep(0.5)

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
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
