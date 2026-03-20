from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import DeskLocators
from src.data import EMAIL_EXIST_USER, PASSWORD_EXIST_USER

class TestDeskLogIn:
    
    def test_log_in(self, driver):
        wait = WebDriverWait(driver, Config.TIMEOUT)
        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.AUTH_BUTTON)).click()

        email_field = wait.until(expected_conditions.visibility_of_element_located(DeskLocators.EMAIL_FIELD))
        email_field.send_keys(EMAIL_EXIST_USER)
        driver.find_element(*DeskLocators.PASSWORD_FIELD).send_keys(PASSWORD_EXIST_USER)

        wait.until(expected_conditions.element_to_be_clickable(DeskLocators.LOGIN_BUTTON)).click()

        assert wait.until(expected_conditions.visibility_of_element_located(DeskLocators.AVATAR))
        assert wait.until(expected_conditions.visibility_of_element_located(DeskLocators.USER))
        