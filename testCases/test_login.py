import pytest
from pageObjects.loginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("init__driver")
class Test_001_login:
    baseURL = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    def test_homePageTitle(self):
        self.logger.info("***************** Test_001_Login *****************")
        self.logger.info("***************** Verifying Home Page Title *****************")
        #print("testing home page")
        # self.driver = init__driver
        #print(self.driver)
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        print(f'actual_title: {actual_title}')
        assert actual_title == "Your store. Login"
    def test_login(self):
              self.logger.info("***************** Verifying Login *****************")
              self.driver.get(self.baseURL)
              self.lp = Login(self.driver)
              self.lp.SetUsername(self.useremail)
              self.lp.SetPassword(self.password)
              self.lp.clickLogin()
              act_title = self.driver.title
              if act_title == "Dashboard / nopCommerce administration":
                 assert True
                 self.logger.info("***************** Login Passed *****************")
              else:
                  self.driver.save_screenshot("login.png")
                  self.logger.error("***************** Login test is failed *****************")
                  assert False

