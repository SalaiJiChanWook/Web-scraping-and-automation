from selenium import webdriver
from selenium.webdriver.common.by import By
################################

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time


################################
options = Options()
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_experimental_option("detach",True)
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

# list_data = []

def initialize_browser():
    driver.get("https://eimaung.com/pwd2022/")
    print("Starting driver...")
    click_button = driver.find_element(by=By.CLASS_NAME, value="pre-order-link")
    click_button.click()

initialize_browser()