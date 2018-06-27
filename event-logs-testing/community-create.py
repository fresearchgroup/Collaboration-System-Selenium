import unittest
from selenium import webdriver
import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class test(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.url_basic = "http://localhost:8000/"

	def test_community_create(self):
		url_api = self.url_basic + 'logapi/event/community/create/'
		result = requests.get(url_api).json()
		if (result["status code"] == 200):
			data = result["result"]
			total_hits = result["total hits"]
		
		user ="root"
		pwd= "pass1234"

		comm_name="testing_community"
		comm_tag="this is a tag"
		comm_desc="this is description"
		comm_category="this is category"
		comm_username="root"
		comm_image="/home/bharat/Pictures/hotel_trans.jpeg"


		driver = webdriver.Firefox()
		driver.maximize_window() #For maximizing window
		driver.implicitly_wait(20) #gives an implicit wait for 20 seconds
		driver.get("http://localhost:8000/")
		driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
		driver.get("http://localhost:8000/login/?next=/")
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(pwd)
		driver.find_element_by_class_name('btn-block').click()
		###################
		driver.get("http://localhost:8000/create_community/")
		elem = driver.find_element_by_id("name")
		elem.send_keys(comm_name)

		elem = driver.find_element_by_id("tag_line")
		elem.send_keys(comm_tag)

		elem = driver.find_element_by_id("comm_text_box")
		elem.send_keys(comm_desc)

		elem = driver.find_element_by_id("category")
		elem.send_keys(comm_category)

		elem = driver.find_element_by_id("username")
		elem.send_keys(comm_username)

		elem = driver.find_element_by_id("community_image")
		elem.send_keys(comm_image)

		driver.find_element_by_id("create").click()

		#################

		
		url_api = self.url_basic + 'logapi/event/community/create/'
		result = requests.get(url_api).json()
		if (result["status code"] == 200):
			data = result["result"]
			if (result["total hits"]== total_hits+1):
				self.assertEqual(data[0]["event_name"],"event.community.create")
				self.assertEqual(data[0]["event"]["community-name"], "testing_community")
				self.assertEqual(data[0]["event"]["admin-username"], "root")

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()
