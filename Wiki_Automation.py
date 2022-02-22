import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path="/Users/anastasia/PycharmProjects/python_cctb/chromedriver")
driver = webdriver.Chrome(service=s)

wiki_url = "https://en.wikipedia.org/wiki/Main_Page"
wiki_search = "Python (programming language)"

def setUp():
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(wiki_url)
    wiki_title = driver.find_element(By.LINK_TEXT, "Wikipedia")
    if driver.current_url == wiki_url:
        assert wiki_title.is_displayed()
        print(f"Welcome to Wikipedia homepage -- {wiki_url}")
        print(f"We\'re seeing the title message -- 'Welcome to Wikipedia'")
    else:
        print(f"We are not on the Wikipedia's homepage. Check your code!")
        driver.close()
        driver.quit()

def search_python_link():
    driver.find_element(By.ID, "searchInput").send_keys(wiki_search)
    driver.find_element(By.LINK_TEXT, wiki_search).click()
    search_python_title = driver.find_element(By.XPATH, f'//h1[contains(., "Python (programming language")]')
    if search_python_title.is_displayed():
        print(f"The Python article is successfully displayed")
    else:
        print(f"The Python article is not displayed. Search again!")
sleep(0.25)

def click_main_logo():
    driver.find_element(By.XPATH, '//*[@id="p-logo"]').click()
    wiki_title = driver.find_element(By.LINK_TEXT, "Wikipedia")
    if driver.current_url == wiki_url:
        assert wiki_title.is_displayed()
        print(f"Welcome back to the Wikipedia homepage. The main page is displayed at: {datetime.datetime.now()}")
    else:
        print(f"You have not returned to the wiki's main page. Try again!")

def tearDown():
    if driver is not None:
        print(f"--------------------------------------------")
        print(f"Test Completed at: {datetime.datetime.now()}")
        driver.close()
        driver.quit()

setUp()
search_python_link()
click_main_logo()
tearDown()