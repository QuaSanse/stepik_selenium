import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture
def get_chrome_options() -> chrome_options:
    options = chrome_options()
    # --headless Запуск в автономном режиме, т. е. без зависимостей пользовательского интерфейса или сервера отображения.
    # options.add_argument('headless')
    options.add_argument('crome')
    # Запуск в автономном режиме, т. е. без зависимостей пользовательского интерфейса или сервера отображения.
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1200,1080')
    return options


@pytest.fixture
def get_firefox_options() -> firefox_options:
    options = firefox_options()
    options.add_argument('firefox')
    # options.add_argument('--start-maximized')
    # options.add_argument('--window-size=1200,1080')
    return options


@pytest.fixture
def get_webdriver(request, get_chrome_options, get_firefox_options) -> webdriver:
    browser_name = request.config.getoption("browser_name")
    driver = None
    if browser_name == "chrome":
        options = get_chrome_options
        print("\nstart Chrome browser for test...")
        driver = webdriver.Chrome(
            executable_path='C:\\projects\\stepik_selenium\\chromedriver\\chromedriver.exe',
            options=options
        )
        return driver
    elif browser_name == "firefox":
        options = get_firefox_options
        print("\nstart Firefox browser for test...")
        driver = webdriver.Firefox(
            executable_path='C:\\projects\\stepik_selenium\\geckodriver\\geckodriver.exe'
        )
        return driver
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")


@pytest.fixture(scope='function')  # function session
def setup(request, get_webdriver):
    driver = get_webdriver
    if request.cls is not None:
        request.cls.driver = driver
    yield driver

    driver.close()
    print("\nquit browser...")
    driver.quit()
