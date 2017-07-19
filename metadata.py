from selenium import webdriver

url = 'http://magentofinal.mytriorings.com/layaway-plan'
meta_title = ''
meta_description = ''

browser = webdriver.Chrome(r'C:\bin\selenium\chromedriver230.exe')
browser.get(url)

page_title = browser.title
page_description = browser.find_element_by_xpath("//meta[@name='description']").get_attribute("content")

print(page_title)
print(page_description)

browser.quit()
