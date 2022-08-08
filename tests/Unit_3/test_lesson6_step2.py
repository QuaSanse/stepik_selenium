"""
    Параметризация тестов

    @pytest.mark.parametrize()
    

    pytest -s -v tests\Unit_3\test_lesson6_step2.py
    
"""
import pytest
# from selenium import webdriver
from selenium.webdriver.common.by import By


# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     driver = get_webdriver()
#     yield driver
#     print("\nquit browser..")
#     browser.quit()

@pytest.mark.usefixtures('setup')
@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(setup, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    driver = setup
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, "#login_link")
