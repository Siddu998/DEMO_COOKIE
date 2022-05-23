import pytest
import time
from POM.AdminPage import Admin_Login_Page
from POM.RulesPage import Rules_Setup_Page
from Pages.Cookie_Capture import Cookie




class Test_DS_login:

    
    Re_Rule = "https://app.requestly.io/rules/#sharedList/1641928973304-My-rules"   
    requestly_url = "https://app.requestly.io/rules/my-rules"
    Local_URL = "https://zus2prs.myherbalife.com/it-IT/Home/Default/Ds"
    memberid = "staff"
    local = "Italy - Italiano"
    RuleName = "MYHL_Test"
    Containt = "satelliteLib-12930be22558042bc632cff190e4776deb189a2a.js"
    Redirect = "https://assets.adobedtm.com/78ef23cd3941/4d66435cf9ad/launch-6c390220da59-development.min.js"
    CurrentURL = "https://zus2prs-myhladmin.myherbalife.com/DistributorRelations/MyHLUtils.aspx"

    #Admin Login MYHL
    def test_Login(self,setup):
        self.driver = setup
        allTabs = self.driver.window_handles
        print (allTabs)

        for tab in allTabs:
            self.driver.switch_to.window(tab)
            if(self.driver.current_url == self.Re_Rule):
                self.Rul_Set = Rules_Setup_Page(self.driver)
                time.sleep(5)
                print("Rules Created")
                window_after = self.driver.window_handles[1]
                self.driver.switch_to.window(window_after)
                self.Adm_Log = Admin_Login_Page(self.driver)
                time.sleep(5)
                print("Admin Login Pass")
                window_after = self.driver.window_handles[3]
                self.driver.switch_to.window(window_after)
                if(self.driver.current_url == self.Local_URL):
                    print("TC_001 Pass---\n",self.driver.current_url)
                else:
                    print("TC_001 Fail")
                self.driver.quit()
                time.sleep(3)
                self.CK_Capture = Cookie(self.driver)
                self.CK_Capture.cookiesCapture()
                
                
                
                



