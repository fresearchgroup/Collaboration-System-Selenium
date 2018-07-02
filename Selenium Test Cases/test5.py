import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from decouple import config
class DSpace(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		var = "creategrouparticles/"
		self.driver.get("http://"+config('IP')+":"+config('port')+"/"+var)
		self.driver.maximize_window()
		
	def test_Check_Home(self):
		home = driver.find_element_by_id('home')
		home.click()
		WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id('create_community'))
		
	def tearDown(self):
		self.driver.quit()
		
		
if __name__ == '__main__':
	unittest.main()
