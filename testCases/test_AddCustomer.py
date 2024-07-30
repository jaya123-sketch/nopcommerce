import pytest
import time
from PageObjects.LoginPage import Login
from selenium.webdriver.common.by import By
from PageObjects.Addcustomerpage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()
    @pytest.mark.sanity
    @pytest.mark.regession
    def test_addCustomer(self,setup):
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

        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickOnCustomersMenu()
        self.addcust.ClickOnCustomersMenuItem()

        self.addcust.ClickOnAddNew()

        self.logger.info("************ Providing customer info******")
        self.email=random_generator() + "@gmail.com"
        self.addcust.SetEmail(self.email)
        self.addcust.SetPassword("test123")
        self.addcust.SetCustomerRoles("Registered")
        self.addcust.SetManagerOfVendor("Vendor 2")
        self.addcust.SetGender("Male")
        self.addcust.SetFirstName("Jayalakshmi")
        self.addcust.SetLastName("Aravapalli")
        self.addcust.SetDOB("15/09/1990")
        self.addcust.SetCompanyName("busyQA")
        self.addcust.SetAdminComment("This is fo testing...........")
        self.addcust.ClickOnSave()

        self.logger.info("************ Saving customer info******")
        self.logger.info("************ Add Customer validation Started********")
        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True==True
            self.logger.info("************ Add Customer Test Passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer_scr.png")
            self.logger.info("********* Add Customer Test Failed ************")
            assert True==False

            self.driver.close()
            self.logger.info("*********** Ending Home Page Title Test************")
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))