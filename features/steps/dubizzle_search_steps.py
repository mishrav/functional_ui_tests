from behave import *
from features.pages.config.driver_config import driver
from features.pages.page_class import dubizzle_homepage
from features.pages.page_class.dubizzle_homepage import DubizzleHomepage

use_step_matcher("re")



@given("I am on dubizzle dubai home page")
def step_impl(context):
    homepage = DubizzleHomepage(context.driver)
    homepage.go_to()


@when("I check for content")
def step_impl(context):
    assert True is True


@then("I the title of home page should be (dubizzle Dubai Classifieds)")
def step_impl(context,expected_title):
    homepage = DubizzleHomepage(context.driver)
    assert homepage.verify_title(expected_title) is True


@step("I should see (place an ad option|search form|quick links)")
def step_impl(context,link):
    homepage = DubizzleHomepage(context.driver)
    assert homepage.element_is_visible(link) is True