from selenium import webdriver
import requests
import unittest
import sys

class LandingPagesUrlsTest(unittest.TestCase):

    def setUp(self):
        chrome_path = r'C:\bin\selenium\chromedriver230.exe'
        base_url = "http://magentofinal.mytriorings.com/"
        path = "about"
        url = base_url + path
        self.browser = webdriver.Chrome(chrome_path)
        self.browser.get(url)
        self.browser.title

    def test_page_ulrs_status(self):
        status_msg = ""
        has_broken_urls = False
        main_container = self.browser.find_element_by_class_name("main-container")
        links = main_container.find_elements_by_tag_name("a")
        for link in links:
            link_text = link.text
            link_href = link.get_attribute("href")
            hash_pos = link_href.find('#')
            http_status = requests.get(link_href).status_code
            try:
                self.assertEqual(200, http_status)
                status_msg = "OK"
                if link_href == '#':
                    status_msg = "TEMPORARY"
            except AssertionError as e:
                status_msg = "ERROR - {}".format(e)
                has_broken_urls = True
            print("{} - {} | {} - {}".format(http_status, link_href, link_text, status_msg))
        self.assertFalse(has_broken_urls)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
