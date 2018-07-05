nimport unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from decouple import config
DSpace_IP = config('DSpace_Selenium_IP')
DSpace_Port = config('DSpace_Selenium_Port')

class DSpace(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		var="createcommunityarticles/"
		self.driver.get("http://"+DSpace_IP+":"+DSpace_Port+"/"+var)
		self.driver.maximize_window()
		
	def test_Check_Groups(self):
		driver = self.driver
		groups = driver.find_element_by_id('check_groups')
		groups.click()
		WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id('check_group_articles'))
		result = driver.find_element_by_id('results')
		self.assertEqual(result,'Success')
		
	def tearDown(self):
		self.driver.quit()
		
		
if __name__ == '__main__':
	unittest.main()
