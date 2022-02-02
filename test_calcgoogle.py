from re import search
from selenium import webdriver
driver = webdriver.Chrome('D:\chromedriver/chromedriver')

driver.get('https://www.google.ru/')

searchbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
searchbox.send_keys('калькулятор')
searchButton = driver.find_element_by_name('btnK')
searchButton.click()
searchbox = driver.find_elements_by_id('cwos')
searchbox.send_keys('1')
   