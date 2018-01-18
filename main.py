# coding=utf8
# the above comment is so that the hebrew string will work. do NOT erase it unless you erase the hebrew message.

from time_config import get_time
from time_config import wait_until

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

# Replace 'target' with the name of your contact, group or broadcast group
target = "self group"

# A text that'll be sent at the end of every message
bot_message = u"_זוהי הודעה אוטומתית שקיבלת מכיוון שאתה ברשימת תפוצה. אם ברצונך לצאת, נא הקש 1_"

# A number that represents the time difference between your computer and phone (in seconds)
COMPUTER_PHONE_DELAY = 16

# The time in seconds that the program won't throw a timeout exception when it loads the page
TIMEOUT_SECONDS = 600

# The default message the send_message function sends. You may ignore this.
DEFAULT_MESSAGE = "selenium test, please ignore"

# Download the driver from https://sites.google.com/a/chromium.org/chromedriver/downloads
CHROME_DRIVER_PATH = r'C:\Users\omerl\Desktop\school\tests\chromedriver.exe'

# Replace with your chrome profile path. Make sure NOT to include to /Default directory.
CHROME_PROFILE_PATH = r"user-data-dir=C:\Users\omerl\PycharmProjects\automatic-2212\profile"

# Replace with your message.
MY_MESSAGE = "22:12"


def get_chrome_options(chrome_profile_path, chrome_display=None):
    """
    Builds a ChromeDriver object so that a user profile'll be loaded.
    :param chrome_profile_path: a string containing the path to the chrome profile (excluding the default directory).
    :param chrome_display: if you want to maximize or minimize the page. Personally, I recommend it stays empty.
        example string: "--start-maximized".
    :return: the ChromeOptions object built.
    """
    options = webdriver.ChromeOptions()
    options.add_argument(chrome_profile_path)
    if chrome_display is not None:
        options.add_argument(chrome_display)
    return options


def open_whatsapp(chrome_driver_path=CHROME_DRIVER_PATH, options=None):
    """
    Opens Whatsapp web using the Selenium Chrome web driver.
    :param chrome_driver_path: the path to the driver on your computer.
    :param options: a ChromeOptions object if you want to change the options/load a chrome profile.
    :return: the web driver used to open whatsapp.
    """
    driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)
    driver.get("https://web.whatsapp.com/")
    return driver


def open_group(driver, contact=None):
    """
    Opens a Whatsapp contact/group/broadcast list. 
    :param driver: a webdriver object (from selenium).
    :param contact: The contact/group/broadcast list.
    :return: a WebDriverWait that was used to open the contact/group/broadcast list.
    """
    if contact is None:
        contact = target
    wait = WebDriverWait(driver, TIMEOUT_SECONDS)
    y_arg = '//*[@id="side"]/div[2]/div/label/input'
    input_y = wait.until(EC.presence_of_element_located((
        By.XPATH, y_arg)))
    input_y.send_keys(contact + Keys.ENTER)
    return wait


def send_message(wait, message=DEFAULT_MESSAGE):
    """
    Sends a message in an open Whatsapp contact/group/broadcast list.
    :param wait: A WebDriverWait object(from selenium). 
    :param message: The message to send.
    """
    inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
    inp_xpath = "//div[@contenteditable='true']"
    input_box = wait.until(EC.presence_of_element_located((
        By.XPATH, inp_xpath)))
    input_box.send_keys(message + Keys.SHIFT + Keys.ENTER)
    input_box.send_keys(bot_message + Keys.ENTER)


def prompt_user_for_time():
    """
    Prompts a time from the user and returns a list containing the different parts of the time.
    Splits the time according to the ':' delimiter.
    :returns: the list containing the different parts of the time (hours, minutes seconds, etc.)
    """
    return get_time(raw_input("please enter a time to wake the program up again: "))


def main(target_time=None, message=MY_MESSAGE, contact=None):
    """
    Opens Whatsapp, sends to the target your message at target time. The main function.
    :param target_time: The time to send the message(as a list or string).
    :param message: A string to send to the target.
    :param contact: The contact to send the message.
    """
    options = get_chrome_options(CHROME_PROFILE_PATH)
    driver = open_whatsapp(options=options)
    if target_time is None:
        target_time = prompt_user_for_time()
    wait_until(target_time)
    from time import sleep
    sleep(COMPUTER_PHONE_DELAY)  # difference in time between phone and computer
    wait = open_group(driver, contact)
    send_message(wait, message)
    raw_input("press any button to continue...")  # to let the message get sent before the program closes.

if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        main(argv[0])
    elif len(argv) == 3:
        main(argv[0], argv[1])
    elif len(argv) >= 4:
        main(argv[0], argv[1], argv[2])
    else:
        main()
