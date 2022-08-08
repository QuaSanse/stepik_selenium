"""
    Задание: параметризация тестов
    
    pytest -v Unit_3\test_lesson6_step3.py

    открыть страницу 
    ввести правильный ответ 
    нажать кнопку "Отправить" 
    дождаться фидбека о том, что ответ правильный 
    проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

    Структура

1. Фикстура browser. как в предыдущих примерах.
2. Класс который начинается на Test. Как в предыдущих примерах.
3. Внутри класса 2 переменные: 1. пустая для сообщения = "".  2. массив со списком адресов 
4.Внутри класса также есть функция с parametrize('название переменной для исползования внутри этой функции= неважно какое но желательно подходящее по смыслу я назову links', "название переменой масива со списком адресов") похожее на предыдущий урок
5. Эта функция тест поэтому название функции должно начинаться на test_
6. Эта функция получает self, browser, и название переменной для исползования внутри этой функции( с 4 пункта ' ' я назову links например)

Внутри функции:
7.  Первые 2 строчки как в предыдущем примере 2 предпоследние с небольшим изменением в link
8. browser.implicity_wait(10)
9. Ищем textarea
10. Записываем в неё через  send_key(str(math.log(int(time.time())))  с примера
11. Через WebDriverWait EC.element_to_be_clickable находим класс кнопку
12. нажимаем на кнопку
13. Через WebDriverWait EC.visibility_of_element_located().text находим класс сообщения и текст его присваиваем переменной
14. Проверяем не равен ли он !="Correct!"
15. если не равен то добавляем в переменную с 4 пункта посредством self. название переменной += с пункта 13 пунк переменная и print()
16. assert с пункта13  переменная == False проверяем
17.  
if __name__ == "__main__":

    unittest.main()
    
"""

# from os import link
import pytest
import time
import math
from selenium.webdriver.common.by import By


class TestPageFeedback():

    # для сообщения
    feedback_text = ""
    # массив со списком адресов
    links = [
        "https://stepik.org/lesson/236895/step/1",
        # "https://stepik.org/lesson/236896/step/1",
        # "https://stepik.org/lesson/236897/step/1",
        # "https://stepik.org/lesson/236898/step/1",
        # "https://stepik.org/lesson/236899/step/1",
        # "https://stepik.org/lesson/236903/step/1",
        # "https://stepik.org/lesson/236904/step/1",
        # "https://stepik.org/lesson/236905/step/1"
    ]

    @pytest.mark.parametrize('link', links)
    def test_feedback(self, setup, link):
        driver = setup
        driver.get(link)
        driver.implicity_wait(10)
        input_textarea = driver.find_element(By.ID, 'ember87')
        answer = math.log(int(time.time() + .5))
        input_textarea.send_keys(answer)
        button_send = driver.find_element(
            By.CSS_SELECTOR, 'button.submit-submission')
        button_send.click()
        time.sleep(60)
