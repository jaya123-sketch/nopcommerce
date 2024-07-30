import time
import pytest
from PageObjects.LoginPage import Login
from PageObjects.Addcustomerpage import AddCustomer
from PageObjects.SearchCustomerPage import searchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_searchCustomerByEmail_004:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("************* searchCustomerByEmail_004************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*********** Login successful**************")

        self.logger.info("************ starting search customer by Email*************")

        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickOnCustomersMenu()
        self.addcust.ClickOnCustomersMenuItem()

        self.logger.info("************ searching customer by Email***************")
        searchcust=searchCustomer(self.driver)
        searchcust.setEmail("james_pan@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        Status=searchcust.searchCustomerByEmail("james_pan@nopCommerce.com")
        assert True
        self.logger.info("************ TC_SearchCustomerByEmail_004 finished***************")

