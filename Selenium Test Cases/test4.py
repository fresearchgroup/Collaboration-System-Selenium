import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from decouple import config
class DSpace(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		var = "creategroup/"
		self.driver.get("http://"+config('IP')+":"+config('port')+"/"+var)
		self.driver.maximize_window()
		
	def test_Check_Group_Articles(self):
		driver = self.driver
		group_articles=driver.find_element_by_id('check_group_articles')
		group_articles.click()
		WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id('home'))
		result = driver.find_element_by_id('results')
		self.assertEqual(result,'Success')
		
	def tearDown(self):
		self.driver.quit()
		
		
if __name__ == '__main__':
	unittest.main()
