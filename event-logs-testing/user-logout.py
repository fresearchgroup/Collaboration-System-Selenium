import unittest
from selenium import webdriver
import requests
from selenium.webdriver.support.ui import Select

class signup(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.url_basic = "http://localhost:8000/"

	def test_join_community(self):
		url_api = self.url_basic + 'logapi/event/user/logout/'
		result = requests.get(url_api).json()
		if (result["status code"] == 200):
			data = result["result"]
			total_hits = result["total hits"]
		user ="root"
		pwd= "pass1234"
		driver = webdriver.Firefox()
		driver.maximize_window() #For maximizing window
		driver.implicitly_wait(20) #gives an implicit wait for 20 seconds
		driver.get("http://localhost:8000/")
		driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(pwd)
		driver.find_element_by_class_name('btn-block').click()

		driver.get("http://localhost:8000/logout/")
		
		url_api = self.url_basic + 'logapi/event/user/logout/'
		result = requests.get(url_api).json()

		if (result["status code"] == 200):
			data = result["result"]
			if (result["total hits"]== total_hits+1):
				self.assertEqual(data[0]["event_name"],"event.user.logout")
				self.assertEqual(data[0]["event"]["user-id"], 1)

		driver.quit()

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()
