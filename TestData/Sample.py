import pytest
from TestCases.AdminPage import Admin_Login_Page
from TestCases.RulesPage import Rules_Setup_Page
from TestCases.CookieBannerPage import Banner_Validation
from PageObject.CookieBanner import Cookie_Banner
from selenium.webdriver.common.keys import Keys
from TestCases.Preference_Text_validation import Pref_Text_validation
from PageObject.PreferenceCenter import Preference_Center
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

    #Admin Login MYHL
    # def test_AdminLogin(self,setup):
    #     self.driver = setup
    #     allTabs = self.driver.window_handles
    #     print (allTabs)

    #     for tab in allTabs:
    #         self.driver.switch_to.window(tab)
    #         if(self.driver.current_url == self.requestly_url):
    #             self.Rul_Set = Rules_Setup_Page(self.driver)
    #             time.sleep(5)
    #             print("Rules Created")
    #             window_after = self.driver.window_handles[1]
    #             self.driver.switch_to.window(window_after)
    #             self.Adm_Log = Admin_Login_Page(self.driver)
    #             time.sleep(5)
    #             print("Admin Login Pass")
    #             print("Tc_001_Pass")
    #             self.driver.quit()
    
    def test_CookieBanner_Validation(self,setup):
        self.driver = setup
        allTabs = self.driver.window_handles
        print (allTabs)
        for tab in allTabs:
            self.driver.switch_to.window(tab)
            if(self.driver.current_url == self.requestly_url):
                self.Rul_Set = Rules_Setup_Page(self.driver)
                print("Rules Created")
                window_after = self.driver.window_handles[1]
                self.driver.switch_to.window(window_after)
                self.Adm_Log = Admin_Login_Page(self.driver)
                print("Admin Login Pass")
                window_after = self.driver.window_handles[3]
                self.driver.switch_to.window(window_after)
                self.CB = Cookie_Banner(self.driver)
                self.CB.Validate_Banner_Text()
                print("Tc_002_Pass")
                self.driver.quit()

    # def test_AcceptAll(self,setup):
    #     self.driver = setup
    #     allTabs = self.driver.window_handles
    #     print (allTabs)
    #     for tab in allTabs:
    #         self.driver.switch_to.window(tab)
    #         if(self.driver.current_url == self.requestly_url):
    #             self.Rul_Set = Rules_Setup_Page(self.driver)
    #             print("Rules Created")
    #             window_after = self.driver.window_handles[1]
    #             self.driver.switch_to.window(window_after)
    #             self.Adm_Log = Admin_Login_Page(self.driver)
    #             print("Admin Login Pass")
    #             window_after = self.driver.window_handles[2]
    #             self.driver.switch_to.window(window_after)
    #             self.CB = Cookie_Banner(self.driver)
    #             self.CB.Click_AcceptAll()
    #             print("Tc_003_Pass")
    #             self.driver.quit()

    # def test_RejectAll(self,setup):
    #     self.driver = setup
    #     allTabs = self.driver.window_handles
    #     print (allTabs)
    #     for tab in allTabs:
    #         self.driver.switch_to.window(tab)
    #         if(self.driver.current_url == self.requestly_url):
    #             self.Rul_Set = Rules_Setup_Page(self.driver)
    #             print("Rules Created")
    #             window_after = self.driver.window_handles[1]
    #             self.driver.switch_to.window(window_after)
    #             self.Adm_Log = Admin_Login_Page(self.driver)
    #             print("Admin Login Pass")
    #             window_after = self.driver.window_handles[2]
    #             self.driver.switch_to.window(window_after)
    #             self.CB = Cookie_Banner(self.driver)
    #             self.CB.Click_RejectAll()
    #             print("Tc_004_Pass")
    #             self.driver.quit()

    # def test_CookieSetting(self,setup):
    #     self.driver = setup
    #     allTabs = self.driver.window_handles
    #     print (allTabs)
    #     for tab in allTabs:
    #         self.driver.switch_to.window(tab)
    #         if(self.driver.current_url == self.requestly_url):
    #             self.Rul_Set = Rules_Setup_Page(self.driver)
    #             print("Rules Created")
    #             window_after = self.driver.window_handles[1]
    #             self.driver.switch_to.window(window_after)
    #             self.Adm_Log = Admin_Login_Page(self.driver)
    #             print("Admin Login Pass")
    #             window_after = self.driver.window_handles[2]
    #             self.driver.switch_to.window(window_after)
    #             self.CB = Cookie_Banner(self.driver)
    #             self.CB.Click_CookieSetting()
    #             print("Tc_005_Pass")
    #             self.driver.quit()
