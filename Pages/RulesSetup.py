from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Rules_Setup:

    _imp_rul = "//span[.='Import to My Rules']"



    def __init__(self,driver):
        self.driver = driver
    
    def RUL_SET(self):
        RI = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._imp_rul)))
        RI.click()