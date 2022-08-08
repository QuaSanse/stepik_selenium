"""
    XFail: помечать тест как ожидаемо падающий
    запуск: pytest -v  Unit_3\test_lesson5_step5.py 
    запуск с @pytest.mark.xfail(reason="fixing this bug right now")
        pytest -rx -v Unit_3\test_lesson5_step5.py 
    запуск с по XPASS-тестам добавили символ X в параметр -r  
        pytest -rX -v Unit_3\test_lesson5_step5.py 
    
    https://pytest.org/en/stable/how-to/skipping.html
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        # browser.find_element(By.CSS_SELECTOR, "button.favorite")
        browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")
