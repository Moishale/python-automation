from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class Bands:
    def __init__(self, driver):
        self.urls = Bands.text_to_list('urls.txt')
        self.counter = len(self.urls)
        self.driver = driver
        self.driver.maximize_window()

    @staticmethod
    def text_to_list(filename):
        with open(filename) as file:
            return [line.rstrip() for line in file]

    def do_homework(self):
        while self.urls:
            self.driver.get(self.urls.pop())

            finish_button = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(
                    (
                        By.CLASS_NAME,
                        'finishbutton',
                    )
                )
            )
            self.driver.execute_script('heTerminado()', finish_button)

            check_button = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="floatLayer"]/table/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/span',
                    )
                )
            )
            self.driver.execute_script(
                'comprobarRespuestas(1),cerrarVentana()', check_button)

            grade = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="capanotas"]',
                    )
                )
            )
            self.driver.execute_script(
                'document.querySelector("#capanotas").innerHTML = "10/10"', grade)
            sleep(3)

            height = self.driver.execute_script(
                'return document.body.scrollHeight')

            self.driver.set_window_size(1920, height)
            self.driver.save_screenshot(f'set{self.counter}.png')
            self.counter -= 1

            print(f'Saving set{self.counter+1}.png .....')


class BandsProxy:
    def __init__(self, driver):
        self.bands = Bands(driver)

    def __enter__(self):
        return self.bands

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.bands.driver.quit()


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--headless")


driver = webdriver.Chrome(
    service_log_path="NUL",
    service=Service(ChromeDriverManager().install()),
    options=options,
)

with BandsProxy(driver) as bands:
    bands.do_homework()
