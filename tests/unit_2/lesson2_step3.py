from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    """
        Задание: работа с выпадающим списком
    """
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(0.5)

    # Посчитать сумму заданных чисел
    def get_sum_by_id(elem1, elem2):
        num1 = browser.find_element(By.ID, elem1)
        num2 = browser.find_element(By.ID, elem2)
        return int(num1.text) + int(num2.text)

    # Выбрать в выпадающем списке значение равное расчитанной сумме
    select_drop = Select(browser.find_element(By.TAG_NAME, 'select'))
    select_drop.select_by_index(get_sum_by_id('num1', 'num2'))

    # Нажать кнопку "Submit"
    button_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_submit.click()
    time.sleep(0.5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
