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
		for i in range(0,3):
			self.login(i,driver)
			driver.get(config('url') + 'communities/')
			driver.find_element_by_xpath('//a [@href="/community-view/2/"]').click()
			driver.find_element_by_xpath('//a [@href="/community_content/2/"]').click()
			#make the id as visible of the button of visible in html file
			driver.find_element_by_xpath('//a [@href="/article-view/7/"]').click()
			driver.find_element_by_xpath('//a [@href="/article-edit/7/"]').click()
			driver.find_element_by_id('savechanges').click()
			driver.implicitly_wait(1000)
			driver.get(config('url') + 'logout/')
			driver.implicitly_wait(100)
			driver.get(config('url'))
			self.login(3,driver)
			driver.get(config('url') + 'notifications/')
			driver.implicitly_wait(100)
			driver.get(config('url') + 'logout/')
			driver.get(config('url'))


	@classmethod
	def tearDown(cls):
		cls.driver.quit()

if __name__ == '__main__':
	unittest.main()