import pytest
import time
from POM.AdminPage import Admin_Login_Page
from POM.RulesPage import Rules_Setup_Page
from Pages.CookieBanner import Cookie_Banner
from POM.CPpage import CP_page_validation



class Test_DS_login:

    CP_URL = "https://www.myherbalife.com/it-IT/ed/ds/pages/public/politica-sui-cookie.html"
    Re_Rule = "https://app.requestly.io/rules/#sharedList/1641928973304-My-rules"
    Local_URL = "https://zus2prs.myherbalife.com/it-IT/Home/Default/Ds"


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
                self.CB = Cookie_Banner(self.driver)
                cbt = self.CB.Validate_Banner_Text()
                print('cbt', cbt)
                self.CB.Validate_AcceptAll()
                self.CB.Validate_Cookie_SettingButton()
                self.CB.Validate_MoreInformation_link()
                self.CB.Click_MoreInformation_link()
                window_after = self.driver.window_handles[3]
                self.driver.switch_to.window(window_after)
                if(self.driver.current_url == self.CP_URL):
                    print("TC_002 Pass---\n",self.driver.current_url)
                else:
                    print("TC_002 Fail")
                self.CB = Cookie_Banner(self.driver)
                self.CB.Validate_Banner_Text()
                self.CB.Validate_AcceptAll()
                self.CB.Validate_Cookie_SettingButton()
                self.CB.Validate_MoreInformation_link()
                self.CB.Click_AcceptAll()
                self.CP_Pag = CP_page_validation(self.driver)
                time.sleep(5)
                self.driver.quit()
                
                
                


                
                
                
                



