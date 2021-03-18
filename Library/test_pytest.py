from selenium import webdriver
#from webdriver_manager.firefox import GeckoDriverManager

#PyTest Fixures
import pytest
@pytest.fixture(params=["chrome","firefox"],scope="function")
def setup(request):
    if request.param =='chrome':
     browser = webdriver.Chrome("D:\projectdemo\Env\chromedriver.exe")
     browser.get("https://google.com")
    print("once before every method")
    if request.param =='firefox':
     #browser = webdriver.Firefox(executable_path="D:\projectdemo\Env\geckodriver.exe")
     browser = webdriver.Chrome("D:\projectdemo\Env\chromedriver.exe")
     browser.get("https://google.co.in")
    yield
    print("once after every method")
    browser.close()

def testmethod1(setup):
    print("test method1")

##def testmethod2(setup):
##    print("test method2")


