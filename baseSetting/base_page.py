# coding=utf-8
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os.path
from baseSetting.logger import Logger
import sys
import importlib
importlib.reload(sys)

logger = Logger(logger="BasePage").getlog()

class BasePage(object):
    """
    把 selenium 常用的动作都封装在这里
    """

    def __init__(self, driver):
        self.driver = driver

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    # 定位元素方法
    def find_element(self, selector):
        """ 默认用 xpath 定位 可以多种定位方法封装在一起"""
        try:
            element = self.driver.find_element_by_xpath(selector)
            logger.info("Had find the element \' %s \' successful " % element.text)
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)     

        return element

    # 输入
    def input(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)

    # 清除文本框
    def clear(self, selector):
        """ 一般来说直接 clear 可以清除 但是有些输入框清除不了可以用下面这种方法 """
        el = self.find_element(selector)
        try:
            el.send_keys(Keys.CONTROL+'a')
            el.send_keys(Keys.DELETE)
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)  

    # 点击元素
    def click(self, selector):

        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # 获取文本
    def get_element_text(self, selector):

        logger.info("Current element text is %s" % self.find_element(selector).text)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)
