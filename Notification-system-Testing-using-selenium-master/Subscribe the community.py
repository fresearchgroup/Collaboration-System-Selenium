__author__= 'shubh'
import unittest
from decouple import config
from selenium import webdriver

class signup(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Firefox()

	def login(self,var,driver):
		driver.get(config('IP_ADDRESS'))
		driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
		driver.get(config('IP_ADDRESS') + 'login/?next=/')
		elem = driver.find_element_by_id("id_username")
		user = config('NOTIFICATION_USER').split(',')
		elem.send_keys(user[var])
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(config('NOTIFICATION_PASSWORD'))
		driver.find_element_by_class_name('btn-block').click()

	def test_draftToVisisbleState(self):	
		driver = webdriver.Firefox()
		self.login(3,driver)
		driver.get(config('IP_ADDRESS') + 'communities/')
		driver.find_element_by_xpath('//a [@href="/community-view/2/"]').click()
		driver.find_element_by_id("join-us").click()
		driver.get(config('IP_ADDRESS') + 'notifications/')
			
	@classmethod
	def tearDown(cls):
		cls.driver.quit()

if __name__ == '__main__':
	unittest.main()
