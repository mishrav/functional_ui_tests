from behave import *

@when('we visit google')
def step(context):
   context.driver.get('http://www.google.com')

@then('it should have a title "Google"')
def step(context):
   assert context.driver.title == "Google"