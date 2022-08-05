"""
    Задание: параметризация тестов
    
    pytest -v Unit_3\test_lesson6_step3.py

    открыть страницу 
    ввести правильный ответ 
    нажать кнопку "Отправить" 
    дождаться фидбека о том, что ответ правильный 
    проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
    
"""

import pytest
import time
import math
from ..support.conftest import get_webdriver


class TestPageFeedback():

    answer = math.log(int(time.time() + .5))

    driver = get_webdriver()

    # для сообщения
    feedback_text = ""
    # массив со списком адресов
    links = [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    ]

    @pytest.Mark
    def test_feedback():
        pass
