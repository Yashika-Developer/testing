from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://careers.xenonstack.com/onboarding/login")

@when('I enter valid credentials')
def step_impl(context):
    context.driver.find_element_by_id("email").send_keys("ybajaj256@email.com")
    context.driver.find_element_by_id("password").send_keys("Samarava@123")

@when('I enter invalid credentials')
def step_impl(context):
    context.driver.find_element_by_id("email").send_keys("invalid@email.com")
    context.driver.find_element_by_id("password").send_keys("invalidpassword")

@when('I click the login button')
def step_impl(context):
    context.driver.find_element_by_id("submit").click()
    time.sleep(2)  # Wait for the page to load

@then('I should be redirected to the dashboard')
def step_impl(context):
    assert context.driver.current_url == "https://careers.xenonstack.com/onboarding/employee/modules"


@then('I should see an error message')
def step_impl(context):
    error_message = context.driver.find_element_by_id("error").text
    assert "Invalid credentials" in error_message

@then('I close the browser')
def step_impl(context):
    context.driver.quit()
