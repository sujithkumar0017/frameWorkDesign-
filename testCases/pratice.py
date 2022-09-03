from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("http://admin-demo.nopcommerce.com/")
driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.CLASS_NAME,"button-1.login-button").click()
driver.find_element(By.LINK_TEXT,"Logout").click()