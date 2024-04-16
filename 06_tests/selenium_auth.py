# from pathlib import Path
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from fake_headers import Headers

# path = Path(__file__).parent.parent.resolve()


def wait_element(browser, delay_second=1, by=By.CLASS_NAME, value=None):

    return WebDriverWait(browser, delay_second).until(
        expected_conditions.presence_of_element_located((by, value))
    )


def read_config(config_file):
    with open(config_file) as file:
        return dict(eval(file.read()))


def ya_auth(user_login, user_password, browser_path):
    chrome_path = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM, driver_version='125').install()
    options = ChromeOptions()
    options.binary_location = browser_path
    # options.add_experimental_option("detach", True)
    browser_service = Service(executable_path=chrome_path)
    browser = Chrome(service=browser_service, options=options)

    browser.get("https://passport.yandex.ru/auth/")
    login = wait_element(browser, by=By.ID, value="passp-field-login")
    login_button = wait_element(browser, by=By.ID, value="passp:sign-in")
    login.send_keys(user_login)
    login_button.click()
    # sleep(1)
    password = wait_element(browser, by=By.ID, value="passp-field-passwd")
    password.send_keys(user_password)
    login_button = wait_element(browser, by=By.ID, value="passp:sign-in")
    # sleep(1)
    login_button.click()
    sleep(5)
    current_url = browser.current_url
    return current_url


if __name__ == '__main__':
    config = read_config("config.json")
    # print(ChromeDriverManager(driver_version='120').install())
    # chrome_path = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM, driver_version='125').install()
    # print(chrome_path)
    # options = ChromeOptions()
    # options.binary_location = config['browser_path']
    # options.add_experimental_option("detach", True)
    # headers = Headers(browser="chrome", os="win").generate()
    # print(headers)
    # options.add_argument(f"user-agent={headers['User-Agent']}")
    # browser_service = Service(executable_path=chrome_path)
    # browser = Chrome(service=browser_service, options=options)
    # print(browser)
    site = ya_auth(config['login'], config['password'], config['browser_path'])
    print(site)
    # sleep(5)

