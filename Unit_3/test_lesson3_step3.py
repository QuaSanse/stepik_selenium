import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


def get_link(url) -> str:
    """
        Запускает драйвер и проходит по полям
    """
    driver = webdriver.Chrome()
    driver.get(url)

    # Ваш код, который заполняет обязательные поля
    input_first_name = driver.find_element(
        By.CSS_SELECTOR, "div.first_block .form-control.first")
    input_first_name.send_keys("Name")

    input_last_name = driver.find_element(
        By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input")
    input_last_name.send_keys("Last name")

    input_email = driver.find_element(
        By.CSS_SELECTOR, "div.form-group.third_class > input")
    input_email.send_keys("email")

    # Отправляем заполненную форму
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    return welcome_text

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(3)
    # закрываем браузер после всех манипуляций
    # driver.quit()


class TestUnit_step13(unittest.TestCase):
    def test_web1(self):
        """
            Первый тест
        """
        link = "http:\\suninjuly.github.io\\registration1.html"
        self.assertEqual(get_link(link),
                         "Congratulations! You have successfully registered!",
                         "registration is failed")

    def test_web2(self):
        """
            Второй тест
        """
        link = "http:\\suninjuly.github.io\\registration2.html"
        self.assertEqual(get_link(link),
                         "Congratulations! You have successfully registered!",
                         "registration is failed")


if __name__ == "__main__":
    unittest.main()
