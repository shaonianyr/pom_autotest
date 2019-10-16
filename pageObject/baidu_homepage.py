# coding=utf-8
from baseSetting.base_page import BasePage


class HomePage(BasePage):
    
    baidu_shurukuang = '//*[@id="kw"]'
    baiduyixia = '//*[@id="su"]'
    sousuojieguo = '//*[@id="2"]/h3/a'

    # 所有的返回文本动作
    def get_sousuo_text(self):
        self.get_element_text(self.sousuojieguo)
        return self.find_element(self.sousuojieguo).text

    # 所有的输入动作
    def input_selenium(self, text):
        self.input(self.baidu_shurukuang, text)
        self.sleep(1)

    # 所有的点击动作
    def click_baiduyixia(self):
        self.click(self.baiduyixia)
        self.sleep(1)
