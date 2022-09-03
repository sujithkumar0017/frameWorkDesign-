import time
import pytest
from pageObjects.Add_Customer import AddCustomer
from pageObjects.Search_Customer import search_customer

from pageObjects.loginPage import Login
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

@pytest.mark.usefixtures("init__driver")
class Test_004_searchEmail:
    baseURL = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_searchCustomer_Emailid(self):
        self.logger.info("******Search_Customer_EmailID**************")
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.SetUsername(self.useremail)
        self.lp.SetPassword(self.password)
        self.lp.clickLogin()
        self.driver.maximize_window()
        self.logger.info("************Login Successful*********")
        self.logger.info("*********Starting for Searching a Customer********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuitem()

        self.logger.info("********Search a Customer********")
        self.searchCustomer= search_customer(self.driver)
        self.searchCustomer.SetEmail("victoria_victoria@nopCommerce.com")
        self.searchCustomer.SearchButton()
        time.sleep(10)
        status = self.searchCustomer.SearchByEmailId("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("*******TC_SearchCustomerByEmail_004 finished**********")
