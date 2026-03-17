import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from src.config import Config
from src.locators import DeskLocators
from src.helpers import get_sign_up_data 

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Config.BASE_URL)
    yield browser
    browser.quit()

@pytest.fixture
def new_user_data(driver):
    email_new_user, password_new_user = get_sign_up_data()

    wait = WebDriverWait(driver, Config.TIMEOUT)
    wait.until(expected_conditions.element_to_be_clickable(DeskLocators.AUTH_BUTTON)).click() 
    wait.until(expected_conditions.element_to_be_clickable(DeskLocators.NO_ACCOUNT_BUTTON)).click() 

    wait.until(expected_conditions.element_to_be_clickable(DeskLocators.EMAIL_FIELD)).send_keys(email_new_user)
    driver.find_element(*DeskLocators.PASSWORD_FIELD).send_keys(password_new_user)
    driver.find_element(*DeskLocators.CONFIRM_PASSWORD_FIELD).send_keys(password_new_user)

    wait.until(expected_conditions.element_to_be_clickable(DeskLocators.CREATE_ACCOUNT_BUTTON)).click() 

    wait.until(expected_conditions.visibility_of_element_located(DeskLocators.AVATAR))
    wait.until(expected_conditions.element_to_be_clickable(DeskLocators.LOGOUT_BUTTON)).click()

    return  email_new_user, password_new_user
