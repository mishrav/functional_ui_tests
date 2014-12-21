from page_objects import PageObject, PageElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import re
from selenium.webdriver.common.by import By


class DubizzleHomepage(PageObject):

    place_an_ad_option = PageElement(id_='place_an_ad_callout_en')
    search_form = PageElement(id_='search-widget-form')
    quick_links = PageElement(id_='quick-links')

    def __init__(self, driver):
        super(DubizzleHomepage, self).__init__(driver)
        self.fn = None
        self.driver = driver


    def go_to(self, local='dubai'):
        self.driver.get(self.homepage_url(local))

    def homepage_url(self, local):
        site_url = ''
        if local == 'dubai':
            return 'http://dubai.dubizzle.com'
        elif local == 'other blah':
            return ""
        else:
            return 'super blah'

    def verify_title(self, expected):
        actual = self.driver.title
        if re.search(expected, actual):
            return True
        else:
            return False

    def element_is_visible(self, link):
        fn_string = link.replace(" ", "_")
        fn = eval('self.'+fn_string)
        var = fn.is_displayed()
        return fn.is_displayed()




