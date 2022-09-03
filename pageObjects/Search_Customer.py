from selenium.webdriver.common.by import By


class search_customer:

    txt_email_id = "SearchEmail"
    txt_firstname_id = "SearchFirstName"
    txt_lastname_id = "SearchLastName"
    btn_searchButton_id = "search-customers"

    tblSearchResult_Xpath = "//table[@role='grid']"
    table_Xpath = "//div[@id='customers-grid_wrapper']"
    tableRows_Xpath = "//div[@id='customers-grid_wrapper']//tbody/tr"
    tableColumns_Xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver
    def SetEmail(self,email):
        self.driver.find_element(By.ID,self.txt_email_id).send_keys(email)
    def SetFirstname(self,firstname):
        self.driver.find_element(By.ID,self.txt_firstname_id).send_keys(firstname)
    def SetLastname(self,lastname):
        self.driver.find_element(By.ID,self.txt_lastname_id).send_keys(lastname)
    def SearchButton(self):
        self.driver.find_element(By.ID,self.btn_searchButton_id).click()
    def GetNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_Xpath))
    def GetNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColumns_Xpath))
    def SearchByEmailId(self,email):
        flag=False
        for r in range(1,self.GetNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_Xpath)
            emailid = table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr/td[2]").text
            if emailid == email:
                flag=True
                break
        return flag

    def SearchByFirstname(self,firstname):
        flag=False
        for r in range(1,self.GetNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_Xpath)
            Firstname = table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr/td[3]").text
            if Firstname == firstname:
                flag=True
                break
        return flag

        
