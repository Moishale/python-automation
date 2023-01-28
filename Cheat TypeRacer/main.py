import urllib.request
import pytesseract
import cv2

from time import sleep
from PIL import Image

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

URL = "https://play.typeracer.com/"
SOURCE = ""


class CheatTypeRacer:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.opener = urllib.request.build_opener()
        self.opener.addheaders = [(

            "User-Agent",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        )
        ]

    @staticmethod
    def configure(opener):
        pytesseract.pytesseract.tesseract_cmd = SOURCE
        urllib.request.install_opener(opener)

    def __enter__(self):
        CheatTypeRacer.configure(self.opener)

        self.driver.get(URL)
        return self

    def __exit__(self, type, value, traceback):
        print("Waiting 20 seconds before closing ...")
        sleep(20)
        self.driver.close()

    def start_menu(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "bkgnd-green"))
        ).click()

    def start_race(self):
        text = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div',
                )
            )
        )
        sleep(0.05)
        print(f"The text is: ", text.text)

        input_button = self.driver.find_element(By.CLASS_NAME, "txtInput")

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(input_button))

        for word in str(text.text):
            input_button.click()
            input_button.send_keys(word)

    def start_captcha(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "gwt-Button"))
        ).click()

        img = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "challengeImg"))
        )
        src = img.get_attribute("src")

        urllib.request.urlretrieve(src, "Cheat TypeRacer/captcha.png")

        captcha_text = pytesseract.image_to_string(
            cv2.imread("Cheat TypeRacer/captcha.png"))

        print(captcha_text)

        for word in captcha_text:
            self.driver.find_element(
                By.CLASS_NAME, "challengeTextArea").send_keys(word)

        sleep(2)

        self.driver.find_element(By.CLASS_NAME, "gwt-Button").click()


class CheatTypeProxy:
    def __init__(self, driver):
        self.driver = driver
        self.racer = CheatTypeRacer(self.driver)

    def run(self):
        with self.racer as c:
            c.start_menu()
            c.start_race()
            c.start_captcha()


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(
    service_log_path="NUL",
    service=Service(ChromeDriverManager().install()),
    options=options,
)


proxy = CheatTypeProxy(driver)
proxy.run()

