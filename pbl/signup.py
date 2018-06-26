import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class LoginCorrect(unittest.TestCase):
    
    	def setUp(self):
           self.driver = webdriver.Remote(command_executor='http://192.168.211.129:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX) 
               

    	def test_LoginCorrect(self):
         fname = "Aadarsh"
         lname = "Singh"
         cno = "7894561230"
         email = "aadarsh@gmail.com"
         user ="aadarsh"
         pwd= "root123456"

         driver = webdriver.Remote(command_executor='http://192.168.211.129:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX) 
         # driver = webdriver.Firefox()
         # driver.maximize_window()


         driver.get("http://192.168.211.129:8001/register/")
         elem = driver.find_element_by_id("first_name")
         elem.send_keys(fname)
         elem = driver.find_element_by_id("last_name")
         elem.send_keys(lname)
         elem = driver.find_element_by_id("contact_no")
         elem.send_keys(cno)
         elem = driver.find_element_by_id("email")
         elem.send_keys(email)
         elem = driver.find_element_by_id("username")
         elem.send_keys(user)
         elem = driver.find_element_by_id("password")
         elem.send_keys(pwd)
         driver.find_element_by_name('user_type').click()
         # driver.find_element_by_class_name('custom-control-input').click()
         driver.find_element_by_id('create_account_btn').click()


    	def tearDown(self):
           self.driver.quit()


if __name__ == '__main__':
           unittest.main()