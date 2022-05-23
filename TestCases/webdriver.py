
import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# Chrome driver
#path = r"C:\Users\nagarajud-c\Desktop\Demo_Cookie\chromedriver.exe"
#driver = webdriver.Chrome(path)

#options = webdriver.ChromeOptions()




#URL:
importrule = "https://app.requestly.io/rules/#sharedList/1641928973304-My-rules"
URL= "https://zus2q1-myhladmin.myherbalife.com/DistributorRelations/MyHLUtils.aspx"
Re_Rule = "https://app.requestly.io/en-us/extension-installed"
requestly_url = "https://app.requestly.io/rules/my-rules"
Local_URL = "https://zus2q1.myherbalife.com/it-IT/Home/Default/Ds"
Cookie_policy_url = "https://www.myherbalife.com/it-IT/ed/ds/pages/public/politica-sui-cookie.html"

#Rules Locaters:
_imp_rul = "//span[.='Import to My Rules']"
Skip_Demo = "//span[.='Skip']"
_rules_signin = "//span[.='Sign in']"
_redirect = "//a[contains(.,'Redirect a URL')]"
_Ungrouped_Locater = "[name='name']"
_Contains_Locater = "[placeholder='e.g. facebook']"
_Redirect_Locater = "[placeholder='e.g. http://www.new-example.com']"
_ClickSave_Locater = ".ant-btn-primary"
_SaveRules_Locater = "//span[.='Save Rule']"
#Rules SendKeys:
_Ungrouped_Keys = "MyHerbalife" 
_Contains_Keys = "satelliteLib-12930be22558042bc632cff190e4776deb189a2a.js"
_Redirect_Keys = "https://assets.adobedtm.com/78ef23cd3941/4d66435cf9ad/launch-6c390220da59-development.min.js"

#Cookie Banner Locaters
_Cookie_setting = "//button[@id='onetrust-pc-btn-handler']"
_cookie_policy = "//a[.='Ulteriori informazioni']"
_Reject_Cookie = ".onetrust-close-btn-ui"
_accept_cookie_button = "//button[@id='onetrust-accept-btn-handler']"

#Preference Locaters
_performance_cookie = "[for='ot-group-id-C0008']"
_policy_text = "//p[@id='onetrust-policy-text']"
_target_cookie = "[for='ot-group-id-C0004']"
_preference_cookie = "[for='ot-group-id-C0007']"
_analitic_cookie = "[for='ot-group-id-C0002']"
_Preference_Center = "//div[@id='ot-pc-desc']"
_Confirm_mychoice = "//button[@class='save-preference-btn-handler onetrust-close-btn-handler']"
_Accept_All = "//button[@id='accept-recommended-btn-handler']"

#Admin Locaters
Member_id = "[type='text']"
Select_Local = "ctl00_Main_myBox_ddlLocaleSelector"
Click_Login = "ctl00_Main_myBox_doLogIn"

#Admin Inputs
memberid = "staff"
local = "Italy - Italiano"

#Project selection Locaters
_Project = "#projectID"
_UserName = "#userNamePrj"
_ContinueButton = "//button[@class='button']"

#Project Selection Inputs
_ProjectName = "101592 PCX Implementation (Global Segmentation)"
_User = "Nagaraju"
_chromepath = r"C:\Users\nagarajud-c\Desktop\Demo_Cookie\Requestly--Modify-Headers--Mock-API--Redirect.crx"
_rulepath = r"C:\Users\nagarajud-c\Desktop\Demo_Cookie\chromedriver.exe"

executable_path = _rulepath
os.environ["webdriver.chrome.driver"] = executable_path
chrome_options = Options()
chrome_options.add_extension(_chromepath)

driver = webdriver.Chrome(executable_path = executable_path, chrome_options = chrome_options)
driver.maximize_window()


def webpage():
    driver.get(URL)
    time.sleep(3)
    driver.execute_script("window.open('https://app.requestly.io/rules/#sharedList/1641928973304-My-rules','new window')")
    allTabs = driver.window_handles
    print (allTabs)
def test_RulesSetup():
    allTabs = driver.window_handles
    for tab in allTabs:
        driver.switch_to.window(tab)
        if(driver.current_url== importrule):
            RI = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, _imp_rul)))
            RI.click()
            print("Rules Created")

def test_AdminLogin():
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    Admin = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, Member_id)))
    Admin.send_keys(memberid, Keys.ENTER)

    local_Selection = Select(driver.find_element_by_id(Select_Local))
    for opt in local_Selection.options:
        local_Selection.select_by_visible_text(local)

    login_button = driver.find_element_by_id(Click_Login)
    login_button.click()
    window_after = driver.window_handles[3]
    driver.switch_to.window(window_after)

    print("Admin Login Complete")

def test_CookieBanner():
    window_after = driver.window_handles[3]
    driver.switch_to.window(window_after)
    cookie_names_captured = []
    cookie_banner = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, _policy_text)))
    if cookie_banner.is_displayed():
        print('cookies banner text---\n',cookie_banner.text)
    else:
        print("Cookie Banner not found")

    #Cookie_setting
    Cookie_setting = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, _Cookie_setting)))
    driver.execute_script("arguments[0].click();", Cookie_setting)
    if Cookie_setting.is_displayed():
        print("Window found and clicked on the Cookie Setting button")
    else:
        print("Cookie Setting Button not found")

    #Privacy Preference Center text
    Preference_Center = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, _Preference_Center)))
    print('Preference text---\n',Preference_Center.text)

    #Analitic Cookie
    Analitic_cookie = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, _analitic_cookie)))
    driver.execute_script("arguments[0].click();", Analitic_cookie)

    #Preference Cookie
    Preference_cookie = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, _preference_cookie)))
    driver.execute_script("arguments[0].click();", Preference_cookie)

    #Targetting Cookie
    Targetting_cookie = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, _target_cookie)))
    driver.execute_script("arguments[0].click();", Targetting_cookie)

    #Performance Cookie
    Performance_cookie = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, _performance_cookie)))
    driver.execute_script("arguments[0].click();", Performance_cookie)

    time.sleep(3)

    #Confirm my Choice
    Confirm_mychoice = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, _Confirm_mychoice)))
    driver.execute_script("arguments[0].click();", Confirm_mychoice)
    print("clicked on the Confirm my Choice")

    #Choose Project
    Project_Selection = Select(driver.find_element_by_css_selector(_Project))
    for opt in Project_Selection.options:
        Project_Selection.select_by_visible_text(_ProjectName)
    
    #Choose User name
    driver.find_element_by_css_selector(_UserName).send_keys(_User)
    

    #Click Continue button

    ContinueButton = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, _ContinueButton)))
    driver.execute_script("arguments[0].click();", ContinueButton)



    time.sleep(3)
    cookies = driver.get_cookies()
    print(len(cookies))
    print("cookies list :- \n", cookies)
    print(cookies)


    for i in cookies:
        # print(i['name'])
        cookie_names_captured.append(i['name'])


        #Accept All Cookies from Cookie Setting
        #Accept_All = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, _Accept_All)))
        #driver.execute_script("arguments[0].click();", Accept_All)


        #cookie_policy
        #performance_cookie = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, _performance_cookie)))
        #driver.execute_script("arguments[0].click();", performance_cookie)

webpage()
test_RulesSetup()
test_AdminLogin()
test_CookieBanner()
            


