from selenium import webdriver
import requests

url = "http://magentofinal.mytriorings.com/layaway-plan"

browser = webdriver.Chrome(r'C:\bin\selenium\chromedriver230.exe')
browser.get(url)
main_container = browser.find_element_by_class_name("main-container")
# print(main_container.text)
links = main_container.find_elements_by_tag_name("a")

for link in links:
    print(link.get_attribute("href"))
    print(requests.get(link.get_attribute("href")).status_code)

browser.quit()
