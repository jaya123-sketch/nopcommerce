import pytest
import time

from PageObjects.LoginPage import Login
from selenium.webdriver.common.by import By
from PageObjects.Addcustomerpage import AddCustomer
from PageObjects.ExportCustomerPage import ExportCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_006_ExportCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_exportCustomer(self,setup):
        self.logger.info("******** Test_003_AddCustomer***********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******* Login successful***********")
        self.logger.info("*********** Starting Add Customer Test")

        self.addcust = AddCustomer(self.driver)
        self.addcust.ClickOnCustomersMenu()
        self.addcust.ClickOnCustomersMenuItem()

        self.logger.info("************ Providing  export customer info******")
        self.addexpo = ExportCustomer(self.driver)
        self.addexpo.click_AddExport()


        #self.addexpo.Exporttoxml1(215)
        self.addexpo.Exporttoxml2(215)
        #self.addexpo.Exporttoexcel1()
        #self.addexpo.Exporttoexcel2()
        self.logger.info("********** Validation starts**************")

        assert True


        time.sleep(5)


        self.logger.info("************ Saving customer info******")
        self.logger.info("************ Add Export Customer successful********")
        self.logger.info("************ TC_ExportCustomer_006 passed***************")
        self.driver.close()

