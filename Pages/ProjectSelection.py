from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pytest




class ProjectSelection_Validation:


  #Locator:
  Project_ID = "#projectID"   #CSS
  UserName = "#userNamePrj"   #CSS
  ContinueButton = "//button[@class='button']"  #XPATH
  CPP_footerlink = "#main-footer ul:nth-of-type(4) > li:nth-of-type(5)" #CSS
  PPP_footerlink = "#main-footer ul:nth-of-type(4) > li:nth-of-type(4)" #CSS

  #Name Validation locators
  _Project_ID ="101592 PCX Implementation (Global Segmentation)"
  _UserName = "Nagaraju"
  _CPP_footerlink_text = "Politica sui cookie"
  _PPP_footerlink_text = "Informativa sulla privacy"

  def __init__(self,driver):


    self.driver = driver

  #Text and hyperlink Validation

  def Project_Validation(self):

    Project_Selection = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.Project_ID)))
    for opt in Project_Selection.options:
      Project_Selection.select_by_visible_text(self._Project_ID)

  def UserName_Validation(self):
    UserName_Selection = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.UserName)))
    UserName_Selection.send_keys(self._UserName)

  def Cilck_Continue(self):
    Continue_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ContinueButton)))
    Continue_button.click()
  
  def validate_CPP_Footerlink(self):
    CPP_link = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.CPP_footerlink))).text

    if (CPP_link == self._CPP_footerlink_text):
      result = 'TC_005_03 - pass'
      print('result = ', result)
      
    else:
      result = 'TC_005_03 - fail'
      print('result = ', result)
      return result

  def validate_PPP_Footerlink(self):
    PPP_link = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.PPP_footerlink))).text

    if (PPP_link == self._PPP_footerlink_text):
      result = 'TC_005_04 - pass'
      print('result = ', result)
      
    else:
      result = 'TC_005_04 - fail'
      print('result = ', result)
      return result

  def Click_CPP_Footerlink(self):
    CPP_link = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.CPP_footerlink))).text

    if (CPP_link == self._CPP_footerlink_text):
      result = 'TC_005_03 - pass'
      print('result = ', result)
      CPP_link.click()
      
    else:
      result = 'TC_005_03 - fail'
      print('result = ', result)
      return result

  def Click_PPP_Footerlink(self):
    PPP_link = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.PPP_footerlink))).text

    if (PPP_link == self._PPP_footerlink_text):
      result = 'TC_005_04 - pass'
      print('result = ', result)
      PPP_link.click()
      
    else:
      result = 'TC_005_04 - fail'
      print('result = ', result)
      return result
