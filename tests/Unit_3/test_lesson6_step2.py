"""
    Параметризация тестов
    @pytest.mark.parametrize()

"""
#     pytest -s -v tests\Unit_3\test_lesson6_step2.py


# @pytest.mark.usefixtures('setup')


import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(setup, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    driver = setup
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, "#login_link")
