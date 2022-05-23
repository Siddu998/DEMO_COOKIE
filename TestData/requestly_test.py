# import time
# from TestCases.AdminPage import Admin_Login_Page
# from TestCases.RulesPage import Rules_Setup_Page
# from PageObject.CookieBanner import Cookie_Banner
# import pytest

# baseURL = "https://zus2prs-myhladmin.myherbalife.com/DistributorRelations/MyHLUtils.aspx"
# requestly_url = "https://app.requestly.io/rules/my-rules"
# Local_URL = "https://zus2prs.myherbalife.com/it-IT/Home/Default/Ds"
# memberid = "staff"
# local = "Italy - Italiano"
# RuleName = "MYHL_Test"
# Containt = "satelliteLib-12930be22558042bc632cff190e4776deb189a2a.js"
# Redirect = "https://assets.adobedtm.com/78ef23cd3941/4d66435cf9ad/launch-6c390220da59-development.min.js"
# CurrentURL = "https://zus2prs-myhladmin.myherbalife.com/DistributorRelations/MyHLUtils.aspx"


# def test_homePageTitle(setup):  
#     driver = setup
#     allTabs = driver.window_handles
#     print (allTabs)
#     for tab in allTabs:
#             driver.switch_to.window(tab)
#     if (driver.current_url == Local_URL):
#                 self.CB = Cookie_Banner(self.driver)
#                 self.CB.Validate_Banner_Text()
#                 time.sleep(5)
#                 self.CB.Click_CookieSetting()
#                 self.PC = Preference_Center(self.driver)
#                 self.PC.Validate_Strictly_Text()
#                 self.PC.Validate_Analitic_Text()
#                 self.PC.Validate_Targeting_Text()
#                 self.PC.Validate_Preference_Text()
#                 self.PC.Validate_Performance_Text()
#                 time.sleep(5)
#                 self.driver.quit()

# from webdriver import *

# webpage()
# test_RulesSetup()
# driver.quit()