import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import ElementNotInteractableException

class ExportCustomer:
    btn_ExportCustomer_linktxt_xpath="/html/body/div[3]/div[1]/form[1]/div/div/div/button[2]"
    Exporttoxml1_xpath="//*[@name='exportxml-all']"
    Exporttoxml2_xpath="//*[@id='exportxml-selected']"
    Exporttoexcel1_xpath="//*[@name='exportexcel-all']"
    Exporttoexcel2_xpath="//*[@id='exportexcel-selected']"

    def __init__(self,driver):
        self.driver=driver

    def click_AddExport(self):
        self.driver.find_element(By.XPATH,self.btn_ExportCustomer_linktxt_xpath).click()


    #def Exporttoxml1(self,CustomerId):
        self.driver.find_element(By.XPATH,self.Exporttoxml1_xpath).click()

    def Exporttoxml2(self,CustomerId):
        self.driver.find_element(By.XPATH,self.Exporttoxml2_xpath).click()

    #def ExporttoExcel1(self):
        #self.driver.find_element(By.XPATH,self.Exporttoexcel1_xpath).click()

    #def ExporttoExcel2(self):
        #self.driver.find_element(By.XPATH,self.Exporttoexcel2_xpath).click()


