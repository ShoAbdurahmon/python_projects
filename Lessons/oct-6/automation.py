"""
from selenium import webdriver
from time import sleep


browser = webdriver.Chrome("/Users/abdurahmon/Desktop/oct-6")

browser.get("https://google.com/")

browser.fullscreen_window()

sleep(2)

browser.set_window_size(1000,800)

browser.save_screenshot("rasm.png")


browser.get("https://google.com/")
sleep(2)
browser.back()


searching_field = browser.find_element_by_xpath("")
searching_field.send_key("Python new books 2021")
sleep(2)

button = browser.find_element_by_xpath("")
button.click()
"""
# AUTOMATION
# SELENIUM

from selenium import webdriver
import time

browser = webdriver.Firefox("./")

#print(browser.page_source)
#print(browser.title)
#browser.fullscreen_window()
#time.sleep(2)
#browser.set_window_size(1980,1200)
#browser.save_screenshot("screenshot.png")
#browser.get("https://yandex.com/")
#time.sleep(2)
#browser.back()
#browser.quit()

browser.get("https://google.com/")

searching_field = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
searching_field.send_keys("Mayoq.uz")
time.sleep(3)

search_button = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]")
search_button.click()




browser.quit()