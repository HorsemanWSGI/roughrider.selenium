import pytest
from selenium import webdriver


class WSGISelenium:

    def pytest_addoption(self, parser):
        parser.addoption(
            "--browser-headless",
            action="store_true",
            help="Specify if the browser should be HEADLESS.",
        )
        parser.addoption(
            "--browser",
            default="firefox",
            choices=["firefox", "chrome"],
            help="Specify the browser used to run the tests.",
        )
        parser.addoption(
            "--browser-width",
            type=int,
            default=1200,
            help="Specify the browser window width.",
        )
        parser.addoption(
            "--browser-height",
            type=int,
            default=600,
            help="Specify the browser window height.",
        )

    @pytest.fixture(scope="class")
    def browser_driver(self, request):
        browser = request.config.getoption("--browser")
        if browser == 'firefox':
            options = webdriver.FirefoxOptions()
            args = {'firefox_options': options}
            factory = webdriver.Firefox
        else:
            options = webdriver.ChromeOptions()
            args = {'chrome_options': options}
            factory = webdriver.Chrome

        if request.config.getoption("--browser-headless"):
            options.set_headless()

        driver = factory(**args)
        driver.set_window_size(
            request.config.getoption("--browser-width"),
            request.config.getoption("--browser-height")
        )
        request.cls.driver = driver
        yield
        driver.close()


wsgi_selenium = WSGISelenium()
