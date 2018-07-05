import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class Log_in(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.get("http://" + config('IP_ADDRESS') + ':' + config('REPUTATION_PORT'))
		self.driver.maximize_window()

	def test_Log_in(self):
		driver = self.driver
		username = driver.get(config('REPUTATION_USER')).split(',')
		elem = driver.find_element_by_id('id_username')
		elem.send_keys(username[0])
		password = driver.get(config('REPUTATION_PASSWORD'))
		elem = driver.find_element_by_id('id_password')
		elem.send_keys(password)
		#driver.find_element_by_id('id_username').send_keys('amu')
		#driver.find_element_by_id('id_password').send_keys('!!Killerbee8')
		driver.find_element_by_id('log_in_btn').click()
		driver.get("http://127.0.0.1:8000/article-view/4/")
		driver.find_elements_by_css_selector('#my_form>button')[0].click()
	
	def tearDown(self):
		self.driver.quit()
	
if __name__ == '__main__':
	unittest.main()
