# Simple assignment
from selenium.webdriver import Chrome
driver = Chrome('venv/Drivers/chromedriver.exe')
with Chrome('venv/Drivers/chromedriver.exe') as driver:
    driver.get("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
    username = driver.find_element_by_id('email--1')
    username.send_keys('tigran.gagiyan@mail.ru')
    password = driver.find_element_by_id('id_password')
    password.send_keys('tigranarmen')
    submit = driver.find_element_by_id('submit-id-submit')
    submit.click()
    driver.quit()
