# Simple assignment
import time
from selenium.webdriver import Chrome
driver = Chrome('venv/Drivers/chromedriver.exe')
with Chrome('venv/Drivers/chromedriver.exe') as driver:
    driver.get("https://www.udemy.com")
    driver.maximize_window()
    # //test
    # username = driver.find_element_by_id('email--1')
    # username.send_keys('tigran.gagiyan@mail.ru')
    # password = driver.find_element_by_id('id_password')
    # password.send_keys('tigranarmen')
    # submit = driver.find_element_by_id('submit-id-submit')
    # submit.click()
    time.sleep(2)
    box1 = driver.find_element_by_id('header-search-field')
    box1.send_keys('python selenium')
    box1.click()
    time.sleep(7)
    searbutton=driver.find_element_by_class_name('input-group-btn')
    searbutton.click()
    time.sleep(5)
    # box1.send_keys('selenium python')
    driver.quit()
