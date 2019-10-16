# coding=utf-8
import unittest
import time
import sys
from baseSetting.browser_engine import BrowserEngine
from pageObject.baidu_homepage import HomePage
from baseSetting.logger import Logger

logger = Logger(logger="BaiduSearch").getlog()

class BaiduSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_1_baidu_search(self):
        """ 搜索 selenium """
        homepage = HomePage(self.driver)
        homepage.input_selenium('selenium')
        homepage.click_baiduyixia()
        expect_text = 'Selenium(浏览器自动化测试框架)_百度百科'
        actual_text = homepage.get_sousuo_text()
        try:
            self.assertEqual(expect_text, actual_text)
            logger.info('expect_text: %s is equal to actual_text: %s .Test pass.' % (expect_text, actual_text))
        except Exception as e:
            logger.info(format(e))
            logger.info('Tess fail.')

if __name__ == '__main__':
    unittest.main()