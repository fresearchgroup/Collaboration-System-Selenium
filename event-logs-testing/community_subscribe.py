import unittest
from selenium import webdriver
import requests

class test(unittest.TestCase):

	def setUp(self):
		self.user = raw_input("Enter username: ")
		self.pwd = raw_input("Enter password: ")
		print("Note that user should not be a part of community: ")
		self.comm_id = raw_input("Enter id of community which the user will join: ")
		self.url_basic = "http://localhost:8000/"
		self.EVENT_API_TOKEN = 'e1eebb20fd4f01d6f733cc6d355b45e9fb1ed78d' #This should be generated by tester
		self.headers = {'Authorization': 'Token ' + str(self.EVENT_API_TOKEN)}

	def test_community_subscribe(self):

		url_api = self.url_basic + 'logapi/event/community/subscribe/' + self.comm_id + '/'

		result = requests.get(url_api, headers = self.headers).json()
		new_result={}
		for key,value in result.iteritems():
			new_result[key.lower()] = value
		if(new_result["status code"] == 200):
			data = new_result["result"]
			total_hits = new_result["total hits"]

		driver = webdriver.Firefox()
		driver.maximize_window() #For maximizing window
		driver.get("http://localhost:8000/")
		driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
		driver.get("http://localhost:8000/login/?next=/")
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(self.user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(self.pwd)
		driver.find_element_by_class_name('btn-block').click()
		driver.find_element_by_xpath('//a [@href="/communities/"]').click()
		driver.find_element_by_xpath('//a [@href="/community-view/'+ self.comm_id +'/"]').click()
		driver.find_element_by_id("join-us").click()
		url_api = self.url_basic + 'logapi/event/community/subscribe/' + self.comm_id + '/'
		result = requests.get(url_api, headers = self.headers).json()

		new_result={}
		for key,value in result.iteritems():
			new_result[key.lower()] = value

		if (new_result["status code"] == 200):
			data = new_result["result"]
			if (new_result["total hits"]== total_hits+1):
				self.assertEqual(data[0]["event_name"],"event.community.subscribe")
				self.assertEqual(data[0]["event"]["community-id"], self.comm_id)
			else:
				self.assertFalse(True)

		driver.quit()

if __name__ == '__main__':
	unittest.main()
