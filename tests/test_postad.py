from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import DeskLocators
from src.data import TITLE, CATEGORY, CITY
from src.helpers import get_ad_data
import time

class TestDeskPostAd:

    def test_post_ad_unauth_user(self, driver):
        wait = WebDriverWait(driver, Config.TIMEOUT)
        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.POST_AD_BUTTON)).click() 
        assert wait.until(expected_conditions.visibility_of_element_located(DeskLocators.AUTH_MODAL))

    def test_post_ad_auth_user(self, driver, new_user_data):
        email_new_user, password_new_user = new_user_data
        wait = WebDriverWait(driver, Config.TIMEOUT)
        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.AUTH_BUTTON)).click()

        wait.until(expected_conditions.visibility_of_element_located(DeskLocators.EMAIL_FIELD)).send_keys(email_new_user)
        driver.find_element(*DeskLocators.PASSWORD_FIELD).send_keys(password_new_user)

        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.LOGIN_BUTTON)).click()
        wait.until(expected_conditions.visibility_of_element_located(DeskLocators.AVATAR))

        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.POST_AD_BUTTON)).click()

        description, price = get_ad_data()
        wait.until(expected_conditions.visibility_of_element_located(DeskLocators.TITLE_FIELD)).send_keys(TITLE)

        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.CATEGORY_DROPDOWN)).click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, f"//button[./span[text()='{CATEGORY}']]"))).click()

        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.CONDITION_RADIO)).click()

        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.CITY_DROPDOWN)).click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, f"//button[./span[text()='{CITY}']]"))).click()

        wait.until(expected_conditions.visibility_of_element_located(DeskLocators.DESCRIPTION_FIELD)).send_keys(description)
        wait.until(expected_conditions.visibility_of_element_located(DeskLocators.PRICE_FIELD)).send_keys(price)
        time.sleep(5)
        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.PUBLISH_BUTTON)).click()
        time.sleep(2)
        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.AVATAR)).click()

        wait.until(expected_conditions.url_contains("/profile"))
        
        assert wait.until(expected_conditions.visibility_of_element_located(DeskLocators.PUBLISHED_AD))
        
        