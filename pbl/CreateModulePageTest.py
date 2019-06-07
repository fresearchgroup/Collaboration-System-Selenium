__author__ = 'aadarshsingh'

import unittest
import argparse
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException , TimeoutException, NoSuchElementException, StaleElementReferenceException
# from selenium.common.exceptions import TimeoutException
import random
import string
from decouple import config

IP = config('IP_ADDRESS')
PORT = config('PBLCLIENT_PORT')


class LoginCorrect(unittest.TestCase):

       

	def setUp(self):

	   user = "aadarshsingh191198"
	   pwd= "root1234"
	   # self.driver = webdriver.Remote(command_executor='http://10.196.24.237:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX) 
	   self.driver = webdriver.Firefox() 
	   self.driver.maximize_window()
	   self.driver.get("http://"+IP+":"+PORT+"/login")
	   elem = self.driver.find_element_by_id("username")
	   elem.send_keys(user)
	   elem = self.driver.find_element_by_id("password")
	   elem.send_keys(pwd)
	   elem = self.driver.find_element_by_name("user_type")
	   elem.click()
	   elem = self.driver.find_element_by_id("sign_in_btn")
	   elem.click()


	   self.driver.implicitly_wait(10)
	   # time.sleep(10)
	   self.driver.find_elements_by_css_selector("#headerMenuCollapse li.nav-item>a")[3].click()

	   elem = self.driver.find_element_by_id("project_title")
	   title = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
	   elem.send_keys(title)
	   elem = self.driver.find_element_by_id("project_description")
	   elem.send_keys("Something1")
	   self.driver.find_element_by_id("save_and_redirect_btn").click()

	   self.driver.implicitly_wait(10)

	def test_AddRemove(self):
	   
	   fields = self.driver.find_elements_by_css_selector("table>tbody>tr")[0].find_elements_by_tag_name("textarea")
	   module_title = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
	   fields[0].send_keys(module_title)
	   module_desc = ''.join(random.choice(string.ascii_lowercase) for _ in range(20))
	   fields[1].send_keys(module_desc)
	   
	   #extra modules to be added

	   no=6
	   

	   for i in range(no):
		self.driver.find_element_by_id("add_new_module").click()
		try:
			field = self.driver.find_elements_by_css_selector("table>tbody>tr")[i+1].find_elements_by_tag_name("textarea")
			module_title = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
			field[0].send_keys(module_title)
			module_desc = ''.join(random.choice(string.ascii_lowercase) for _ in range(20))
			field[1].send_keys(module_desc)

		except:
			print ("row not added")
			self.fail("Add button does not add row.")
		# boxes = self.driver.find_elements_by_css_selector("table>tbody>tr")
		# if len(boxes) != i + 2:
			
		# 	print("Row not added")

	   # boxes = self.driver.find_elements_by_css_selector("table>tbody>tr")

	 #   if len(boxes) == no+1:
		# print ("All rows added Successfully") 
	   for i in range(no):
		self.driver.find_element_by_id("remove_last_module").click()
		boxes = self.driver.find_elements_by_css_selector("table>tbody>tr")
		length = len(boxes)
		if length != no -i :
			self.assertFalse(boxes[i].is_displayed(), "Remove button did not work")
			# print("Box not removed",i)
		# else:
			# print("Box removed")


	   if len(boxes)==1:
		self.driver.find_element_by_id("remove_last_module").click()
		try:
			self.assertTrue(boxes[0].is_displayed(),"Last button not removed")
		except StaleElementReferenceException:
			self.fail("Last box removed.")


	   self.driver.quit()

	def test_EmptyModule(self):
	
	   self.driver.find_element_by_id("submit_project").click() 

	   try:
			#switch control to the alert box,by creating a alert object
			alert = self.driver.switch_to_alert()
			self.alert_wait()
			#accept the alert
			alert.accept()
	   except NoAlertPresentException:
			self.fail("No alert found")   


	   
	   self.driver.quit()


	def test_SaveModule(self):
	   

	   fields = self.driver.find_elements_by_css_selector("table>tbody>tr")[0].find_elements_by_tag_name("textarea")
	   module_title = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
	   fields[0].send_keys(module_title)
	   module_desc = ''.join(random.choice(string.ascii_lowercase) for _ in range(20))
	   fields[1].send_keys(module_desc)
	   
	   self.driver.find_element_by_id("submit_project").click() 
	   try:
		WebDriverWait(self.driver, 10).until(EC.alert_is_present())
		alert = self.driver.switch_to.alert
		self.assertEqual("{\"msg\": \"Project Successfully Added\", \"status\": \"true\"}", alert.text)
		alert.accept()
		# print("Successfully submitted")
	   except TimeoutException:
		self.fail("No alert")

	   
	   self.driver.quit()


	def tearDown(self):
	   self.driver.quit()


if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='My program.')
	parser.add_argument('-u', '--username', type=str)
	parser.add_argument('-p', '--password', type=str)

	args = parser.parse_args()

	unittest.main()

