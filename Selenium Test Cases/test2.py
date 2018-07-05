import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from decouple import config
DSpace_IP = config('DSpace_Selenium_IP')
DSpace_Port = config('DSpace_Selenium_Port')

class DSpace(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		var = "createcommunity/"
		self.driver.get("http://"+DSpace_IP+":"+DSpace_Port+"/"+var)
		self.driver.maximize_window()
		
	def test_community_article_test(self):
		driver = self.driver
		community_articles = driver.find_element_by_id('create_community_articles')
		community_articles.click()
		WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id('check_groups'))
		result = driver.find_element_by_id('results')
		self.assertEqual(result,'Success')
		
	def tearDown(self):
		self.driver.quit()
		
		
if __name__ == '__main__':
	unittest.main()
