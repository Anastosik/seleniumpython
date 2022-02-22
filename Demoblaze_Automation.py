import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path="/Users/anastasia/PycharmProjects/python_cctb/chromedriver")
driver = webdriver.Chrome(service=s)

demoblz_url = "https://www.demoblaze.com/"

def setUp():
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(demoblz_url)
    sleep(2)
    demoblz_title = driver.find_element(By.XPATH, '//*[@id="nava"]')
    if driver.current_url == demoblz_url:
        assert demoblz_title.is_displayed()
        print(f"Welcome to Demoblaze homepage -- {demoblz_url}")
        print(f"We\'re seeing the store's logo -- 'PRODUCT STORE'")
    else:
        print(f"We are not on the Demoblaze's homepage. Check your code!")
        driver.close()
        driver.quit()
sleep(2)

def click_nexus6():
        driver.find_element(By.LINK_TEXT, "Nexus 6").click()
        sleep(2)
        nexus6_url = "https://www.demoblaze.com/prod.html?idp_=3"
        nexus6_title = driver.find_element(By.XPATH, '//h2[contains(., "Nexus 6")]')
        if driver.current_url == nexus6_url:
            assert nexus6_title.is_displayed()
            print(f"'Nexus 6' Page is opened at: {datetime.datetime.now()}")
        else:
            print(f"'Nexus 6' page is not opened. Try again!")
sleep(2)

def manipulate_cart_nexus6():
    driver.find_element(By.LINK_TEXT, "Add to cart").click()
    driver.find_element(By.LINK_TEXT, "Cart").click()
    sleep(2)
    if driver.find_element(By.XPATH, '//td[contains(., "Nexus 6")]'):
        print(f"The item 'Nexus 6' is successfully added to cart. The Order page is displayed.")
    else:
        print(f"The Order page of 'Nexus 6' is not displayed. Try again!")
    driver.find_element(By.LINK_TEXT, "Delete").click()
sleep(2)

def tearDown():
    if driver is not None:
        print(f"--------------------------------------------")
        print(f"The product item has been removed. Test Completed at: {datetime.datetime.now()}")
        driver.close()
        driver.quit()

setUp()
click_nexus6()
manipulate_cart_nexus6()
tearDown()