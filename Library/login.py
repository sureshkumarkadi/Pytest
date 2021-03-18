import os
import sys
from selenium import webdriver

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))
print(folder_path)

sys.path.insert(0, folder_path + '\Syslibrary')
sys.path.insert(0, folder_path + '\Env')

from datadriver import jsonread

read1 = jsonread()


class registration():
    def openbrowser(self):
        value1 = read1.jsonread(folder_path + '\Env\setup.json')
        #print(value1)
        if value1["browser"] == 'chrome':
            browser = webdriver.Chrome(folder_path + '\Env\chromedriver.exe')
            return browser

    def closebrowser(self, browser):
        browser.close()

    def inputurl(self, browser):
        url = read1.jsonread(folder_path + '\Env\setup.json')
        browser.get(url["url"])
