#import modules
from selenium import webdriver

# create driver
browser = webdriver.Chrome()


browser.get("http://python.org")

html_content = browser.page_source
print(html_content)

browser.quit()