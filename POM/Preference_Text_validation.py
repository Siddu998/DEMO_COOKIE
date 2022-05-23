import pytest
from Pages.PreferenceCenter import Preference_Center
import time






def Pref_Text_validation(setup):
    
    driver = setup

    PC = Preference_Center(driver)
    PC.Validate_Strictly_Text()
    PC.Validate_Analitic_Text()
    PC.Validate_Targeting_Text()
    PC.Validate_Preference_Text()
    PC.Validate_Preference_Text()
    