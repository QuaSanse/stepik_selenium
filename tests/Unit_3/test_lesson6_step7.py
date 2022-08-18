"""
    Плагины и перезапуск тестов
"""
# pip install pytest-rerunfailures
# pytest -v --tb=line --reruns 1 --browser_name=chrome tests\Unit_3\test_lesson6_step7.py
# pytest -v --tb=line --reruns 1 tests\Unit_3\test_lesson6_step7.py

from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_pass(setup):
    setup.get(link)
    setup.find_element(By.CSS_SELECTOR, "#login_link")


def test_guest_should_see_login_link_fail(setup):
    setup.get(link)
    setup.find_element(By.CSS_SELECTOR, "#magic_link")
