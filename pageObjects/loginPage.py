from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException


class Login:
    textboxes_username_Xpath="//input[@id='Email']"
    textboxes_password_id="Password"
    button_login_class="button-1.login-button"
    button_logout_Css_Selector="a[href*='/logout']"
    def __init__(self, driver):
         self.driver=driver
    def SetUsername(self,username):
         self.driver.find_element(By.XPATH,self.textboxes_username_Xpath).clear()
         self.driver.find_element(By.XPATH,self.textboxes_username_Xpath).send_keys(username)
    def SetPassword(self,password):
        self.driver.find_element(By.ID,self.textboxes_password_id).clear()
        self.driver.find_element(By.ID,self.textboxes_password_id).send_keys(password)
    def clickLogin(self):
         self.driver.find_element(By.CLASS_NAME,self.button_login_class).click()
    def clickLogout(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_logout_Css_Selector).click()
        #self.driver.execute_script("argument[0].click();",Logout)
        #wait = WebDriverWait(self.driver, 30)
        #wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_logout_Css_Selector))).click()
        """WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_logout_Css_Selector)))
        Next = self.driver.find_element(By.CSS_SELECTOR, self.button_logout_Css_Selector)
        Next.click()
        #element = self.driver.find_element(By.CSS_SELECTOR, self.button_logout_Css_Selector)
        #webdriver.ActionChains(self.driver).move_to_element(element).click(element).perform()"""