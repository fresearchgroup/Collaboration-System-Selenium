import unittest
from selenium import webdriver
import requests

class signup(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.url_basic = "http://localhost:8000/"

	def test_group_create(self):
		url_api = self.url_basic + 'logapi/event/group/create/'
		result = requests.get(url_api).json()
		if (result["status code"] == 200):
			data = result["result"]
			total_hits = result["total hits"]
		user ="root"
		pwd= "pass1234"

		grp_name="testing group"
		grp_desc="this is group description"

		driver = webdriver.Firefox()
		driver.maximize_window() #For maximizing window
		#driver.implicitly_wait(20) #gives an implicit wait for 20 seconds
		driver.get("http://localhost:8000/")
		driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(pwd)
		driver.find_element_by_class_name('btn-block').click()
		driver.find_element_by_xpath('//a [@href="/communities/"]').click()
		driver.find_element_by_xpath('//a [@href="/community-view/1/"]').click()

		driver.find_element_by_id("create_resource_id").click()
		driver.find_element_by_id("group_resource_id").click()
		driver.find_element_by_id("exampleCheck1_group").click()
		driver.find_element_by_id("group_yes_id").click()

		elem = driver.find_element_by_id("title")
		elem.send_keys(grp_name)

		elem = driver.find_element_by_id("group_create_textbox_id")
		elem.send_keys(grp_desc)

		driver.find_element_by_id("grp_create").click()		



		url_api = self.url_basic + 'logapi/event/group/create/'
		result = requests.get(url_api).json()
		if (result["status code"] == 200):
			data = result["result"]
			if (result["total hits"]== total_hits+1):
				self.assertEqual(data[0]["event_name"],"event.group.create")
				self.assertEqual(data[0]["event"]["community-id"], '1')
				self.assertEqual(data[0]["event"]["group-name"], "testing group")

		driver.quit()

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()