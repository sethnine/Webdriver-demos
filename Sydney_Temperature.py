from selenium import webdriver
import os

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("C:\Program Files\chromedriver.exe", options=options)

driver.get("http://www.bom.gov.au/nsw/forecasts/sydney.shtml")
elem = driver.find_element_by_css_selector('.forecast')
elem2 = elem.find_element_by_css_selector('.max')
#print(elem.get_attribute("innerHTML"), elem2.get_attribute("innerText"))
print(f"Sydney max forecast: {elem2.get_attribute('innerText')} degrees centergrade")
driver.quit()
