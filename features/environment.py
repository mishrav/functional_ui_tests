from selenium import webdriver
from pyvirtualdisplay import Display
from features.pages.config import driver_config
from features.pages.config import base_page

def before_all(context):

    # desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    # desired_capabilities['version'] = '12'
    # desired_capabilities['platform'] = 'WINDOWS'
    # desired_capabilities['name'] = 'Testing Selenium 2 with Behave'
    # desired_capabilities['client_key'] = 'key'
    # desired_capabilities['client_secret'] = 'secret'
    context.driver = driver_config.driver()

    #context.browser = webdriver.Remote(
     #   desired_capabilities = desired_capabilities,
      #  command_executor = "http://hub.testingbot.com:4444/wd/hub"
    #)

def after_all(context):
    context.driver.quit()