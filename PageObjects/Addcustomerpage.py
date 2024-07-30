import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
class AddCustomer:
    link_Customers_menu_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    linkCustomers_menuitem_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    btnAddnew_xpath="/html/body/div[3]/div[1]/form[1]/div/div/a"
    txt_Email_xpath="//input[@id='Email']"
    txt_Password_xpath="//input[@id='Password']"
    txt_CustomerRoles_xpath="//input[@class='select2-search__field']"
    listitemAdministrators_xpath='//*[@id="SelectedCustomerRoleIds"]/option[1]'
    listitemRegistered_xpath='//*[@id="SelectedCustomerRoleIds"]/option[3]'
    listitemGuests_xpath="//*[@id='SelectedCustomerRoleIds']/option[4]"
    #listitemVendors_xpath="//li[contains(text(),'Vendors')]"
    drpdwnOfVendor_xpath="//*[@id='VendorId']"
    rdMaleGender_id="Gender_Male"
    rdFemaleGender_id="Gender_Female"
    txtFirstname_xpath="//input[@id='FirstName']"
    txtLastName_xpath="//input[@id='LastName']"
    txtDOB_xpath="//input[@id='DateOfBirth']"
    txtCompanyName_xpath="//input[@id='Company']"
    txtAdminComment_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"
    def __init__(self,driver):
        self.driver=driver

    def ClickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.link_Customers_menu_xpath).click()

    def ClickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH,self.linkCustomers_menuitem_xpath).click()

    def ClickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def SetEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_Email_xpath).send_keys(email)

    def SetPassword(self,password):
        self.driver.find_element(By.XPATH,self.txt_Password_xpath).send_keys(password)

    def SetCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txt_CustomerRoles_xpath).click()
        time.sleep(3)
        if role=='Registered':
            self.listitem=self.driver.find_element(By.XPATH,self.listitemRegistered_xpath)
        elif role=='Administrators':
            self.listitem=self.driver.find_element(By.XPATH,self.listitemAdministrators_xpath)
        elif role=="Guests":
            self.listitem=self.driver.find_element(By.XPATH,self.listitemGuests_xpath)
            #here user can be Registered,Administrators,Guests
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds']").click()
            self.listitem=self.driver.find_element(By.XPATH,self.listitemGuests_xpath)
        elif role=='Registered':
            self.listitem=self.driver.find_element(By.XPATH,self.listitemRegistered_xpath)
        elif role=='Vendors':
            self.listitem=self.driver.find_element(By.XPATH,self.listitemVendors_xpath)
        else:
            self.listitem=self.driver.find_element(By.XPATH,self.listitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def SetManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpdwnOfVendor_xpath))
        drp.select_by_visible_text(value)
    def  SetGender(self,gender):
        if gender=="Male":
           self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender=="Female":
            self.driver.find_element(By.ID,self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.Gender_Male).click()
    def SetFirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.txtFirstname_xpath).send_keys(firstname)
    def SetLastName(self,lastname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lastname)
    def SetDOB(self,dob):
        self.driver.find_element(By.XPATH,self.txtDOB_xpath).send_keys(dob)
    def  SetCompanyName(self,comname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(comname)
    def SetAdminComment(self,comment):
        self.driver.find_element(By.XPATH,self.txtAdminComment_xpath).send_keys(comment)
    def ClickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()