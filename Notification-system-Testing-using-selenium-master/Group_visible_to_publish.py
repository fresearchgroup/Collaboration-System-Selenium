__author__= 'shubh'
import unittest
from decouple import config
from selenium import webdriver

class signup(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Firefox()

	def login(self,var,driver):
		driver.get(config('url'))
		driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
		driver.get(config('url') + 'login/?next=/')
		elem = driver.find_element_by_id("id_username")
		user = config('user').split(',')
		elem.send_keys(user[var])
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(config('pwd'))
		driver.find_element_by_class_name('btn-block').click()

	def test_draftToVisisbleState(self):	
		driver = webdriver.Firefox()
		self.login(2,driver)
		driver.get(config('url') + 'communities/')
		driver.find_element_by_xpath('//a [@href="/community-view/2/"]').click()
		driver.find_element_by_xpath('//a [@href="/group-view/1/"]').click()
		driver.find_element_by_xpath('//a [@href="/group_content/1/"]').click()
		driver.find_element_by_xpath('//a [@href="/article-view/8/"]').click()
		driver.find_element_by_xpath('//a [@href="/article-edit/8/"]').click()
		driver.find_element_by_id('publish').click()
		driver.get(config('url') + 'articles/')
		driver.get(config('url') + 'logout/')
		for i in range(1,4):
			self.login(i,driver)
			driver.find_element_by_xpath('//a [@href="/notifications/"]').click()
			driver.get(config('url') + 'logout/')


	@classmethod
	def tearDown(cls):
		cls.driver.quit()

if __name__ == '__main__':
	unittest.main()
