import pytest
from selenium import webdriver


@pytest.fixture(params=['chrome','Firefox'],scope="class")
def setup(request):
    if request.param == 'chrome':
        chrome_driver = webdriver.Chrome('c')
        #request.cls.browser  = chrome_driver
        print('Run once before eery method')
    if request.param == 'Firefox':
        chrome_driver = webdriver.Chrome('D:\projectdemo\Env\chromedriver.exe')
    request.cls.browser  = chrome_driver
    print('Run once before eery method')
    yield
    chrome_driver.close()
    #return browser

#def test_method(setup):
 #   print('run this method')

#@pytest.mark.usefixtures("setup")
#class Basetest:
 #  pass
@pytest.mark.usefixtures("setup")
class Test_maintest():
    def test_classtest(self):
        self.browser.get('https://google.com')
        print("pass")
