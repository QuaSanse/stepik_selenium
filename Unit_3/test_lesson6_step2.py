"""
    Параметризация тестов

    @pytest.mark.parametrize()
    

    pytest -s -v Unit_3\test_lesson6_step2.py
    
"""
# from support_test.conftest import get_webdriver
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
from pprint import pprint
import sys
import support_test.conftest
# sys.path.append('..')
# import sys.path[5].support_test.conftest

# pprint(sys.path[5])

pprint(dir(support_test.conftest))

# sys.path.append('..')

# C:\projects\stepik_selenium\support_test\conftest.py
# support_test\conftest.py
# from ..support_test.conftest import get_webdriver


# print(dir(varib))


# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

# driver = get_webdriver()


# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# def test_guest_should_see_login_link(driver, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     driver.get(link)
#     driver.find_element(By.CSS_SELECTOR, "#login_link")
