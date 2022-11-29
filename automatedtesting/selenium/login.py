# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import logging


# Start the browser and login with standard_user
def login(user, password):
    logging.basicConfig(filename='selenium.log', level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')
    logging.info('Starting the browser...')
    print('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome('./chromedriver')
    #driver = webdriver.Chrome(options=options)
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

    print('INFO: Successfully logged in as ' + user)
    logging.info('Successfully logged in as ' + user)

    items = driver.find_elements(
        "css selector", "button.btn_primary.btn_small.btn_inventory")

    for item in items:
        product = item.get_property("name")
        print('INFO: ' + product + ' added to the cart')
        logging.info(product + ' added to the cart')
        item.click()
    cart_label = driver.find_element(
        "css selector", '.shopping_cart_badge').text

    driver.find_element(
        "css selector", "a[class='shopping_cart_link']").click()
    print('INFO: Removing all 6 items to cart')
    logging.info('Removing all 6 items to cart')
    items = driver.find_elements("css selector", "button.cart_button")

    for item in items:
        product = item.get_property("name")
        print('INFO: ' + product + ' removed from the cart')
        logging.info(product + ' removed from the cart')
        item.click()


login('standard_user', 'secret_sauce')
