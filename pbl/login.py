import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class LoginCorrect(unittest.TestCase):
    
    	def setUp(self):
           self.driver = webdriver.Remote(command_executor='http://192.168.211.129:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX) 
               

    	def test_LoginCorrect(self):
           user ="triples59"
           pwd= "root1234"
           driver = webdriver.Remote(command_executor='http://192.168.211.129:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX) 

      
           driver.get("http://192.168.211.129:8001/login/")
           elem = driver.find_element_by_id("username")
           elem.send_keys(user)
           elem = driver.find_element_by_id("password")
           elem.send_keys(pwd)
           driver.find_element_by_name('user_type').click()
           driver.find_element_by_id('sign_in_btn').click()


    	def tearDown(self):
           self.driver.quit()


if __name__ == '__main__':
           unittest.main()