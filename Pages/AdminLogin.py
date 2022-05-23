from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Admin:
    
    Member_id = "[type='text']"
    Select_Local = "ctl00_Main_myBox_ddlLocaleSelector"
    Click_Login = "ctl00_Main_myBox_doLogIn"


    def __init__(self,driver):
        self.driver = driver

    def setmemberid(self,memberid):
        Login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.Member_id)))
        Login.send_keys(memberid, Keys.ENTER)
        
        

    def selectlocal(self,local):
        Select_local = Select(self.driver.find_element_by_id(self.Select_Local))
        for opt in Select_local.options:
            Select_local.select_by_visible_text(local)
        
    def clicklogin(self):
        login_button = self.driver.find_element_by_id(self.Click_Login)
        login_button.click()



    