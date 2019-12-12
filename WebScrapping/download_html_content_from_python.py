#import modules
from selenium import webdriver

url = "https://python.org"

# create driver
browser = webdriver.Chrome()
browser.get(url)

html_content = browser.page_source
print(html_content)