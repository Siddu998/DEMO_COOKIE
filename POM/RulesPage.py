import pytest
from Pages.RulesSetup import Rules_Setup
import time



RuleName = "MYHL_Test"
Containt = "satelliteLib-12930be22558042bc632cff190e4776deb189a2a.js"
Redirect = "https://assets.adobedtm.com/78ef23cd3941/4d66435cf9ad/launch-6c390220da59-development.min.js"


def Rules_Setup_Page(setup):
    driver = setup

    RL = Rules_Setup(driver)
    RL.RUL_SET()

    