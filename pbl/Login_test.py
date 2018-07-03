__author__ = 'naveen t'

import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains

class LoginCorrect(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_UI7_1(self):

		fname = 'Saurabh'+''.join(random.SystemRandom().choice(string.digits) for _ in range(3))
		lname = 'Singh'+''.join(random.SystemRandom().choice(string.digits) for _ in range(3))
		cno =  ''.join(random.SystemRandom().choice(string.digits) for _ in range(10))
		email = 'saurabh'+''.join(random.SystemRandom().choice(string.digits) for _ in range(3))+'@gmail.com'
		user = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
		pwd=  ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))

		# Creating User account
		driver = self.driver

		driver.get("http://localhost:8001/register/")
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
		driver.find_element_by_id('create_account_btn').click()

		driver.get("http://localhost:8001/login")
		elem = driver.find_element_by_id("username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("password")
		elem.send_keys(pwd)
		driver.find_element_by_name("user_type").click()
		driver.find_element_by_class_name("custom-checkbox").click()
		driver.find_element_by_id("sign_in_btn").click()
		assert "dashboard" in driver.current_url

	def test_UI7_2(self):
		user = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
		pwd=  ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))

		driver.get("http://localhost:8001/login")
		elem = driver.find_element_by_id("username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("password")
		elem.send_keys(pwd)
		driver.find_element_by_name("user_type").click()
		driver.find_element_by_class_name("custom-checkbox").click()
		driver.find_element_by_id("sign_in_btn").click()

		assert "login" in driver.current_url

    def test_UI7_3(self):
        driver = self.driver
        driver.get("http://localhost:8001/login")
        driver.find_element_by_id("sign_in").click()
        alertmessage = self.driver.switch_to.alert.text
        self.assertEqual("Enter All Information", alertmessage)

	def test_UI7_4(self):
		
		driver=self.driver
		driver.get("http://localhost:8001/login")
		element = driver.find_element_by_link_text("Sign in")
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		hover = ActionChains(driver).move_to_element(element).perform()
		txtdec = element.value_of_css_property('text-decoration')
		self.assertEqual('underline', txtdec)

	def test_UI7_5(self):
		
		driver=self.driver
		driver.get("http://localhost:8001/login") 
		driver.find_element_by_link_text('Sign up').click()
		assert "register" in driver.current_url   

	def tearDown(self):
	   self.driver.quit()

		
if __name__ == '__main__':
	unittest.main()
