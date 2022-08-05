import math
from support_test.conftest import driver
from selenium.webdriver.common.by import By


class Captcha:

    # Посчитать математическую функцию от x
    def calc():
        x_element = driver.find_element(
            By.CSS_SELECTOR, "span.nowrap#input_value")
        resoult = str(math.log(abs(12*math.sin(int(x_element.text)))))
        return resoult


# x_element = driver.find_element(
#     By.CSS_SELECTOR, "span.nowrap#input_value")
# x = x_element.text
# y = calc(x)
