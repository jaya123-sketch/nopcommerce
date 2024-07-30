from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("launching chrome browser")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("launching firefox browser")
    elif browser=='edge':
       driver=webdriver.Edge()
       print("launching edge browser")
    else:
        driver=webdriver.Ie()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  #this wii return browser value to setup method
    return request.config.getoption("--browser")

#############pytest HTML reports##########


#######hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata={
        "Project Name":"nopCommerce",
        "Module Name":"Customers",
         "Tester":"Jayalakshmi"
    }
############hook for delete/modify environment info to HTML report
@pytest.mark.opionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME",None)
    metadata.pop("Plugins",None)