import pytest
from selenium import webdriver

@pytest.fixture(params=['chrome','Ie'],scope="class")
def setup(request):
    if request.param == 'chrome':
     chrome_driver = webdriver.Chrome('D:\projectdemo\Env\chromedriver.exe')
    if request.param == 'Ie':
     chrome_driver = webdriver.Chrome('D:\projectdemo\Env\chromedriver.exe')
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()

@pytest.mark.usefixtures("setup")
class Test_method():
    def test_main(self):
        self.driver.get('https://google.com')