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
		for i in range(1,4):
			self.login(i,driver)
			driver.get(config('IP_ADDRESS') + 'communities/')
			driver.find_element_by_xpath('//a [@href="/community-view/2/"]').click()
			driver.find_element_by_xpath('//a [@href="/group-view/1/"]').click()
			driver.find_element_by_xpath('//a [@href="/group_content/1/"]').click()
			driver.find_element_by_xpath('//a [@href="/article-view/11/"]').click()
			driver.find_element_by_xpath('//a [@href="/article-edit/11/"]').click()
			driver.find_element_by_id('savechanges').click()
			driver.get(config('IP_ADDRESS') + 'logout/')
			driver.get(config('IP_ADDRESS'))
			self.login(0,driver)
			driver.get(config('IP_ADDRESS') + 'notifications/')
			driver.implicitly_wait(100)
			driver.get(config('IP_ADDRESS') + 'logout/')


	@classmethod
	def tearDown(cls):
		cls.driver.quit()

if __name__ == '__main__':
	unittest.main()