import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_HomePageTitle(self,setup):
        self.logger.info("*********** Test_001_Login********")
        self.logger.info("************ Verifying Home Page Title************")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************  Home Page Title test is passed************")
        else:
            self.driver.save_screenshot(".\\Screenshots"+"\\test_HomePageTitle.png")
            self.driver.close()
            self.logger.error("************  Home Page Title test is failed************")
            assert False

    @pytest.mark.sanity

    def test_Login(self,setup):
        self.logger.info("************ Verifying Login test************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************ Login test is passed***********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_Login.png")
            self.logger.error("************ Login test is failed************")
            self.driver.close()
            assert False




