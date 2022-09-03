import time

import pytest

from pageObjects.Add_Customer import AddCustomer
from pageObjects.Search_Customer import search_customer
from pageObjects.loginPage import Login
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

@pytest.mark.usefixtures("init__driver")
class Test_005_SearchCustomerByFirstname:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_SearchCustomerByFirstname(self):
        self.logger.info("******Search_By_Firstname********")
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.SetPassword(self.password)
        self.lp.clickLogin()
        self.driver.maximize_window()

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuitem()

        self.searchCustomer= search_customer(self.driver)
        self.searchCustomer.SetFirstname("Victoria")
        self.searchCustomer.SearchButton()
        time.sleep(5)
        Status = self.searchCustomer.SearchByFirstname("Victoria Terces")
        assert True == Status
        self.logger.info("*******Test_005_SearchCustomerByFirstname(Passed)*******")
