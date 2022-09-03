import time
import pytest

from pageObjects.loginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtilis

@pytest.mark.usefixtures("init__driver")
class Test_002_DDT_login:
    baseURL = ReadConfig.getApplicationUrl()
    path= ".//Test_Data/Login_Excel.xlsx"
    logger=LogGen.loggen()
    def test_login(self):
              self.logger.info("***************** Test_002_DDT_Login *****************")
              self.logger.info("***************** Verifying Login *****************")
              self.driver.get(self.baseURL)
              self.lp=Login(self.driver)
              self.rows=XLUtilis.getRowCount(self.path,'Sheet1')
              print("Number of Rows:",self.rows)
              lst_status=[]
              for r in range(2,self.rows+1):
                  self.user=XLUtilis.readData(self.path,'Sheet1',r,1)
                  self.password=XLUtilis.readData(self.path, 'Sheet1', r, 2)
                  self.exp=XLUtilis.readData(self.path, 'Sheet1', r, 3)
                  self.lp.SetUsername(self.user)
                  self.lp.SetPassword(self.password)
                  self.lp.clickLogin()
                  time.sleep(3)

                  act_title=self.driver.title
                  exp_title="Dashboard / nopCommerce administration"

                  if act_title==exp_title:
                      if self.exp=="Pass":
                          self.logger.info("*****Passed*****")
                          self.lp.clickLogout()
                          lst_status.append("Pass")
                      elif self.exp=="Fail":
                          self.logger.info("*****Failed*****")
                          self.lp.clickLogout()
                          lst_status.append("Fail")
                  elif act_title!=exp_title:
                      if self.exp=='Pass':
                         self.logger.info("*****Failed*****")
                         lst_status.append("Fail")
                      elif self.exp=='Fail':
                          self.logger.info("******Passed*****")
                          lst_status.append("Pass")

              if "Fail" not in lst_status:
                  self.logger.info("*******Login DDT test Passed********")
                  #self.driver.close()
                  assert True
              else:
                  self.logger.info("*******Login DDT test failed********")
                  #self.driver.close()
                  assert False

              self.logger.info("*******End of Login DDT Test********")
              self.logger.info("*******Completed TC_LoginDDT_002********")

