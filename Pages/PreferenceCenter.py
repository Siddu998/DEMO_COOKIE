from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class Preference_Center:

    More_Information_hyperlink = "//a[.='More information']"
    Allow_All = "//button[@id='accept-recommended-btn-handler']"
    Confirm_Mychoice = "//button[@class='save-preference-btn-handler onetrust-close-btn-handler']"
    _Preference_Center = "//div[@id='ot-pc-desc']"

    #Button Locators
    SBT = "[aria-controls='ot-desc-id-C0001']"
    ABT = "[aria-controls='ot-desc-id-C0002']"
    TBT = "[aria-controls='ot-desc-id-C0004']"
    PEBT= "[aria-controls='ot-desc-id-C0007']"
    PRBT= "[aria-controls='ot-desc-id-C0008']"

    #Button Text Locators
    Strictly_Necessary_Cookies = "[data-optanongroupid='C0001'] .ot-cat-header"
    Analytic_Cookies = "[data-optanongroupid='C0002'] .ot-cat-header"
    Targetting_Cookies = "[data-optanongroupid='C0004'] .ot-cat-header"
    Preference_Cookies = "[data-optanongroupid='C0007'] .ot-cat-header"
    Performance_Cookies = "[data-optanongroupid='C0008'] .ot-cat-header"
    

    #Category text Locaters
    _Strictly_Necessary_locator = "[data-optanongroupid='C0001'] .ot-acc-grpdesc"
    _Analytic_locator = ".ot-accordion-layout[data-optanongroupid='C0002'] .ot-acc-grpdesc"
    _Targetting_locator = ".ot-accordion-layout[data-optanongroupid='C0004'] .ot-acc-grpdesc"
    _Preference_locator = ".ot-accordion-layout[data-optanongroupid='C0007'] > .ot-acc-grpcntr"
    _Performance_locator = ".ot-accordion-layout[data-optanongroupid='C0008'] .ot-acc-grpdesc"


    #Toggle Button
    Analytic_Toggle_Button = "[for='ot-group-id-C0002']"
    Targetting_Toggle_Button = "[for='ot-group-id-C0004']"
    Preference_Toggle_Button = "[for='ot-group-id-C0007']"
    Performance_Toggle_Button = "[for='ot-group-id-C0008']"

    #Button Text
    _Strictly_Necessary = "Cookie strettamente necessari"
    _Analytic = "Cookie analitici"
    _Targetting = "Cookie di target e a fini pubblicitari"
    _Preference = "Cookie di preferenza"
    _Performance = "Cookie di performance"

    #Button Text validation
    _Strictly_Necessary_Text = "Questi cookie sono necessari necessari ai fini della funzionalità, della sicurezza e della conformità dei nostri Siti. Non è possibile disattivare tali cookie nel centro preferenze."
    _Performance_Text = "Sono utilizzati per le seguenti finalità: aiutarci a instradare il traffico tra i vari server; conoscere la rapidità con cui gli utenti caricano le funzioni; identificare e risolvere problemi di esperienza dell’utente e migliorare le operazioni del sito Web; rispondere alle richieste di informazioni dei membri e contribuire ad assicurare la conformità alle regole dei nostri membri; conteggiare il numero di utenti del nostro sito."
    _Targetting_Text = "Sono utilizzati per le seguenti finalità: permetterci di adattare contenuti o pubblicità ai tuoi interessi, alla geolocalizzazione o impedire che ti vengano presentati sempre gli stessi annunci; contribuire a valutare l’efficacia delle campagne di marketing; comprendere più a fondo come le persone utilizzano i nostri prodotti."
    _Preference_Text = "Sono utilizzati per le seguenti finalità: consentire al sito Web di fornire una maggiore funzionalità e personalità; permettere ai Siti di ricordare informazioni che modificano il modo di comportarsi e l’aspetto del sito; trasferire informazioni tra una pagina e l’altra ed evitare la necessità di inserire di nuovo le informazioni; consentirti di accedere a informazioni memorizzate all’interno della sessione."
    _Analytic_Text = "Sono utilizzati per le seguenti finalità: compilare statistiche aggregate che ci consentono di migliorare la aiutarci a comprendere meglio come le persone interagiscano con le proprietà del sito Web e delle applicazioni; aiutarci a determinare quali annunci di prodotto risultino più rilevanti."
    
    

    def __init__(self,driver):
        self.driver = driver

    def Prf_Center (self):
        Preference_Center = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._Preference_Center)))
        print('Preference text---\n',Preference_Center.text)
    

    def Validate_Strictly_Necessary(self):
        Strictly_BT_Text =  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.Strictly_Necessary_Cookies)))
        SN_BT =  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.SBT)))
        if (Strictly_BT_Text.text == self._Strictly_Necessary):
            SN_BT.click()
            print('Button Name Match---\n',Strictly_BT_Text.text)
        else:
            print("Button Mismatch")

        Strictly_Text = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._Strictly_Necessary_locator)))
        if (Strictly_Text.text == self._Strictly_Necessary_Text):
            print('Text Match---\n',Strictly_Text.text)
        else:
            print("Text Mismatch")
       

    def Validate_Analitic(self):
        Analatic_BT_Text = self.driver.find_element(By.CSS_SELECTOR, self.Analytic_Cookies)
        AN_BT = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.ABT)))
        if (Analatic_BT_Text.text == self._Analytic):
            AN_BT.click()
            print('Button Name Match---\n',Analatic_BT_Text.text)
        else:
            print("Button Mismatch")

        Analatic_Text = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._Analytic_locator)))
        if (Analatic_Text.text == self._Analytic_Text):
            print('Text Match---\n',Analatic_Text.text)
        else:
            print("Text Mismatch")
        Analatic_Toggle_BT = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.Analytic_Toggle_Button)))
        Analatic_Toggle_BT.click()
        print("Window found and clicked on the Analatic button")

    def Validate_Targeting(self):
        Targeting_BT_Text = self.driver.find_element(By.CSS_SELECTOR, self.Targetting_Cookies)
        TG_BT = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.TBT)))
        if (Targeting_BT_Text.text == self._Targetting):
            TG_BT.click()
            print('Button Name Match---\n',Targeting_BT_Text.text)
        else:
            print("Button Mismatch")

        Targeting_Text = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._Targetting_locator)))
        if (Targeting_Text.text == self._Targetting_Text):
            print('Text Match---\n',Targeting_Text.text)
        else:
            print("Text Mismatch")
        Targeting_Toggle_BT = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.Targetting_Toggle_Button)))
        Targeting_Toggle_BT.click()
        print("Window found and clicked on the Targeting button")
        

    def Validate_Perference(self):
        preference_BT_Text = self.driver.find_element(By.CSS_SELECTOR, self.Preference_Cookies)
        PE_BT = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.PEBT)))
        if (preference_BT_Text.text == self._Preference):
            PE_BT.click()
            print('Button Name Match---\n',preference_BT_Text.text)
        else:
            print("Button Mismatch")

        Preference_Text = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._Preference_locator)))
        if (Preference_Text.text == self._Preference_Text):
            print('Text Match---\n',Preference_Text.text)
        else:
            print("Text Mismatch")
        Preference_Toggle_BT = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.Preference_Toggle_Button)))
        Preference_Toggle_BT.click()
        print("Window found and clicked on the Preference button")

    def Validate_Performance(self):
        performance_BT_Text = self.driver.find_element(By.CSS_SELECTOR, self.Performance_Cookies)
        PR_BT = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.PRBT)))
        if (performance_BT_Text.text == self._Performance):
            PR_BT.click()
            print('Button Name Match---\n',performance_BT_Text.text)
        else:
            print("Button Mismatch")

        Performance_Text = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._Performance_locator)))
        if (Performance_Text.text == self._Performance_Text):
            print('Text Match---\n',Performance_Text.text)
        else:
            print("Text Mismatch")
        Performance_Toggle_BT = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.Performance_Toggle_Button)))
        Performance_Toggle_BT.click()
        print("Window found and clicked on the Preference button")

    def Click_Confirm_mychoice(self):
        Confirm_Choice = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Confirm_Mychoice)))
        self.driver.execute_script("arguments[0].click();", Confirm_Choice.click())
        print("clicked on the Confirm my Choice")

    def Click_More_Information(self):
        self.driver.find_element_by_xpath(self.More_Information_hyperlink).click()

    def Click_Allow_All(self):
        self.driver.find_element_by_xpath(self.Allow_All).click()

   