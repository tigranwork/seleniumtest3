# Simple assignment
from selenium.webdriver import Chrome
driver = Chrome()
with Chrome() as driver:
    driver.get("http://the-internet.herokuapp.com/login")
    username = driver.find_element_by_id('username')
    username.send_keys('tomsmith')
    password = driver.find_element_by_id('password')
    password.send_keys('SuperSecretPassword!')
    submit = driver.find_element_by_xpath('//*[@id="login"]/button')
    submit.click()
    driver.quit()
    