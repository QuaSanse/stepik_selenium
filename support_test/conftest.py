from selenium import webdriver

varib = "Hello"


def get_webdriver() -> webdriver:
    print("\nstart browser for test...")
    driver = webdriver.Chrome(
        executable_path='C:\\projects\\stepik_selenium\\chromedriver\\chromedriver.exe'
    )
    yield driver

    driver.close()
    print("\nquit browser...")
    driver.quit()
