import sys
import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import lab17_locators as locators
from selenium.webdriver.support.ui import Select

s = Service(executable_path="/Users/anastasia/PycharmProjects/python_cctb/chromedriver")
driver = webdriver.Chrome(service=s)

def setUp():
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.opencart_url)
    sleep(2)
    if driver.current_url == locators.opencart_url and driver.title == "OpenCart - Open Source Shopping Cart Solution":
        print(f"Welcome to the OpenCart main page! -- {locators.opencart_url}")
        print(f"We\'re seeing the app's logo -- 'OPENCART'")
    else:
        print(f"We are not on the OpenCart's's homepage. Check your code!")
        driver.close()
        driver.quit()
sleep(5)

def register_new_user():
    driver.find_element(By.LINK_TEXT, "REGISTER").click()
    sleep(0.25)
    assert driver.current_url == locators.register_url
    driver.find_element(By.ID, "input-username").send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.ID, "input-firstname").send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, "input-lastname").send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, "input-email").send_keys(locators.email)
    sleep(0.25)
    Select(driver.find_element(By.ID, "input-country")).select_by_visible_text("Canada")
    sleep(0.25)
    driver.find_element(By.ID, "input-password").send_keys(locators.new_password)
    sleep(5)
    # IMPORTANT NOTE: Click  the security feature "CAPTCHA" manually!
    driver.find_element(By.XPATH, "//button[contains(., 'Register')]").click()
    sleep(0.25)
    if driver.find_element(By.ID, "account-register-success").is_displayed():
       print(f"A new user - Username: {locators.new_username} and Password: {locators.new_password} has ben successfully created!")

def login_as_new_user():
    driver.find_element(By.LINK_TEXT, "LOGOUT").click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, "LOGIN").click()
    sleep(0.25)
    if driver.find_element(By.NAME, "email").is_displayed():
        sleep(0.25)
        driver.find_element(By.CSS_SELECTOR, "input#input-email").send_keys(locators.email)
        sleep(0.25)
        driver.find_element(By.CSS_SELECTOR, "input#input-password").send_keys(locators.new_password)
        sleep(0.25)
        driver.find_element(By.XPATH, "//button[contains(., 'Login')]").click()
        sleep(0.25)
    if driver.find_element(By.XPATH, "//h3[contains(., 'Setup PIN for your account')]"):
        driver.find_element(By.CSS_SELECTOR, "input#input-pin").send_keys(locators.PIN_number)
        sleep(0.25)
        print(f"A PIN number: {locators.PIN_number} for a new user has been created and recorded")
        driver.find_element(By.XPATH, "//button[contains(., 'Submit')]").click()
        sleep(0.25)

def click_Marketplace():
    driver.find_element(By.LINK_TEXT, "Marketplace").click()
    sleep(0.25)
    if driver.current_url == locators.marketplace_url:
        assert driver.find_element(By.XPATH, "//h1[text() = 'Welcome to OpenCart Extension Store']").is_displayed()
    driver.find_element(By.LINK_TEXT, "Marketplaces").click()
    sleep(0.25)
    driver.find_element(By.XPATH, "//a[text() = 'Free']").click()
    # driver.find_element(By.XPATH, "//input[@name='OpenCart Partners']").click()
    # driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='OpenCart Partners']")[2].click()
    # driver.find_element(By.CSS_SELECTOR, "input#category_id=20&filter_license=0&filter_partner=partner']").click()
    sleep(0.25)
    print(f"'Marketplace' page {locators.marketplace_url} is displayed. The option 'FREE' has been chosen for demo purposes")

def click_Resources():
    driver.find_element(By.CLASS_NAME, "caret").click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, "Contact Us").click()
    if driver.current_url == locators.contact_us_url:
        assert driver.find_element(By.XPATH, "//h1[text() = 'Contact Us']").is_displayed()
        print(f"'Contact Us' page {locators.contact_us_url} is displayed")
        sleep(0.25)

def log_out_new_user():
    driver.find_element(By.LINK_TEXT, "LOGOUT").click()
    if driver.current_url == locators.homepage_url and driver.title == "OpenCart - Open Source Shopping Cart Solution":
        print(f"Welcome back to the OpenCart home page! -- {locators.homepage_url}")
        print(f"We\'re seeing the app's logo again -- 'OPENCART'")
    else:
        print(f"We are not back on the OpenCart's's homepage. Check your code!")
        driver.close()
        driver.quit()


def tearDown():
    if driver is not None:
        print(f"--------------------------------------------")
        print(f"Test Completed at: {datetime.datetime.now()}")
        driver.close()
        driver.quit()
        #Make a log file
        old_instance = sys.stdout
        log_file = open("message.log", "w")
        sys.stdout = log_file
        print(f"Email: {locators.email} \nUsername: {locators.new_username}\nPassword: {locators.new_password}\nPIN: {locators.PIN_number}")
        sys.stdout = old_instance
        log_file.close()

setUp()
register_new_user()
login_as_new_user()
click_Marketplace()
click_Resources()
log_out_new_user()
tearDown()