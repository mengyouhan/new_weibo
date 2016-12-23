from bs4 import BeautifulSoup
import requests
import os,time
from selenium import webdriver

# Chrome()PhantomJS()
class Comm(object):
    def __init__(self,url,loginName,loginPassword,txtComment):
        self.url = url
        self.loginName = loginName
        self.loginPassword = loginPassword
        self.txtComment = txtComment

    def start(self):
        driver = webdriver.PhantomJS()
        driver.get(self.url)
        time.sleep(6)
        driver.find_element_by_css_selector(".m-diy-btn .m-font-comment").click()
        time.sleep(8)
        driver.find_element_by_css_selector(".btnWhite").click()
        time.sleep(8)

        driver.find_element_by_css_selector("#loginName").send_keys(self.loginName)
        driver.find_element_by_css_selector("#loginPassword").send_keys(self.loginPassword)
        time.sleep(8)
        driver.find_element_by_css_selector("#loginAction").click()
        time.sleep(4)
        driver.find_element_by_css_selector(".m-diy-btn .m-font-comment").click()
        time.sleep(4)
        driver.find_element_by_css_selector("#settop-publisher").click()

        time.sleep(4)
        driver.find_element_by_css_selector("#txt-publisher").send_keys(self.txtComment)
        driver.find_element_by_css_selector("#txt-publisher").click()
        time.sleep(10)
        driver.find_element_by_css_selector(".module-topbar .fr").click()

