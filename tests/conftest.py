import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options() -> chrome_options:
    options = chrome_options()
    # --headless Запуск в автономном режиме, т. е. без зависимостей пользовательского интерфейса или сервера отображения.
    # options.add_argument('headless')
    options.add_argument('crome')
    # Запуск в автономном режиме, т. е. без зависимостей пользовательского интерфейса или сервера отображения.
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1200,800')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options) -> webdriver:
    options = get_chrome_options
    print("\nstart browser for test...")
    driver = webdriver.Chrome(
        executable_path='C:\\projects\\stepik_selenium\\chromedriver\\chromedriver.exe',
        options=options
    )
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    if request.cls is not None:
        request.cls.driver = driver
    yield driver

    driver.close()
    print("\nquit browser...")
    driver.quit()
