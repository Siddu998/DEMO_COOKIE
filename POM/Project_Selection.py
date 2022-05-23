import pytest
from Pages.ProjectSelection import ProjectSelection_Validation



def CP_page_validation(setup):
    
    driver = setup

    PS = ProjectSelection_Validation(driver)
    PS.Project_Validation()
    PS.UserName_Validation()
    PS.Cilck_Continue()
    PS.validate_CPP_Footerlink()
    PS.validate_PPP_Footerlink()
    PS.Click_CPP_Footerlink()
    PS.Click_PPP_Footerlink()