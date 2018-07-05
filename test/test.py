import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class Reputation_System(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.get("http://" + config('IP_ADDRESS') + ':' + config('REPUTATION_PORT'))
		self.driver.maximize_window()

	def test_login_test(self):
		driver = self.driver
		driver.find_element_by_link_text('Log In').click()
		username = driver.find_element_by_id('id_username')
		password = driver.find_element_by_id('id_password')
		username.clear()
		password.clear()
		username.send_keys("karthik")
		password.send_keys("kaushik123")
		driver.find_element_by_class_name('btn-block').click()
		driver.find_element_by_class_name('dropdown-toggle').text
	
	def tearDown(self):
		self.driver.quit()
	
if __name__ == '__main__':
	unittest.main()
	

