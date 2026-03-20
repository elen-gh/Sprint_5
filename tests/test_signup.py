import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import DeskLocators
from src.data import EMAIL_EXIST_USER, PASSWORD_EXIST_USER, INVALID_MASK_EMAIL
from src.helpers import get_sign_up_data

class TestDeskSignUp:

    def test_sign_up_new_user(self, driver):
        wait = WebDriverWait(driver, Config.TIMEOUT)
        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.AUTH_BUTTON)).click() 
        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.NO_ACCOUNT_BUTTON)).click() 

        email_data, password_data = get_sign_up_data()
        wait.until(expected_conditions.visibility_of_element_located(DeskLocators.EMAIL_FIELD)).send_keys(email_data)
        driver.find_element(*DeskLocators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*DeskLocators.CONFIRM_PASSWORD_FIELD).send_keys(password_data)

        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.CREATE_ACCOUNT_BUTTON)).click() 
        
        assert wait.until(expected_conditions.visibility_of_element_located(DeskLocators.AVATAR))
        assert wait.until(expected_conditions.visibility_of_element_located(DeskLocators.USER))

    @pytest.mark.parametrize("invalid_email", INVALID_MASK_EMAIL)
    def test_sign_up_invalid_mask_email(self, driver, invalid_email):
        wait = WebDriverWait(driver, Config.TIMEOUT)
        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.AUTH_BUTTON)).click() 
        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.NO_ACCOUNT_BUTTON)).click() 

        wait.until(expected_conditions.visibility_of_element_located(DeskLocators.EMAIL_FIELD))
        driver.find_element(*DeskLocators.EMAIL_FIELD).clear()
        driver.find_element(*DeskLocators.EMAIL_FIELD).send_keys(invalid_email)

        driver.find_element(*DeskLocators.PASSWORD_FIELD).send_keys(PASSWORD_EXIST_USER)
        driver.find_element(*DeskLocators.CONFIRM_PASSWORD_FIELD).send_keys(PASSWORD_EXIST_USER)

        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.CREATE_ACCOUNT_BUTTON)).click() 
        
        assert wait.until(expected_conditions.visibility_of_element_located(DeskLocators.ERROR))
        assert wait.until(expected_conditions.visibility_of_element_located(DeskLocators.EMAIL_ERROR_FIELD))
        assert wait.until(expected_conditions.visibility_of_element_located(DeskLocators.PASSWORD_ERROR_FIELD))
        assert wait.until(expected_conditions.visibility_of_element_located(DeskLocators.CONFIRM_PASSWORD_ERROR_FIELD))

        driver.refresh() 
        

    def test_sign_up_exist_user(self, driver):
        wait = WebDriverWait(driver, Config.TIMEOUT)
        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.AUTH_BUTTON)).click() 
        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.NO_ACCOUNT_BUTTON)).click() 

        wait.until(expected_conditions.visibility_of_element_located(DeskLocators.EMAIL_FIELD)).send_keys(EMAIL_EXIST_USER)
        driver.find_element(*DeskLocators.PASSWORD_FIELD).send_keys(PASSWORD_EXIST_USER)
        driver.find_element(*DeskLocators.CONFIRM_PASSWORD_FIELD).send_keys(PASSWORD_EXIST_USER)

        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.CREATE_ACCOUNT_BUTTON)).click() 
        
        assert wait.until(expected_conditions.visibility_of_element_located(DeskLocators.ERROR))
        assert wait.until(expected_conditions.visibility_of_element_located(DeskLocators.EMAIL_ERROR_FIELD))
        assert wait.until(expected_conditions.visibility_of_element_located(DeskLocators.PASSWORD_ERROR_FIELD))
        assert wait.until(expected_conditions.visibility_of_element_located(DeskLocators.CONFIRM_PASSWORD_ERROR_FIELD))