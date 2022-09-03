import random
import string
import time
from faker import Faker

import pytest
from selenium.webdriver.common.by import By

from pageObjects.Add_Customer import AddCustomer
from pageObjects.loginPage import Login
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

@pytest.mark.usefixtures("init__driver")
class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()

    def test_addcustomer(self):
        self.logger.info("***********Test_003_AddCustomer*******")
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.SetUsername(self.useremail)
        self.lp.SetPassword(self.password)
        self.lp.clickLogin()
        self.driver.maximize_window()
        self.logger.info("************Login Successful*********")

        self.logger.info("*******Starting Add Customer Test**********")

        self.faker = Faker()
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        #time.sleep(3)
        self.addcust.clickOnCustomerMenuitem()
        #time.sleep(3)
        self.addcust.ClickOnAddNew()
        #time.sleep(3)

        self.logger.info("********* Adding Customer Info **********")

        #self.email = random_generator() + "@gmail.com"
        self.addcust.SetEmail(self.faker.email())
        self.addcust.SetPassword("test123")
        self.addcust.Customer_roles("Guests")
        self.addcust.SetManagerVendor("Vendor 2")
        self.addcust.SetGender("Male")
        self.addcust.SetFirstname(self.faker.name())
        self.addcust.SetLastname(self.faker.name())
        self.addcust.SetDateOfBirth("9/03/2000")
        self.addcust.SetCompanyName("busyQA")
        self.addcust.Admin_Comment("This is for testing")
        self.addcust.ClickOnSave()


        self.logger.info("*******Saving customer info*********")

        self.logger.info("****** Add Customer Validation started *******")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text             #It will overall body of the page.

        #print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("******** Added customer Successfully *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer_scr.png")
            self.logger.info("********Add Customer Test Failed **********")
            assert True == False

        self.logger.info("********* Ending Home Page test **********")

# def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
#        return''.join(random.choice(chars) for x in range(size))