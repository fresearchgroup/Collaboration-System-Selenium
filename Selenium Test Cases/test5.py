import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from decouple import config
DSpace_IP = config('DSpace_Selenium_IP')
DSpace_Port = config('DSpace_Selenium_Port')

class DSpace(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		var = "creategrouparticles/"
		self.driver.get("http://"+DSpace_IP+":"+DSpace_Port+"/"+var)
		self.driver.maximize_window()
		
	def test_Check_Home(self):
		home = driver.find_element_by_id('home')
		home.click()
		WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id('create_community'))
		
	def tearDown(self):
		self.driver.quit()
		
		
if __name__ == '__main__':
	unittest.main()
