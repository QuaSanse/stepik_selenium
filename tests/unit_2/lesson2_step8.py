import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))

try:
    """
        Задание: загрузка файла
    """
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    input_first_name = browser.find_element(
        By.CSS_SELECTOR, "input[name='firstname']")
    input_first_name.send_keys("Name")
    time.sleep(0.5)

    input_last_name = browser.find_element(
        By.CSS_SELECTOR, "input[name='lastname']")
    input_last_name.send_keys("Last name")
    time.sleep(0.5)

    input_email = browser.find_element(
        By.CSS_SELECTOR, "input[name='email']")
    input_email.send_keys("test@yandex.ru")
    time.sleep(0.5)

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    button_file = browser.find_element(
        By.CSS_SELECTOR, "input#file[type='file']")

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt')
    button_file.send_keys(file_path)

    # Нажать кнопку "Submit"
    button_submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
