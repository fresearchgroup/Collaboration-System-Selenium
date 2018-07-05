import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from decouple import config
DSpace_IP = config('DSpace_Selenium_IP')
DSpace_Port = config('DSpace_Selenium_Port')

class DSpace(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get("http://"+DSpace_IP+":"+DSpace_Port+"/")
		self.driver.maximize_window()
		
	def test_Community_test(self):
		driver = self.driver
		create_community = driver.find_element_by_id('create_community')
		create_community.click()
		WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id('create_community_articles'))
		result = driver.find_element_by_id('results')
		self.assertEqual(result,'Success')
	
	def tearDown(self):
		self.driver.quit()
		
		
if __name__ == '__main__':
	unittest.main()
