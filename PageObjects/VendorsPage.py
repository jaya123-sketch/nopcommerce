import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Vendors:
     link_Vendors_menu_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[4]/a/p"
     link_AddNew_btn_xpath="/html/body/div[3]/div[1]/div/div/a"
     txtbox_Vendorname_xpath="//input[@name='Name']"
     txtbox_Vendoremail_xpath="//input[@id='Email']"
     btn_active_xpath="//input[@id='Active']"
     btn_Save_xpath="//button[@name='save']"

     def __init__(self,driver):
          self.driver = driver

     def ClickOnVendorsMenu(self):
          self.driver.find_element(By.XPATH,self.link_Vendors_menu_xpath).click()

     def ClickOnAddNew(self):
          self.driver.find_element(By.XPATH,self.link_AddNew_btn_xpath).click()

     def SetVendorname(self,vendorname):
          self.driver.find_element(By.XPATH,self.txtbox_Vendorname_xpath).send_keys(vendorname)

     def SetVendoremail(self,vendoremail):
          self.driver.find_element(By.XPATH,self.txtbox_Vendoremail_xpath).send_keys(vendoremail)


     def Clickonactive(self,value):
          self.driver.find_element(By.XPATH,self.btn_active_xpath).send_keys(value)

     def ClickOnSave(self):
          self.driver.find_element(By.XPATH,self.btn_Save_xpath).click()