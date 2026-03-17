from selenium.webdriver.common.by import By

class DeskLocators:

    AUTH_BUTTON = By.XPATH, ".//button[text()='Вход и регистрация']"
    LOGIN_BUTTON = By.XPATH, "//button[@type='submit' and starts-with(@class, 'buttonPrimary')]"
    LOGOUT_BUTTON = By.XPATH, "//*[@class='spanGlobal btnSmall']"
    NO_ACCOUNT_BUTTON = By.XPATH, "//button[text()='Нет аккаунта']"
    CREATE_ACCOUNT_BUTTON = By.XPATH, "//button[text()='Создать аккаунт']"

    POST_AD_BUTTON = By.XPATH, "//button[text()='Разместить объявление']"
    PUBLISH_BUTTON = By.XPATH, "//button[text()='Опубликовать']"

    EMAIL_FIELD = By.XPATH, "//input[@name='email']"
    PASSWORD_FIELD = By.XPATH, "//input[@name='password']"
    CONFIRM_PASSWORD_FIELD = By.XPATH, "//input[@name='submitPassword']"

    AVATAR = By.XPATH, "//*[contains(@class, 'circleSmall')]//*[local-name()='svg']"
    USER = By.XPATH, "//*[@class='profileText name']"

    ERROR = By.XPATH, "//span[text()='Ошибка']"
    EMAIL_ERROR_FIELD = By.XPATH, "//*[contains(@class, 'inputError') and .//input[@name='email']]"
    PASSWORD_ERROR_FIELD = By.XPATH, "//*[contains(@class, 'inputError') and .//input[@name='password']]"
    CONFIRM_PASSWORD_ERROR_FIELD = By.XPATH, "//*[contains(@class, 'inputError') and .//input[@name='submitPassword']]"

    AUTH_MODAL = By.XPATH, "//*[contains(@class, 'popUp_inputColumn') and .//input[@name='email']]"

    TITLE_FIELD = By.XPATH, "//div[contains(@class, 'input_inputDefault')]//input[@name='name']"
    CATEGORY_DROPDOWN = By.XPATH, "//input[@name='category']/following-sibling::button"
    CONDITION_RADIO = By.XPATH, "//input[@value='Б/У']/following-sibling::div"
    CITY_DROPDOWN = By.XPATH, "//input[@name='city']/following-sibling::button"
    DESCRIPTION_FIELD = By.XPATH, "//div[contains(@class, 'textarea_inputDefault')]//textarea"
    PRICE_FIELD = By.XPATH, "//div[contains(@class, 'input_inputDefault')]//input[@name='price']"

    PROFILE_PAGE = By.XPATH, "//div[contains(@class, 'profilePage_shell')]"
    PROFILE_HEADER = (By.XPATH, "//h1[text()='Мой профиль']")
    PUBLISHED_AD = By.XPATH, "//div[contains(@class, 'card')]//*[text()='Полет на Луну']"