import pytest
from Pages.AdminLogin import Admin
from Pages.RulesSetup import Rules_Setup
from Pages.CookieBanner import Cookie_Banner
from Pages.PreferenceCenter import Preference_Center
from POM.AdminPage import Admin_Login_Page
 
from selenium.webdriver.common.keys import Keys



import time









class Test_DS_login:
    
    requestly_url = "https://app.requestly.io/rules/my-rules"
    Local_URL = "https://zus2prs.myherbalife.com/it-IT/Home/Default/Ds"

    memberid = "staff"
    local = "Italy - Italiano"
    RuleName = "MYHL_Test"
    Containt = "satelliteLib-12930be22558042bc632cff190e4776deb189a2a.js"
    Redirect = "https://assets.adobedtm.com/78ef23cd3941/4d66435cf9ad/launch-6c390220da59-development.min.js"
    CurrentURL = "https://zus2prs-myhladmin.myherbalife.com/DistributorRelations/MyHLUtils.aspx"
    



    def test_homePageTitle(self,setup):
        
        self.driver = setup
        allTabs = self.driver.window_handles
        print (allTabs)
        for tab in allTabs:
            self.driver.switch_to.window(tab)
            if(self.driver.current_url == self.CurrentURL):
        
                time.sleep(5)
            act_title = self.driver.title
            if act_title == "https://zus2prs-myhladmin.myherbalife.com/DistributorRelations/MyHLUtils.aspx":
                assert True
                time.sleep(5)
                self.driver.quit()
            else:
                self.driver.save_screenshot(".\\Screenshorts\\"+"test_homePageTitle")
                time.sleep(5)
                self.driver.quit()
                assert False
                

    #Admin Login MYHL
    def test_Login(self,setup):
        

        self.driver = setup
        allTabs = self.driver.window_handles
        print (allTabs)

        for tab in allTabs:
            self.driver.switch_to.window(tab)
            if(self.driver.current_url == self.CurrentURL):
                self.Adm_Log = Admin_Login_Page(self.driver)
                time.sleep(5)
                self.driver.quit()

    # Setup Rules & Validate Cookie Banner
    def test_SetupRules_(self,setup):
                
        self.driver = setup
        allTabs = self.driver.window_handles
        print (allTabs)
        cookie_names_captured = []
        
        
        for tab in allTabs:
            self.driver.switch_to.window(tab)
            if(self.driver.current_url == self.requestly_url):
                self.RL = Rules_Setup(self.driver)
                self.RL.set_Rule_click()
                self.RL.set_RuleName(self.RuleName)
                self.RL.Set_RuleContaint(self.Containt)
                self.RL.Set_RuleRedirect(self.Redirect)
                self.RL.CreateRule_Click()
                self.RL.SaveRule_Click()

            if(self.driver.current_url== self.baseURL):
                self.lp = Admin(self.driver)
                self.lp.setmemberid(self.memberid)
                self.lp.selectlocal(self.local)
                self.lp.clicklogin()

            if (self.driver.current_url == self.Local_URL):
                CK = Cookie_Banner(self.driver)
                CK.Validate_Banner_Text
                time.sleep(5)
                CK.Click_CookieSetting()
                self.driver.quit()

     # Preference selection
    def test_Preference_Category_Textvalidation(self,setup):
                
        self.driver = setup
        allTabs = self.driver.window_handles
        print (allTabs)
        cookie_names_captured = []
        
        
        for tab in allTabs:
            self.driver.switch_to.window(tab)
            if(self.driver.current_url == self.requestly_url):
                self.RL = Rules_Setup(self.driver)
                self.RL.set_Rule_click()
                self.RL.set_RuleName(self.RuleName)
                self.RL.Set_RuleContaint(self.Containt)
                self.RL.Set_RuleRedirect(self.Redirect)
                self.RL.CreateRule_Click()
                self.RL.SaveRule_Click()

            if(self.driver.current_url== self.baseURL):
                self.lp = Admin(self.driver)
                self.lp.setmemberid(self.memberid)
                self.lp.selectlocal(self.local)
                self.lp.clicklogin()

            if (self.driver.current_url == self.Local_URL):
                self.CB = Cookie_Banner(self.driver)
                self.CB.Validate_Banner_Text()
                time.sleep(5)
                self.CB.Click_CookieSetting()
                self.PC = Preference_Center(self.driver)
                self.PC.Validate_Strictly_Text()
                self.PC.Validate_Analitic_Text()
                self.PC.Validate_Targeting_Text()
                self.PC.Validate_Preference_Text()
                self.PC.Validate_Performance_Text()
                time.sleep(5)
                self.driver.quit()               

                    
                

                






