import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
# Navigate to the application home page
driver.get("https://www.google.com")
# get the search textbox
search_field = driver.find_element_by_name("q")
search_field.clear()
# enter search keyword and submit
search_field.send_keys("openwisp")
search_field.submit()
# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name method
lists= driver.find_elements_by_class_name("r")
# get the number of elements found
print ("Found " + str(len(lists)) + " searches:")
# close the browser window
driver.quit()
