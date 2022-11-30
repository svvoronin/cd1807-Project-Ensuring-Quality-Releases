# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:41:16 2022

@author: Voroserg
"""

import logging
logging.basicConfig(filename='selenium.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

def add_remove_from_cart(driver):

    elements = driver.find_elements("css selector", "button.btn_primary.btn_small.btn_inventory")
    
    # Add products to the cart:
    
    for element in elements:
            product_name = element.get_property("name")
            element.click()
            print('Running: Product ' + product_name.replace('add-to-cart-', '') + ' was added to the cart')
            logging.info('Product '+product_name.replace('add-to-cart-', '') + ' was added to the cart')
      
    # Removing products to the cart:        
    
    print('Running: Removing products from cart')
    driver.find_element("css selector", "a[class='shopping_cart_link']").click()
    logging.info('Removing products from cart')
    
    elements = driver.find_elements("css selector", "button.cart_button")
    
    for element in elements:
        product_name = element.get_property("name")
        element.click()
        print('Running: Product '+ product_name.replace('remove-', '') +' was removed from the cart')
        logging.info('Product '+product_name.replace('remove-', '') +' was removed from the cart')