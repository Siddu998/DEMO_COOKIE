import pytest
from Pages.CPP import CookiPolicyPage_Validation



def CP_page_validation(setup):
    
    driver = setup

    CP = CookiPolicyPage_Validation(driver)
    CP.Validate_CP_Text()
    CP.Validate_WAC_Text()
    CP.Validate_WDWUC_Text()
    CP.Validate_LOC_Text()
    CP.Validate_SN_Cookies_Text()
    CP.Validate_PR_Cookies_Text()
    CP.Validate_PRE_Cookies_Text()
    CP.Validate_TR_Cookies_Text()
    CP.Validate_AN_Cookies_Text()
    CP.Validate_hyperlinks()