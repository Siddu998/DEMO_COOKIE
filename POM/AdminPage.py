import pytest
from Pages.AdminLogin import Admin



memberid = "staff"
local = "Italy - Italiano"



def Admin_Login_Page(setup):

    driver = setup

    lp = Admin(driver)
    lp.setmemberid(memberid)
    lp.selectlocal(local)
    lp.clicklogin()

