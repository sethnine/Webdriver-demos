from selenium import webdriver
import random

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("C:\Program Files\chromedriver.exe", options=options)

page_number=random.randrange(0,100) # pick a page 1 - 100
quote_number=random.randrange(0,30) # each page has 30 quotes so pick one of them
url = "https://www.goodreads.com/quotes?page={}".format(page_number)

driver.get("https://www.goodreads.com/quotes/tag/random")
elem = driver.find_elements_by_css_selector('.quoteText')[quote_number] # get only the specific quote
nl = "\n"
print(f"Random quote:{nl}{elem.get_attribute('innerText')}")
driver.quit()
