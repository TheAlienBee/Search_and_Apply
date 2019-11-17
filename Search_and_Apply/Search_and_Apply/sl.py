# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 09:33:32 2019

@author: bkermani
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
 
# The place we will direct our WebDriver to
url = 'https://www.indeed.com/viewjob?jk=9a47091324121975&q=software+engineering&l=Fairfax%2C+VA&tk=1dpqgel6043q4801&from=web&advn=210908886952977&adid=316206168&sjdu=RjrjP3TXJPtsBLro8K2Df0eyZufxG4-d7TYf78ErEElqOKNzJSU6jNy6SYTmMDBX5B6n1m6-clrgeJ9lT_OSyNM7hw_E48gt40O8og-gXrT3hiLiXR6JwosXsqBge2WCH14MaOLQUB1AdamR_OggC0MmXkxeodWiaIYpT28LUbGBYbfR8Sy8fFck9lsupkGtL0qPBpSv2WO3m8sPf82mc287bIAuW6NVy2wP1fN2vC5cDGlzx1TN1kGkbsro7qCD&acatk=1dpqgen8q5he4800&pub=4a1b367933fd867b19b072952f68dceb&vjs=3'
# Creating the WebDriver object using the ChromeDriver
driver = webdriver.Chrome()

# Directing the driver to the defined url
driver.get(url)


apply_button = driver.find_element_by_xpath('//*[@id="indeedApplyButtonContainer"]/span/div[2]/button/div')
apply_button.click()


driver.switch_to_default_content()

# Directing the driver to the popped up new frame

wait = ui.WebDriverWait(driver, 20)
frame = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/iframe")))
driver.switch_to.frame(frame)
wait.until(EC.frame_to_be_available_and_switch_to_it(0))

# filling out the form

# filling name
text_name = driver.find_element_by_xpath("//*[@id='input-applicant.name']")
try:     
    wait = ui.WebDriverWait(driver, 20)
    text_name.clear()
    text_name.send_keys("John Smith")
except StaleElementReferenceException as Exception:
    print('StaleElementReferenceException while trying to type title')
    text_name = driver.find_element_by_xpath("//*[@id='input-applicant.name']")
    text_name.clear()
    text_name.send_keys("John Smith")

# filling email
text_email = driver.find_element_by_xpath('//*[@id="input-applicant.email"]')    
try:     
    wait = ui.WebDriverWait(driver, 20)
    text_email.clear()
    text_email.send_keys("applysmith2345@gmail.com")
except StaleElementReferenceException as Exception:
    print('StaleElementReferenceException while trying to type title')
    text_email = driver.find_element_by_xpath('//*[@id="input-applicant.email"]')
    text_email.clear()
    text_email.send_keys("applysmith2345@gmail.com")

# filling phone
text_phone = driver.find_element_by_xpath('//*[@id="input-applicant.phoneNumber"]')   
try:     
    wait = ui.WebDriverWait(driver, 20)
    text_phone.clear()
    text_phone.send_keys("111-222-3456")
except StaleElementReferenceException as Exception:
    print('StaleElementReferenceException while trying to type title')
    text_phone = driver.find_element_by_xpath('//*[@id="input-applicant.phoneNumber"]')
    text_phone.clear()
    text_phone.send_keys("111-222-3456")
    
   


wait = ui.WebDriverWait(driver, 5)

# switch back to parent window
#driver.switch_to_default_content()

###################
#driver.quit()


