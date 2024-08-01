import time
import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from PageObjects.LoginPage import Login
from PageObjects.VendorsPage import Vendors
from PageObjects.Addcustomerpage import AddCustomer
from PageObjects.ExportCustomerPage import ExportCustomer
from PageObjects.SearchCustomerPage import searchCustomer

class Test_007_AddVendors:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    def test_AddVendor(self,setup):
        self.logger.info("******** Test_007_AddVendor***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******* Login successful***********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.ClickOnCustomersMenu()
        self.addcust.ClickOnCustomersMenuItem()


        self.logger.info("*********** Starting Add Vendor Test")

        self.addven=Vendors(self.driver)
        self.addven.ClickOnVendorsMenu()
        self.addven.ClickOnAddNew()
        self.addven.SetVendorname("Vendor1")
        self.addven.SetVendoremail("Vendor1@gmail.com")
        self.addven.Clickonactive("true")
        self.addven.ClickOnSave()

        self.logger.info("************ Saving customer info******")

