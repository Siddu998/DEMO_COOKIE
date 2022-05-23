from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
import os
import time
from selenium.webdriver.chrome.options import Options


baseURL = "https://zus2prs-myhladmin.myherbalife.com/DistributorRelations/MyHLUtils.aspx"

@pytest.fixture
def setup():
    executable_path = r"C:\Users\nagarajud-c\Desktop\Demo_Cookie\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = executable_path
    options = Options()
    options.add_extension(r'C:\Users\nagarajud-c\Desktop\Demo_Cookie\Requestly--Redirect-Url--Modify-Headers-etc.crx')

    driver = webdriver.Chrome(executable_path=executable_path, options = options)
    driver.maximize_window()
    
    driver.get(baseURL)
    time.sleep(3)
    driver.execute_script("window.open('https://app.requestly.io/rules/#sharedList/1641928973304-My-rules','new window')")
    allTabs = driver.window_handles

    return driver
