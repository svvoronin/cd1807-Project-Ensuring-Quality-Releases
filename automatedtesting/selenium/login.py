# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import logging
from add_remove_from_cart import add_remove_from_cart
logging.basicConfig(filename='selenium.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')

# Start the browser and login with standard_user


def login(user, password):

    logging.info('Starting the browser...')
    print('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    #driver = webdriver.Chrome('./chromedriver')
    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome()
    print('Browser started successfully. Navigating to the demo page to login.')
    logging.info(
        'Browser started successfully. Navigating to the demo page to login...')
    driver.get('https://www.saucedemo.com/')

    driver.find_element(
        "css selector", "input[id='user-name']").send_keys(user)
    driver.find_element(
        "css selector", "input[id='password']").send_keys(password)
    driver.find_element("css selector", "input[id='login-button']").click()
    add_remove_from_cart(driver)


login('standard_user', 'secret_sauce')
