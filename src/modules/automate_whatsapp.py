import logging
import sys

import chromedriver_autoinstaller
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .random_sleep import random_sleep

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def find_contact(chrome_driver, phone_number: str) -> None:
    def click_newchat_button(
        chrome_driver,
        chat_button_xpath='//div[@class="_26lC3"][@title="Nouvelle discussion"]',
    ) -> None:

        chat_button = WebDriverWait(chrome_driver, 300).until(
            EC.presence_of_element_located((By.XPATH, chat_button_xpath))
        )

        chat_button.click()

    def paste_phone_number(
        chrome_driver,
        phone_number: str,
        chat_search_xpath: str = """//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/div/div[2]/div/div[2]""",
    ) -> None:

        pyperclip.copy(phone_number)
        chat_search = WebDriverWait(chrome_driver, 50).until(
            EC.presence_of_element_located((By.XPATH, chat_search_xpath))
        )
        random_sleep()
        chat_search.click()
        chat_search.send_keys(Keys.CONTROL + "v")
        random_sleep()
        chat_search.send_keys(Keys.ENTER)
        chat_search.clear()

    click_newchat_button(
        chrome_driver,
    )
    random_sleep()
    paste_phone_number(chrome_driver, phone_number)


def click_for_attachment(
    chrome_driver, attachment_xpath: str = '//div[@title = "Joindre"]'
) -> None:

    logger.debug("Click for attachment.")
    attachment_box = WebDriverWait(chrome_driver, 5).until(
        EC.presence_of_element_located((By.XPATH, attachment_xpath))
    )
    attachment_box.click()


def add_image_attachment(
    chrome_driver,
    attachment_path: str,
    image_xpath: str = '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]',
) -> None:
    logger.debug("Add image.")
    image_box = WebDriverWait(chrome_driver, 50).until(
        EC.presence_of_element_located((By.XPATH, image_xpath))
    )
    image_box.send_keys(attachment_path)


def paste_caption_to_image(
    chrome_driver,
    message: str,
    caption_xpath: str = """//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]""",
) -> None:

    logger.debug("Paste caption.")
    caption_box = WebDriverWait(chrome_driver, 50).until(
        EC.presence_of_element_located((By.XPATH, caption_xpath))
    )
    pyperclip.copy(message)
    caption_box.send_keys(Keys.CONTROL + "v")
    caption_box.send_keys(Keys.ENTER)


def install_driver() -> None:
    chromedriver_autoinstaller.install()


class WhatsAppSender:
    def __init__(self, chrome_cookies: str) -> None:

        install_driver()

        self.chrome_cookies = chrome_cookies
        self.chrome_driver = self._get_chrome_driver
        self.url: str = "https://web.whatsapp.com/"
        self._go_to_whatsapp()

    @property
    def _get_chrome_driver(self):
        logger.debug("Get chrome driver.")

        options = webdriver.ChromeOptions()
        options.add_argument(self.chrome_cookies)

        return webdriver.Chrome(options=options)

    def _go_to_whatsapp(self) -> None:
        logger.debug("Go to whatsapp.")
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(self.url)

    def send_message_whith_attachment(
        self, name: str, phone_number: str, image_path: str, message: str
    ) -> None:
        find_contact(self.chrome_driver, name, phone_number)
        random_sleep()
        click_for_attachment(self.chrome_driver)
        random_sleep()
        add_image_attachment(self.chrome_driver, image_path)
        random_sleep()
        paste_caption_to_image(self.chrome_driver, message)
        random_sleep()
