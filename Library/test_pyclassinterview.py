import pytest
from selenium import webdriver
import allure
@pytest.fixture(params=['chrome','Firefox'],scope="class")
def setup(request):
    if request.param == "chrome":
     chrome_driver = webdriver.Chrome('D:\projectdemo\Env\chromedriver.exe')
    if request.param == "Firefox":
     chrome_driver = webdriver.Chrome('D:\projectdemo\Env\chromedriver.exe')
    request.cls.browser = chrome_driver
    yield
    chrome_driver.close()

@pytest.mark.usefixtures("setup")
class Test_pytest():
    @allure.severity(allure.severity_level.MINOR)
    def test_pytestclass(self):
        self.browser.get('https://google.co.in')
        print(self.browser.title)
        title = 'Google'
        assert title == self.browser.title

def sum1(a,b):
    c = a+b
    print("value for c is:",c)
    #return c
sum1(1,2)

list1 = [1,2,3]

print([i for i in list1 if i%2==0])
