import time
from select import select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    lnk_Customer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_Customer_menuitems_xpath = "//a[@href='/Admin/Customer/List']"
    btn_AddNewCustomer_xpath = "//a[normalize-space()='Add new']"
    input_Email_xpath = '//input[@name="Email"]'
    input_Password_xpath = '//input[@name="Password"]'
    input_firstname_xpath = '//input[@name="FirstName"]'
    input_Lastname_xpath = '//input[@name="LastName"]'
    rb_gender_male_xpath = '//input[@id="Gender_Male"]'
    rb_gender_female_xpath = '//input[@id="Gender_Female"]'
    input_DOB_xpath = '//input[@id="DateOfBirth"]'
    input_company_xpath = '//input[@id="Company"]'
    checkbox_taxExempt_xpath = '//input[@id="IsTaxExempt"]'
    DD_customer_roles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    ls_registered_role_xpath = '//li[@class="k-item k-state-selected k-state-focused k-state-hover"]'
    register_close_icon = "//span[@title='delete']"
    ls_guest_role_xpath = "//li[contains(text(),'Guests')]"
    ls_forumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    ls_adminstration_xpath = "//li[contains(text(),'Administrators')]"
    ls_vendors_xpath = "//li[contains(text(),'Vendors')]"
    cb_active_xpath = '//input[@id="Active"]'
    Select_MangerForAdmin_Xpath = '//select[@id="VendorId"]'
    ta_AdminComment_xpath = '//textarea[@id="AdminComment"]'
    btn_Save_xpath = '//button[@name="save"]'
    
    def __init__(self,driver):
        self.driver = driver
    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnk_Customer_menu_xpath).click()
    def clickOnCustomerMenuitem(self):
        self.driver.find_element(By.XPATH,self.lnk_Customer_menuitems_xpath).click()
    def ClickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btn_AddNewCustomer_xpath).click()
    def SetEmail(self,email):
        self.driver.find_element(By.XPATH,self.input_Email_xpath).send_keys(email)
    def SetPassword(self,password):
        self.driver.find_element(By.XPATH,self.input_Password_xpath).send_keys(password)
    def SetFirstname(self,firstname):
        self.driver.find_element(By.XPATH,self.input_firstname_xpath).send_keys(firstname)
    def SetLastname(self,lastname):
        self.driver.find_element(By.XPATH,self.input_Lastname_xpath).send_keys(lastname)
    def gender_male(self):
        self.driver.find_element(By.XPATH,self.rb_gender_male_xpath).click()
    def gender_female(self):
        self.driver.find_element(By.XPATH,self.rb_gender_female_xpath).click()
    def SetDateOfBirth(self,DOB):
        self.driver.find_element(By.XPATH,self.input_DOB_xpath).send_keys(DOB)
    def SetCompanyName(self,companyName):
        self.driver.find_element(By.XPATH,self.input_company_xpath).send_keys(companyName)
    def tax_exempt(self):
        self.driver.find_element(By.XPATH,self.checkbox_taxExempt_xpath).click()
    def Customer_roles(self,role):
        self.driver.find_element(By.XPATH,self.DD_customer_roles_xpath).click()
        time.sleep(3)
        if role=="Registered":
            self.listitem = self.driver.find_element(By.XPATH,self.ls_registered_role_xpath)
        elif role=="Administrators":
            self.listitem = self.driver.find_element(By.XPATH,self.ls_adminstration_xpath)
        elif role=="Guests":
            time.sleep(3)
            self.driver.find_element(By.XPATH,self.register_close_icon).click()
            self.listitem = self.driver.find_element(By.XPATH,self.ls_guest_role_xpath)
        elif role=="Vendors":
            self.listitem = self.driver.find_element(By.XPATH,self.ls_vendors_xpath)
        elif role=="Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH,self.ls_forumModerators_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH,self.ls_guest_role_xpath)
            time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)
    def SetGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.XPATH,self.rb_gender_male_xpath).click()
        elif gender=='Female':
            self.driver.find_element(By.XPATH,self.rb_gender_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rb_gender_male_xpath).click()
    def SetManagerVendor(self,value):
        drp =Select(self.driver.find_element(By.XPATH,self.Select_MangerForAdmin_Xpath))
        drp.select_by_visible_text(value)
    def Admin_Comment(self,adminContent):
        self.driver.find_element(By.XPATH,self.ta_AdminComment_xpath).send_keys(adminContent)
    def ClickOnSave(self):
        self.driver.find_element(By.XPATH,self.btn_Save_xpath).click()
