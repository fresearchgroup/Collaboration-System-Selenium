__author__ = 'dhanushsr'

import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from decouple import config

IP = config('IP_ADDRESS')
PORT = config('PBLCLIENT_PORT')

class ProjectPage(unittest.TestCase):

    

    def setUp(self):
        # self.driver = webdriver.Remote(command_executor='http://192.168.119.128:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX) 
        self.driver = webdriver.Firefox()     

    def test_UI5_1(self):
        driver = self.driver 
        driver.get("http://"+IP+":"+PORT+"/dashboard")
        # driver.find_element_by_xpath('//*[@id="headerMenuCollapse"]/div/div/div[2]/ul/li[5]/a').click()
        driver.find_element_by_link_text('Create new project').click()
        assert "Create a new Project" in driver.page_source

    def test_UI5_2(self):
        driver = self.driver
        driver.get("http://"+IP+":"+PORT+"/create_project")
        driver.find_element_by_id("save_and_redirect_btn").click()
        alertmessage = self.driver.switch_to.alert.text
        self.assertEqual("Please enter all information to continue", alertmessage)

    def test_UI5_3(self):
        driver = self.driver
        driver.get("http://"+IP+":"+PORT+"/create_project")
        driver.find_element_by_xpath('//*[@id="createTodoForm"]/fieldset/div[4]/button[2]').click()
        assert "dashboard" in driver.current_url

    def test_UI5_4(self):
        driver = self.driver
        driver.get("http://"+IP+":"+PORT+"/create_project")
        elem = driver.find_element_by_id("project_title")
        elem.send_keys("Testing")
        elem = driver.find_element_by_id("project_description")
        elem.send_keys("Sample testing Project")
        elem = driver.find_element_by_id("no_of_modules")
        elem.send_keys("2")
        driver.find_element_by_id("save_and_redirect_btn").click()
        assert "Testing/Module List" in driver.page_source


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
