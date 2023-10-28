from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
options = Options()
options.add_experimental_option("prefs",{
    "download.default_directory": "C:\Users\EDU-1\Desktop\Downloading_files",
    "download.prompt_for_download": False,
    
})

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("http://192.168.43.59/moodle")
driver.maximize_window()

login = driver.find_elements("xpath","/html/body/div[2]/nav/div/div[2]/div/div/span/a")
login[0].click()
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(3)

# fill_username = driver.find_elements("xpath","/html/body/div[2]/div[4]/div[2]/div/div/section/div/div/div/div/form[1]/div[1]/input")
# fill_username[0].send_keys(userName)
# driver.switch_to.window(driver.window_handles[2])
# time.sleep(3)
userName = driver.find_elements("xpath","/html/body/div[2]/div[4]/div[2]/div/div/section/div/div/div/div/form[1]/div[1]/input")[0].send_keys("Mrcoder")
userName = driver.find_elements("xpath","/html/body/div[2]/div[4]/div[2]/div/div/section/div/div/div/div/form[1]/div[2]/input")[0].send_keys("M@@dleAdmin123456")
login2 = driver.find_elements("xpath","/html/body/div[2]/div[4]/div[2]/div/div/section/div/div/div/div/form[1]/div[3]/button")[0].click()
########################################################################
#Back to Menu Function
def homeMenuFun():
    login2 = driver.find_elements("xpath","/html/body/div[3]/nav/div/div[1]/nav/ul/li[1]/a")[0].click()
################################################################

#Scrolling Function
def scroll_page(page):
    i=0
    while i < page:
    
        driver.find_elements(by=By.TAG_NAME, value="body")[0].send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        i+=1
################################################################################################
homeMenuFun()
scroll_page(7)
loginTogeogrophy = driver.find_elements("xpath","/html/body/div[3]/div[7]/div/div[3]/div/section/div/div[2]/div/div/div[27]/div/div[2]/h5/a")[0].click()

scroll_page(3)
homeMenuFun()

loginTohistory = driver.find_elements("xpath","/html/body/div[3]/div[7]/div/div[3]/div/section/div/div[2]/div/div/div[26]/div/div[2]/h5/a")[0].click()

scroll_page(3)

homeMenuFun()
scroll_page(6)
loginToEnglish = driver.find_elements("xpath","/html/body/div[3]/div[7]/div/div[3]/div/section/div/div[2]/div/div/div[21]/div/div[2]/h5/a")[0].click()

loginToGrade = driver.find_elements("xpath","/html/body/div[3]/div[6]/div/div[2]/nav/ul/li[4]/a")[0].click()
loginToGraderReport = driver.find_elements("xpath","/html/body/div[3]/div[5]/div/div[3]/div/section/div/div[1]/div/div[1]/nav/div/div")[0].click()
scroll_page(1)
time.sleep(1)                                     
loginToExport = driver.find_elements("xpath","/html/body/div[3]/div[5]/div/div[3]/div/section/div/div[1]/div/div[1]/nav/div/ul/li[3]/ul/li[5]")[0].click()
scroll_page(1)
loginToDownload = driver.find_elements("xpath","/html/body/div[2]/div[5]/div/div[3]/div/section/div/form/div[3]/div[2]/input")[0].click()
