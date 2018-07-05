__author__ = 'saurabhsingh'

import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from decouple import config



class SignUpCorrect(unittest.TestCase):

        IP = config('IP_ADDRESS')
        PORT = config('PBLCLIENT_PORT')
	
	def setUp(self):
		self.driver = webdriver.Firefox()
		# self.driver = webdriver.Remote(command_executor='http://192.168.211.129:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)   


	def test_UI6_1(self):
		
		driver=self.driver
		driver.get("http://IP:PORT/login")
		driver.find_element_by_link_text('Sign up').click()
		assert "register" in driver.current_url

	def test_UI6_2(self):
		
		driver=self.driver
		driver.get("http://IP:PORT/register")
		element = driver.find_element_by_id("create_account_btn")
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		hover = ActionChains(driver).move_to_element(element).perform()
		bgcolor = element.value_of_css_property('background-color')
		# print(bgcolor)
		self.assertEqual('rgb(70, 127, 207)', bgcolor)


	def test_UI6_3(self):
		
		driver=self.driver
		driver.get("http://IP:PORT/register")
		driver.find_element_by_id('create_account_btn').click()
		alertmessage = self.driver.switch_to.alert.text
		self.assertEqual('Enter All Information', alertmessage)


	def test_UI6_4(self):
		fname = 'Saurabh'+''.join(random.SystemRandom().choice(string.digits) for _ in range(3))
		lname = 'Singh'+''.join(random.SystemRandom().choice(string.digits) for _ in range(3))
		cno =  ''.join(random.SystemRandom().choice(string.digits) for _ in range(10))
		email = 'saurabh'+''.join(random.SystemRandom().choice(string.digits) for _ in range(3))+'@gmail.com'
		user = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
		pwd=  ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))

		# driver = webdriver.Remote(command_executor='http://192.168.211.129:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX) 
		driver = self.driver
		# driver.maximize_window()


		driver.get("http://IP_PORT/register/")
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
		# print(driver.current_url)
		assert "dashboard" in driver.current_url


	def test_UI6_5(self):
		
		driver=self.driver
		driver.get("http://IP:PORT/register")
		element = driver.find_element_by_link_text("Sign in")
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		hover = ActionChains(driver).move_to_element(element).perform()
		txtdec = element.value_of_css_property('text-decoration')
		# print(txtdec)
		self.assertEqual('underline', txtdec)

	def test_UI6_6(self):
		
		driver=self.driver
		driver.get("http://IP:PORT/register") 
		driver.find_element_by_link_text('Sign in').click()
		assert "login" in driver.current_url   

	def tearDown(self):
	   self.driver.quit()

		
if __name__ == '__main__':
	unittest.main()
