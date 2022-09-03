import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.ie.service import Service as IEService

@pytest.fixture()
def init__driver(browser,request):
        if browser =='chrome':
         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser =='firefox':
         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
         driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
         return driver
        driver.implicitly_wait(10)
        request.cls.driver = driver
        yield driver
        driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

######### PYTEST HTML REPORTS ###############

#It is hook for adding environment info to html reports
def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester']= 'sujith'
    config._metadata['Lead']= 'Aravinth'

#It is hook for delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)


# pytest -s -v testCases/test_login.py --browser chrome --html=Reports/report.html

#Parallel Execution

#pytest -s -v -n=3 testCases/test_login.py --browser chrome --html=Reports/report.html