# Установка Firefox и Selenium-драйвера geckodriver
# pytest -s -v --browser_name=firefox tests\Unit_3\test_lesson6_step5.py


from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox(
    executable_path='C:\\projects\\stepik_selenium\\geckodriver\\geckodriver.exe'
)
driver.get("https://stepik.org/lesson/25969/step/8")
