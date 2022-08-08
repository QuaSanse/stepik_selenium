import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    # browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    # Чтобы определить момент, когда цена аренды уменьшится до $100,
    # используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажать на кнопку "Book"
    button_book = browser.find_element(By.ID, "book")
    button_book.click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
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

    # Нажать на кнопку Submit
    button_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_submit.click()
    time.sleep(0.5)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
