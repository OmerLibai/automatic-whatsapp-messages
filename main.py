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

# a text that'll be sent at the end of every message
bot_message = u"_זוהי הודעה אוטומתית שקיבלת מכיוון שאתה ברשימת תפוצה. אם ברצונך לצאת, נא הקש 1_"


def open_whatsapp(chrome_driver_path=r'C:\Users\omerl\Desktop\school\tests\chromedriver.exe'):
    """
    Opens Whatsapp web using the Selenium Chrome web driver.
    :param chrome_driver_path: the path to the driver on your computer.
    :return: the web driver used to open whatsapp.
    """
    driver = webdriver.Chrome(chrome_driver_path)
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
    wait = WebDriverWait(driver, 600)
    y_arg = '//*[@id="side"]/div[2]/div/label/input'
    input_y = wait.until(EC.presence_of_element_located((
        By.XPATH, y_arg)))
    input_y.send_keys(contact + Keys.ENTER)
    return wait


def send_message(wait, message="selenium test, please ignore"):
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


def main(target_time=None, message='22:12', contact=None):
    """
    Opens Whatsapp, sends to the target your message at target time. The main function.
    :param target_time: The time to send the message(as a list or string).
    :param message: A string to send to the target.
    :param contact: The contact to send the message.
    """
    driver = open_whatsapp()
    if target_time is None:
        target_time = prompt_user_for_time()
    wait_until(target_time)
    wait = open_group(driver, contact)
    send_message(wait, message)


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