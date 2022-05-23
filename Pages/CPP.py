
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest



class CookiPolicyPage_Validation:


    #Locator:
    CPP_BodyText = ".myhl3"

    #Name Validation locators
    _CCPTextValidation = ".aem-Grid--default--10 h1"   #CSS
    _what_are_cookie = ".aem-Grid--default--10 > div:nth-of-type(2) p:nth-of-type(1) > b"    #CSS
    _what_are_cookie_text1 = "//p[contains(.,'I cookie,')]"    #Xpath
    _what_are_cookie_text2 = ".aem-Grid--default--10 > div:nth-of-type(2) p:nth-of-type(3)"    #CSS

    _why_do_we_use_cookies = ".aem-Grid--default--10 p:nth-of-type(5) > b"    #CSS
    _why_do_we_use_cookies_text = ".aem-Grid--default--10 > div:nth-of-type(2) p:nth-of-type(6)"    #CSS

    _list_of_cookies_title = "//h3[@id='cookie-policy-title']"   #Xpath
    _list_of_cookies_text = "#cookie-policy-description"        #CSS

    _SrrictlyNecessaryCookies_title = "//section[1]/h4[@class]"  #Xpath
    _SrrictlyNecessaryCookies_text = "//section[1]/p[@class]"    #Xpath
    _SrrictlyNecessaryCookies_table = "//section[1]/table"       #Xpath

    _PerformaceCookies_title = "//section[2]/h4[@class]"   #Xpath
    _PerformaceCookies_text = "//section[2]/p[@class='ot-sdk-cookie-policy-group-desc']"    #Xpath
    _PerformaceCookies_table = "//section[2]/table"        #Xpath

    _targettingCookie_title = "//section[3]/h4[@class]"    #Xpath
    _targettingCookie_text = "//section[3]/p[@class]"      #Xpath
    _targettingCookie_table = "//section[3]/table"         #Xpath

    _PreferenceCookie_title = "//section[4]/h4[@class]"    #Xpath
    _PreferenceCookie_text = "//section[4]/p[@class]"      #Xpath
    _PreferenceCookie_table = "//section[4]/table"         #Xpath

    _AnalaticCookie_title = "//section[5]/h4[@class]"      #Xpath
    _AnalaticCookies_text = "//section[5]/p[@class]"       #Xpath
    _AnalaticCookies_table = "//section[5]/table"          #Xpath

    _Disable_Enable_Cookies_hyperlink = "//a[.='Impostazioni cookie.']"    #Xpath
    _Disable_Enable_Cookies_text = ".aem-Grid--default--10 p:nth-of-type(4) > font"   #CSS
    _yourChoice_hyperlink = "//a[.='www.youronlinechoices.eu/it/']"  #Xpat
    _Web_hyperlink = "//ul[contains(.,'Impostazioni cookie in Internet Explorer          Impostazioni cookie in Firefox')]" #Xpath



    #Text Validation

    CCPTextValidation = "Politica sui cookie"
    what_are_cookie = "Cosa sono i cookie?"
    what_are_cookie_text1 = """I cookie, i pixel e altre tecnologie di tracciamento (collettivamente, i @@cookie@@) sono una stringa di dati di solo testo che un sito Web trasferisce al file dei cookie del browser situato sul disco rigido del computer dell'utente e che consente al sito di riconoscerlo. I cookie possono aiutare un sito ad adattare i contenuti agli interessi principali dell'utente. Alcuni cookie ci consentono di ricreare e riprodurre le sessioni degli utenti sui nostri Siti. Quasi tutti i siti di grandi dimensioni utilizzano i cookie."""
    what_are_cookie_text2 = """Di solito, un cookie contiene il nome del dominio da cui proviene, la @@durata@@ del cookie stesso e un valore, quasi sempre un numero univoco generato casualmente."""
    why_do_we_use_cookies = "Perché utilizziamo i cookie?"
    why_do_we_use_cookies_text1 = "Herbalife utilizza i cookie per raccogliere informazioni statistiche, misurare le prestazioni del sito, ricordare le preferenze dell'utente, personalizzare i contenuti pubblicitari (inclusa la profilazione) e consentire l'interazione con i social network.  Anche terze parti possono utilizzare i cookie tramite i Siti al fine di facilitare il conseguimento degli scopi sopra elencati o per i propri scopi, come specificato nella tabella. I tipi di cookie utilizzati sono:"

    list_of_cookies_title = "Elenco dei cookie"
    list_of_cookies_text = "Un cookie è una piccola porzione di dati (file di testo) che un sito Web, se visitato da un utente, chiede al browser di memorizzarlo sul dispositivo per ricordare le sue informazioni, quali la lingua preferita o i dati di accesso. Questi cookie sono da noi impostati e denominati cookie di prima parte. Utilizziamo inoltre cookie di terza parte - ovvero i cookie di un dominio diverso da quello del sito Web che si sta visitando - per i nostri tentativi pubblicitari e di marketing. In particolare, utilizziamo i cookie e altre tecnologie di tracciamento per i seguenti scopi:"

    SrrictlyNecessaryCookies_title = "Cookie strettamente necessari"
    SrrictlyNecessaryCookies_text = "Questi cookie sono necessari necessari ai fini della funzionalità, della sicurezza e della conformità dei nostri Siti. Non è possibile disattivare tali cookie nel centro preferenze."
    SrrictlyNecessaryCookies_table = ""

    PerformaceCookies_title = "Cookie di performance"
    PerformaceCookies_text = "Sono utilizzati per le seguenti finalità: aiutarci a instradare il traffico tra i vari server; conoscere la rapidità con cui gli utenti caricano le funzioni; identificare e risolvere problemi di esperienza dell’utente e migliorare le operazioni del sito Web; rispondere alle richieste di informazioni dei membri e contribuire ad assicurare la conformità alle regole dei nostri membri; conteggiare il numero di utenti del nostro sito."
    PerformaceCookies_table = ""

    targettingCookie_title = "Cookie di target e a fini pubblicitari"
    targettingCookie_text = "Sono utilizzati per le seguenti finalità: permetterci di adattare contenuti o pubblicità ai tuoi interessi, alla geolocalizzazione o impedire che ti vengano presentati sempre gli stessi annunci; contribuire a valutare l’efficacia delle campagne di marketing; comprendere più a fondo come le persone utilizzano i nostri prodotti."
    targettingCookie_table = ""

    PreferenceCookie_title = "Cookie di preferenza"
    PreferenceCookie_text = "Sono utilizzati per le seguenti finalità: consentire al sito Web di fornire una maggiore funzionalità e personalità; permettere ai Siti di ricordare informazioni che modificano il modo di comportarsi e l’aspetto del sito; trasferire informazioni tra una pagina e l’altra ed evitare la necessità di inserire di nuovo le informazioni; consentirti di accedere a informazioni memorizzate all’interno della sessione."
    PreferenceCookie_table = ""

    AnalaticCookie_title = "Cookie analitici"
    AnalaticCookies_text = "Sono utilizzati per le seguenti finalità: compilare statistiche aggregate che ci consentono di migliorare la aiutarci a comprendere meglio come le persone interagiscano con le proprietà del sito Web e delle applicazioni; aiutarci a determinare quali annunci di prodotto risultino più rilevanti."
    AnalaticCookies_table = ""


    YourChoice_text = "www.youronlinechoices.eu/it/"
    Disable_Enable_Cookies_text = "Inoltre, hai la possibilità di accettare o rifiutare cookie modificando le impostazioni del tuo browser. Tuttavia, disabilitando determinati cookie, forse non potrai utilizzare tutte le componenti interattive del nostro sito. Se desideri essere avvertito/a prima che un cookie sia memorizzato sul tuo hard disk, ecco cosa devi fare:"
    Disable_Enable_Cookies_hyperlink_text = "Impostazioni cookie."



    def __init__(self,driver):
        self.driver = driver

    #Text and hyperlink Validation

    def Validate_CP_Text(self):
        CP_Text = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._CCPTextValidation))).text
        print(CP_Text)
        
        if (CP_Text == self.CCPTextValidation):
            result = 'TC_004_01_CPT - pass'
            return result
        else:
            result = 'TC_004_01_CPT - fail'
            print('result = ', result)
            return result
    def Validate_WAC_Text(self):
        what_are_cookie_Text = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._what_are_cookie))).text
        if (what_are_cookie_Text == self.what_are_cookie):
            result = 'TC_004_02_CPT - pass'
            print('result = ', result)
        else:
            result = 'TC_004_02_CPT - fail'
            print('result = ', result)
            

        what_are_cookie_Text1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._what_are_cookie_text1))).text
        print('what_are_cookie_Text1--\n',what_are_cookie_Text1)
        print('replace text--\n',what_are_cookie_Text1.replace('"','@@'))
        print('expectedtext--\n',self.what_are_cookie_text1)
        compare_text1_result = []

        for i, row in enumerate(what_are_cookie_Text1.replace('"','@@')):
            for j , value in enumerate(self.what_are_cookie_text1):
                if i == j and row != value:
                    compare_text1_result.append(row)
                else:
                    result = 'TC_004_03_CPT - Pass'
        if len(compare_text1_result) !=0:
            result = 'TC_004_03_CPT - fail'
            print('result = ', result) 
        if len(compare_text1_result) ==0:
            result = 'TC_004_03_CPT - Pass'
            print('result = ', result)
        
        what_are_cookie_Text2 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._what_are_cookie_text2))).text
        print('what_are_cookie_Text1--\n',what_are_cookie_Text2)
        print('replace text--\n',what_are_cookie_Text2.replace('"','@@'))
        print('expectedtext--\n',self.what_are_cookie_text2)
        compare_text2_result = []

        for i, row in enumerate(what_are_cookie_Text2.replace('"','@@')):
            for j , value in enumerate(self.what_are_cookie_text2):
                if i == j and row != value:
                    compare_text2_result.append(row)
                else:
                    result = 'TC_004_04_CPT - Pass'
        if len(compare_text2_result) !=0:
            result = 'TC_004_04_CPT - fail'
            print('result = ', result) 
        if len(compare_text2_result) ==0:
            result = 'TC_004_04_CPT - Pass'
            print('result = ', result)
            
    def Validate_WDWUC_Text(self):
        why_we_use_cookies_text = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._why_do_we_use_cookies))).text

        print(why_we_use_cookies_text)
        

        if (why_we_use_cookies_text == self.why_do_we_use_cookies):
            result = 'TC_004_05_CPT - pass'
            print('result = ', result)
            
        else:
            result = 'TC_004_05_CPT - fail'
            print('result = ', result)
            return result

        why_we_use_cookies_text1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._why_do_we_use_cookies_text))).text

        if (why_we_use_cookies_text1 == self.why_do_we_use_cookies_text1):
            result = 'TC_004_06_CPT - pass'
            print('result = ', result)
        else:
            result = 'TC_004_06_CPT - fail'
            print('result = ', result)
            return result

            
    def Validate_LOC_Text(self):
        LOC_Text = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._list_of_cookies_title))).text
        
        if (LOC_Text == self.list_of_cookies_title):
            result = 'TC_004_07_CPT - pass'
            print('result = ', result)
        else:
            result = 'TC_004_07_CPT - fail'
            print('result = ', result)
            return result
        LOC_Text1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._list_of_cookies_text))).text
        
        if (LOC_Text1 == self.list_of_cookies_text):
            result = 'TC_004_08_CPT - pass'
            print('result = ', result)
        else:
            result = 'TC_004_08_CPT - fail'
            print('result = ', result)
            return result
            

    def Validate_SN_Cookies_Text(self):
        SN_title = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._SrrictlyNecessaryCookies_title))).text
        
        if (SN_title == self.SrrictlyNecessaryCookies_title):
            result = 'TC_004_09_CPT - pass'
            print('result = ', result)
        else:
            result = 'TC_004_09_CBT - fail'
            print('result = ', result)
            return result
        SN_Text = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._SrrictlyNecessaryCookies_text))).text

        print(SN_Text)

        if (SN_Text == self.SrrictlyNecessaryCookies_text):
            result = 'TC_004_10_CPT - pass'
            print('result = ', result)
        else:
            result = 'TC_004_10_CBT - fail'
            print('result = ', result)
            return result

    def Validate_PR_Cookies_Text(self):
        PR_title = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._PerformaceCookies_title))).text
        
        
        if (PR_title == self.PerformaceCookies_title):
            result = 'TC_004_11_CPT - pass'
            print('result = ', result)
        else:
            result = 'TC_004_11_CBT - fail'
            print('result = ', result)
            return result
        PR_Text = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._PerformaceCookies_text))).text

        print(PR_Text)

        if (PR_Text == self.PerformaceCookies_text):
            result = 'TC_004_12_CPT - pass'
            print('result = ', result)
        else:
            result = 'TC_004_12_CBT - fail'
            print('result = ', result)
            return result    
    def Validate_PRE_Cookies_Text(self):
        PRE_title = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._PreferenceCookie_title))).text

        print(PRE_title)
        
        if (PRE_title == self.PreferenceCookie_title):
            result = 'TC_004_13_CPT - pass'
            print('result = ', result)
        else:
            result = 'TC_004_13_CBT - fail'
            print('result = ', result)
            
            return result
        PRE_Text = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._PreferenceCookie_text))).text

        if (PRE_Text == self.PreferenceCookie_text):
            result = 'TC_004_14_CPT - pass'
            print('result = ', result)
        else:
            result = 'TC_004_14_CBT - fail'
            print('result = ', result)
            return result
    def Validate_TR_Cookies_Text(self):
        TR_title = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._targettingCookie_title))).text
        
        if (TR_title == self.targettingCookie_title):
            result = 'TC_004_15_CPT - pass'
            print('result = ', result)
        else:
            result = 'TC_004_15_CBT - fail'
            print('result = ', result)
            return result
        TR_Text = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._targettingCookie_text))).text

        if (TR_Text == self.targettingCookie_text):
            result = 'TC_004_16_CPT - pass'
            print('result = ', result)
        else:
            result = 'TC_004_16_CBT - fail'
            print('result = ', result)
            return result   
    def Validate_AN_Cookies_Text(self):
        AN_title = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._AnalaticCookie_title))).text
        
        if (AN_title == self.AnalaticCookie_title):
            result = 'TC_004_17_CPT - pass'
            print('result = ', result)
        else:
            result = 'TC_004_17_CBT - fail'
            print('result = ', result)
            return result
        AN_Text = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._AnalaticCookies_text))).text

        if (AN_Text == self.AnalaticCookies_text):
            result = 'TC_004_18_CPT - pass'
            print('result = ', result)
        else:
            result = 'TC_004_18_CBT - fail'
            print('result = ', result)
            return result 
    def Validate_hyperlinks(self):
        CookieSetting_hyperlink = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._Disable_Enable_Cookies_hyperlink))).text
        
        if (CookieSetting_hyperlink == self.Disable_Enable_Cookies_hyperlink_text):
            result = 'TC_004_18_CPT - pass'
            print('result = ', result)
        else:
            result = 'TC_004_18_CBT - fail'
            print('result = ', result)
            return result

        YourChoice_hyperlink = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._yourChoice_hyperlink))).text
        
        if (YourChoice_hyperlink == self.YourChoice_text):
            result = 'TC_004_19_CPT - pass'
            print('result = ', result)
            print(YourChoice_hyperlink)
        else:
            result = 'TC_004_19_CBT - fail'
            print('result = ', result)
            return result

        Web_hyperlink = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._Web_hyperlink))).text
        print(Web_hyperlink)
        self.driver.quit()
        # if (Web_hyperlink == self.Disable_Enable_Cookies_hyperlink_text):
        #     result = 'TC_004_18_CPT - pass'
        #     print('result = ', result)
        # else:
        #     result = 'TC_004_18_CBT - fail'
        #     print('result = ', result)
        #     return result