from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from pyvirtualdisplay import Display


def driver(type="local"):
    # display = Display(visible=0, size=(1024, 768))
    # display.start()
    if type == 'local':
        return webdriver.Firefox()


def find(self, context):
        try:
            return context.find_element(*self.locator)
        except NoSuchElementException:
            return None

