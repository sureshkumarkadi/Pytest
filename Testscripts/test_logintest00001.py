import os
import sys
import traceback
import unittest
import pytest
import allure
#from allure_commons.types import AttachmentType
import pytest_html_reporter


import time

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))
print(folder_path)


sys.path.insert(0, folder_path + "/Syslibrary")
sys.path.insert(0, folder_path + "/Library")

from login import registration


reg = registration()

tf = 'test_TestcaseNo100001'


# @allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
class openbrowser(unittest.TestCase):
    #@allure.severity(allure.severity_level.MINOR)
    def test_openbrowser(self):
        try:
            # print('enter')
            browser = reg.openbrowser()
            time.sleep(3)
            # reg.inputurl(browser)
            gettitle = browser.title
            print(gettitle)
            self.assertEqual(gettitle, 'Google')
            # print("pass")
        except Exception:
            #traceback.print_exc()
            #allure.attach(browser.get_screenshot_as_png(), name="title", attachment_type=AttachmentType.PNG)
            pytest_html_reporter.attach(browser.get_screenshot_as_png())
            # browser.save_screenshot(folder_path+'\Screenshots\Testcase-%s.png' %tf)
            self.fail("Test case No failed")
        finally:
            reg.closebrowser(browser)

    #@allure.severity(allure.severity_level.NORMAL)
    def test_openbrowser1(self):
        try:
            # print('enter')
            browser = reg.openbrowser()

            reg.inputurl(browser)
            gettitle = browser.title
            # print(gettitle)
            self.assertEqual(gettitle, 'Google')
            # print("pass")
        except Exception:
            #traceback.print_exc()
            #allure.attach(browser.get_screenshot_as_png(), name="title", attachment_type=AttachmentType.PNG)
            pytest_html_reporter.attach(browser.get_screenshot_as_png())
            # browser.save_screenshot(folder_path+'\Screenshots\Testcase-%s.png' %tf)
            self.fail("Test case No failed")
        finally:
            reg.closebrowser(browser)


if __name__ == '__main__':
    unittest.main()
