from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Cookie_Banner:
    _CookieSetting_Text = "Impostazioni cookie"
    _AcceptButton_Text = "Accetta cookie"
    _Moreinfo_Link_Text = "Altre informazioni sono disponibili qui." 
    Banner_Text = """La chiusura di questa casella con l’apposito comando contrassegnato con la “X” prima di effettuare una selezione consentirà solo i cookie essenziali, che vengono utilizzati esclusivamente per consentire il funzionamento di questo sito Web. Tuttavia, con il tuo consenso, questo sito utilizza i cookie, inclusi i cookie di terzi, per raccogliere informazioni statistiche, misurare le prestazioni del sito, ricordare le preferenze dell'utente, personalizzare i contenuti pubblicitari (inclusa la profilazione) e consentire l'interazione con i social network. Se vuoi accettare l'utilizzo dei tali cookie clicca sull’apposito comando “accetta cookie”, oppure puoi modificare quelli che desideri consentire accedendo alle impostazioni dei cookie. Puoi modificare le tue preferenze anche in un secondo momento visitando il nostro centro di preferenze sui cookie, come descritto nella nostra 'Politica sui cookie'.Altre informazioni sono disponibili qui."""
    policy_Text = "//p[@id='onetrust-policy-text']"
    Accept_All = "//button[@id='onetrust-accept-btn-handler']"
    Reject_All = ".onetrust-close-btn-ui"
    Cookie_Setting = "//button[@id='onetrust-pc-btn-handler']"
    More_Information_link = "[aria-label='Maggiori informazioni sulla tua privacy']"
    Confirm_Mychoice = "//button[@class='save-preference-btn-handler onetrust-close-btn-handler']"
    _Preference_Center = "//div[@id='ot-pc-desc']"

    def __init__(self,driver):
        self.driver = driver

    #Button Validation

    def Validate_Banner_Text(self):
        CB_Text = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.policy_Text))).text
        
        if (CB_Text == self.Banner_Text):
            # print('Cookie Banner Match---\n',CB_Text)
            result = 'TC_002_CBT - pass'
            return result
        else:
            # print('Cookie Banner MisMatch')
            result = 'TC_002_CBT - fail'
            print('result = ', result)
            return result
            

    def Validate_AcceptAll(self):
        validateAccept_BT =  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Accept_All)))
        if (validateAccept_BT.text == self._AcceptButton_Text):
            print('Accept Cookie Button displayed---\n',validateAccept_BT.text)
        else:
            print("Cookie Accept Button not found")

    def Validate_Cookie_SettingButton(self):
        Validate_CS_BT =  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Cookie_Setting)))
        if (Validate_CS_BT.text == self._CookieSetting_Text):
            print('Cookie Setting Button displayed---\n',Validate_CS_BT.text)
        else:
            print("Cookie Setting Button not found")
        
    def Validate_MoreInformation_link(self):
        MoreInfo_Link = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.More_Information_link)))
        if (MoreInfo_Link.text == self._Moreinfo_Link_Text):
            print('More Info link displayed---\n',MoreInfo_Link.text)
        else:
            print("More Info link not found") 


    #Click Buttons

    def Click_AcceptAll(self):
        Accept_BT =  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Accept_All)))
        if (Accept_BT.text == self._AcceptButton_Text):
            print('Accept Cookie Button displayed---\n',Accept_BT.text)
            Accept_BT.click()
        else:
            print("Cookie Accept Button not found")
    def Click_RejectAll(self):
        Reject_BT = self.driver.find_element_by_css_selector(self.Reject_All)
        if Reject_BT.is_displayed():
            print("Window found and clicked on the Cookie Reject button")
            Reject_BT.click()
            print("Tc_003 Pass")
        else:
            print("Cookie Reject Button not found")

    def Click_CookieSetting(self):
        Cookie_Set_BT = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,  self.Cookie_Setting)))
        if (Cookie_Set_BT.text == self._CookieSetting_Text):
            print('Window found and clicked on the Cookie Setting button---\n',Cookie_Set_BT.text)
            Cookie_Set_BT.click()
            print("TC_002 Pass")
        else:
            print("Cookie Setting Button not found")
        
    def Click_Confirm_mychoice(self):
        Confirm_Choice_BT = self.driver.find_element_by_xpath(self.Confirm_Mychoice)
        Confirm_Choice_BT.click()

    def Prf_Center (self):
        Preference_Center = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._Preference_Center)))
        if Preference_Center.is_displayed():
            print('Preference banner text---\n',Preference_Center.text)
        else:
            print("Preference Banner not found")

    def Click_MoreInformation_link(self):
        MoreInfo = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.More_Information_link)))
        if (MoreInfo.text == self._Moreinfo_Link_Text):
            print('Window found and clicked on More Info link------\n',MoreInfo.text)
            MoreInfo.click()
        else:
            print("More Info link not found")
 

    