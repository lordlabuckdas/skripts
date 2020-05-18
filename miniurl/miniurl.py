#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
from time import sleep

#if geckodriver isn't in PATH, copy it to the folder of this file,
#uncomment next line and delete line 9
#driver=webdriver.Firefox(executable_path="./geckodriver") 
driver=webdriver.Firefox()
driver.get("https://bitly.com/")
sleep(1)
urll=driver.find_element_by_xpath('//*[@id="shorten_url"]')
urll.send_keys(pyperclip.paste())
urll.send_keys(Keys.RETURN)
driver.execute_script("window.scrollTo(0,400);")
sleep(0.5)
urll=driver.find_element_by_xpath('//*[@id="shortened_btn"]')
urll.click()
driver.quit()