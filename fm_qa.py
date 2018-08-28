from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import json
import time

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
client_secret = "/Users/crmonlinegraph/Documents/Scripts/fm_secret.json"
timeout = 5

def sign_in_creds():	
	with open(client_secret) as json_file:
		data = json.load(json_file)


	username = get_element("//input[@placeholder='User Name']")
	print("Username entered")
	time.sleep(1)
	username.send_keys(data["username"])
	password = get_element("//input[@placeholder='Password']")
	password.send_keys(data["fm_password"])
	print("Password entered")
	time.sleep(1)
	sign_in = get_element("//a[@name='login_button']")
	sign_in.click()
	print("Sign In clicked")
	tutorial_done = get_element("//span[contains(text(),'Done')]")
	# tutorial_done = browser.find_element_by_xpath("//span[contains(text(),'Done')]")
	tutorial_done.click()
	print("Tutorial: Done clicked")

def create_job():	
	jobs_module = get_element("//a[@class='btn btn-invisible btn-link module-name'][contains(text(),'Jobs')]")
	jobs_module.click()
	print("Jobs module clicked")
	time.sleep(1)
	jobs_create = get_element("//a[@name='create_button']")
	jobs_create.click()
	print("Create job clicked")
	time.sleep(1)
	select_customer()
	select_site()
	select_department()
	select_type()
	set_due_date()
	is_billable()
	# save_job()
	set_job_summary()
	save_job()

def select_customer():
	customer = get_element("/html[1]/body[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/div[1]/a[1]/span[1]")
	customer.click()
	print("Customer clicked")
	time.sleep(1)
	select_customer = get_element("/html[1]/body[1]/div[6]/div[1]/input[1]")
	select_customer.send_keys("James Kilroy")
	print("Customer searched")
	time.sleep(1)
	chosen_customer = get_element("/html[1]/body[1]/div[6]/ul[1]/li[1]/div[1]/span[1]")
	chosen_customer.click()
	print("Customer chosen")
	time.sleep(1)

def select_site():
	site = get_element("/html[1]/body[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/span[1]/div[1]/a[1]/span[1]")
	site.click()
	print("Site clicked")
	time.sleep(1)
	select_site = get_element("/html[1]/body[1]/div[7]/div[1]/input[1]")
	select_site.send_keys("Pheasant")
	print("Site searched")
	time.sleep(1)
	chosen_site = get_element("/html[1]/body[1]/div[7]/ul[1]/li[1]/div[1]")
	chosen_site.click()
	print("Site chosen")
	time.sleep(1)
	confirm_overwrite = get_element("//a[@class='span6 alert-btn-confirm']")
	confirm_overwrite.click()
	print("Confirm overwrite clicked")
	time.sleep(1)

def select_department():
	department = get_element("/html[1]/body[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/span[1]/div[1]/a[1]/span[1]")
	department.click()
	print("Department clicked")
	time.sleep(1)	
	chosen_department = get_element("//div[@id='select2-result-label-38']")
	chosen_department.click()
	print("Department chosen")
	time.sleep(1)

def select_type():
	my_type = get_element("/html[1]/body[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/span[1]/span[1]/div[1]/a[1]/span[1]")
	my_type.click()
	print("Type clicked")
	time.sleep(1)	
	chosen_my_type = get_element("//div[@id='select2-result-label-44']")
	chosen_my_type.click()
	print("Type chosen")
	time.sleep(1)

def set_due_date():
	due_date = get_element("//input[@placeholder='(Required) mm/dd/yyyy']")
	due_date.click()
	due_date.send_keys("08/28/2018")
	due_date.send_keys(Keys.RETURN)
	print("Type clicked")
	time.sleep(1)	

def is_billable():
	billable = get_element("/html[1]/body[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[8]/div[1]/span[1]/span[1]/div[1]/a[1]/span[1]")
	billable.click()
	print("Billable clicked")
	time.sleep(1)	
	chosen_billable = get_element("//div[@id='select2-result-label-52']") #52 = Yes, 53 = No
	chosen_billable.click()
	print("Billable chosen")
	time.sleep(1)

def set_job_summary():	
	job_info_tab = get_element("//li[@class='tab panel_hidden']//a[@href='#panel_hiddenview279'][contains(text(),'Job Info')]")
	job_info_tab.click()
	print("Job Info Tab clicked")
	time.sleep(1)
	job_summary = get_element("//div[@class='row-fluid panel_body panel_hidden']//input[@placeholder='Required']")
	job_summary.send_keys("TBD")
	print("Job Summary set")
	time.sleep(1)

def save_job():
	save = get_element("//a[@name='save_button']")
	save.click()
	print("Job saved")
	time.sleep(1)

def get_element(element_xpath):
	i = 0
	while True:
		try:
			element = WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.XPATH, element_xpath)))
			print("Element fetched: {}".format(element.text))
			return element
			break
		except TimeoutException:
			if i > 5:
				print("Loading took too much time! Check network connection")
				press_any_key()
			else:
				print("Retrying ({})".format(i))
			i+=1

def press_any_key():
	input("Press any key...")
	browser.quit()

def myMain():
	browser.get("https://uat.fieldmagic.co")
	sign_in_creds()
	create_job()
	press_any_key()

try:
	myMain()
except:
	press_any_key()