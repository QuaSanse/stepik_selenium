from selenium import webdriver


def get_webdriver() -> webdriver:
    driver = webdriver.Chrome(
        executable_path='C:\\projects\\stepik_selenium\\chromedriver\\chromedriver.exe'
    )
    return driver
