import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()

url='http://newtours.demoaut.com/mercurywelcome.php'

driver.get(url)

user_name = driver.find_element('name', 'userName')
user_pass = driver.find_element('name', 'password')
sign_in = driver.find_element('name', 'login')

user_name.send_keys('tutorial')
user_pass.send_keys('tutorial')
sign_in.click()

driver.find_element_by_css_selector("input[type='radio'][value='oneway']").click()

passengers = Select(driver.find_element_by_name('passCount'))

passengers.select_by_visible_text('3')
