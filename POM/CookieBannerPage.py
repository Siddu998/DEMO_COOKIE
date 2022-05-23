import pytest
from Pages.CookieBanner import Cookie_Banner
import time






def Banner_Validation(setup):
    
    driver = setup

    CK = Cookie_Banner(driver)
    CK.Validate_Banner_Text()
    CK.Click_RejectAll()
    
    #CK.Validate_AllButtons()