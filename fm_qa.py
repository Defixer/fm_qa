from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import json
import time

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
client_secret = "/Users/crmonlinegraph/Documents/Scripts/fm_secret.json"
timeout = 5

CLASS_NAME = "CLASS_NAME"
CSS_SELECTOR = "CSS_SELECTOR"
ID = "ID"
LINK_TEXT = "LINK_TEXT"
NAME = "NAME"
PARTIAL_LINK_TEXT = "PARTIAL_LINK_TEXT"
TAG_NAME = "TAG_NAME"
XPATH = "XPATH"

def sign_in_creds():	
	with open(client_secret) as json_file:
		data = json.load(json_file)


	username = get_element(XPATH, "//input[@placeholder='User Name']")
	print("Username entered")
	time.sleep(1)
	username.send_keys(data["username"])
	password = get_element(XPATH, "//input[@placeholder='Password']")
	password.send_keys(data["fm_password"])
	print("Password entered")
	time.sleep(1)
	sign_in = get_element(XPATH, "//a[@name='login_button']")
	sign_in.click()
	print("Sign In clicked")
	tutorial_done = get_element(XPATH, "//span[contains(text(),'Done')]")
	# tutorial_done = browser.find_element_by_xpath("//span[contains(text(),'Done')]")
	tutorial_done.click()
	print("Tutorial: Done clicked")

def create_job():	
	browser.get("https://uat.fieldmagic.co")
	sign_in_creds()
	jobs_module = get_element(XPATH, "//a[@class='btn btn-invisible btn-link module-name'][contains(text(),'Jobs')]")
	jobs_module.click()
	print("Jobs module clicked")
	time.sleep(1)
	jobs_create = get_element(XPATH, "//a[@name='create_button']")
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
	customer = get_element(XPATH, "/html[1]/body[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/div[1]/a[1]/span[1]")
	customer.click()
	print("Customer clicked")
	time.sleep(1)
	select_customer = get_element(XPATH, "/html[1]/body[1]/div[6]/div[1]/input[1]")
	select_customer.send_keys("James Kilroy")
	print("Customer searched")
	time.sleep(1)
	chosen_customer = get_element(XPATH, "/html[1]/body[1]/div[6]/ul[1]/li[1]/div[1]/span[1]")
	chosen_customer.click()
	print("Customer chosen")
	time.sleep(1)

def select_site():
	site = get_element(XPATH, "/html[1]/body[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/span[1]/div[1]/a[1]/span[1]")
	site.click()
	print("Site clicked")
	time.sleep(1)
	select_site = get_element(XPATH, "/html[1]/body[1]/div[7]/div[1]/input[1]")
	select_site.send_keys("Pheasant")
	print("Site searched")
	time.sleep(1)
	chosen_site = get_element(XPATH, "/html[1]/body[1]/div[7]/ul[1]/li[1]/div[1]")
	chosen_site.click()
	print("Site chosen")
	time.sleep(1)
	confirm_overwrite = get_element(XPATH, "//a[@class='span6 alert-btn-confirm']")
	confirm_overwrite.click()
	print("Confirm overwrite clicked")
	time.sleep(1)

def select_department():
	department = get_element(XPATH, "/html[1]/body[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/span[1]/div[1]/a[1]/span[1]")
	department.click()
	print("Department clicked")
	time.sleep(1)	
	chosen_department = get_element(XPATH, "//div[@id='select2-result-label-38']")
	chosen_department.click()
	print("Department chosen")
	time.sleep(1)

def select_type():
	my_type = get_element(XPATH, "/html[1]/body[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/span[1]/span[1]/div[1]/a[1]/span[1]")
	my_type.click()
	print("Type clicked")
	time.sleep(1)	
	chosen_my_type = get_element(XPATH, "//div[@id='select2-result-label-44']")
	chosen_my_type.click()
	print("Type chosen")
	time.sleep(1)

def set_due_date():
	due_date = get_element(XPATH, "//input[@placeholder='(Required) mm/dd/yyyy']")
	due_date.click()
	due_date.send_keys("08/28/2018")
	due_date.send_keys(Keys.RETURN)
	print("Type clicked")
	time.sleep(1)	

def is_billable():
	billable = get_element(XPATH, "/html[1]/body[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[8]/div[1]/span[1]/span[1]/div[1]/a[1]/span[1]")
	billable.click()
	print("Billable clicked")
	time.sleep(1)	
	chosen_billable = get_element(XPATH, "//div[@id='select2-result-label-52']") #52 = Yes, 53 = No
	chosen_billable.click()
	print("Billable chosen")
	time.sleep(1)

def set_job_summary():	
	job_info_tab = get_element(XPATH, "//li[@class='tab panel_hidden']//a[@href='#panel_hiddenview279'][contains(text(),'Job Info')]")
	job_info_tab.click()
	print("Job Info Tab clicked")
	time.sleep(1)
	job_summary = get_element(XPATH, "//div[@class='row-fluid panel_body panel_hidden']//input[@placeholder='Required']")
	job_summary.send_keys("TBD")
	print("Job Summary set")
	time.sleep(1)

def add_job_by_site():	
	sites_module = get_element(XPATH, "//a[@class='btn btn-invisible btn-link module-name'][contains(text(),'Sites')]")
	sites_module.click()
	print("Sites module clicked")
	time.sleep(1)
	sites_search = get_element(XPATH, "//input[@placeholder='Search by site name (auto-generated)...']")
	sites_search.send_keys("50968")
	print("Site searched")
	time.sleep(1)
	this_site = get_element(PARTIAL_LINK_TEXT, "50968")
	this_site.click()
	print("Site clicked")
	time.sleep(1)
	manage_maintenance = get_element(XPATH, "//a[@class='manage-maintenance']")
	manage_maintenance.click()
	print("Manage maintenance clicked")
	time.sleep(1)
	period = get_element(XPATH, "//span[@id='select2-chosen-8']")
	period.click()
	print("Period clicked")
	time.sleep(1)
	period_choice = get_element(XPATH, "//div[@id='select2-result-label-138']")
	period_choice.click()
	print("Period chosen")
	time.sleep(1)
	department = get_element(XPATH, "//span[@id='select2-chosen-10']")
	department.click()
	print("Department clicked")
	time.sleep(1)
	department_choice = get_element(XPATH, "//div[@id='select2-result-label-153']")
	department_choice.click()
	print("Department chosen")
	time.sleep(1)
	billable_amount = get_element(XPATH, "//tbody//tr[1]//td[4]//input[1]")
	billable_amount.send_keys(Keys.BACKSPACE)
	billable_amount.send_keys(Keys.BACKSPACE)
	billable_amount.send_keys(Keys.BACKSPACE)
	billable_amount.send_keys(Keys.BACKSPACE)
	billable_amount.send_keys("1500")
	print("Billable amount inputted")
	time.sleep(1)
	billable_checkbox = get_element(XPATH, "//tbody//tr[1]//td[6]//input[1]")
	billable_checkbox.click()
	billable_checkbox.click()
	print("Billable checked")
	time.sleep(1)
	next_job_date = get_element(XPATH, "//tbody//tr[1]//td[8]//input[1]")
	next_job_date.send_keys("08/29/2018")
	next_job_date.send_keys(Keys.RETURN)
	print("Next Job Date inputted")
	time.sleep(1)
	expiry_date = get_element(XPATH, "//tbody//tr[1]//td[9]//input[1]")
	expiry_date.send_keys("09/16/2018")
	expiry_date.send_keys(Keys.RETURN)
	print("Expiry Date inputted")
	time.sleep(1)
	add_more = get_element(XPATH, "//tbody//tr[1]//td[10]//a[1]//i[1]")
	add_more.click()
	print("Add [more] button clicked")
	time.sleep(1)

	period = get_element(XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/a[1]/span[1]")
	period.click()
	print("Period clicked")
	time.sleep(1)
	period_choice = get_element(XPATH, "//div[@id='select2-result-label-164']")
	period_choice.click()
	print("Period chosen")
	time.sleep(1)
	department = get_element(XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/a[1]/span[1]")
	department.click()
	print("Department clicked")
	time.sleep(1)
	department_choice = get_element(XPATH, "//div[@id='select2-result-label-178']")
	department_choice.click()
	print("Department chosen")
	billable_amount = get_element(XPATH, "//tbody//tr[2]//td[4]//input[1]")
	billable_amount.send_keys(Keys.BACKSPACE)
	billable_amount.send_keys(Keys.BACKSPACE)
	billable_amount.send_keys(Keys.BACKSPACE)
	billable_amount.send_keys(Keys.BACKSPACE)
	billable_amount.send_keys("2700")
	print("Billable amount inputted")
	time.sleep(1)
	billable_checkbox = get_element(XPATH, "//tbody//tr[2]//td[6]//input[1]")
	billable_checkbox.click()
	billable_checkbox.click()
	print("Billable checked")
	time.sleep(1)
	next_job_date = get_element(XPATH, "//tbody//tr[2]//td[8]//input[1]")
	next_job_date.send_keys("08/29/2018")
	next_job_date.send_keys(Keys.RETURN)
	print("Next Job Date inputted")
	time.sleep(1)
	expiry_date = get_element(XPATH, "//tbody//tr[2]//td[9]//input[1]")
	expiry_date.send_keys("09/16/2018")
	expiry_date.send_keys(Keys.RETURN)
	print("Expiry Date inputted")
	time.sleep(1)

	save_site = get_element(CLASS_NAME, "save-maintenance")
	save_site.click()
	print("Maintenance saved")
	time.sleep(1)

def generate_scheduled_jobs():
	browser.get("https://uat.fieldmagic.co/#Home/layout/generatescheduledjobs")
	site_search = get_element(XPATH, "//input[@id='s2id_autogen183']")
	site_search.send_keys("50968")
	print("Site searched")
	this_site = get_element(CLASS_NAME, "select2-result-label")
	this_site.click()
	print("Site clicked")
	time.sleep(5)
	job1 = get_element(XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/table[1]/tbody[2]/tr[3]/td[1]/input[1]")
	job1.click()
	print("Job 2 Checked")
	time.sleep(1)
	generate_jobs = get_element(ID, "generate-jobs")
	generate_jobs.click()
	print("Generate Jobs clicked")
	time.sleep(1)
	browser.get("https://uat.fieldmagic.co/#job_jobs")

def save_job():
	save = get_element(XPATH, "//a[@name='save_button']")
	save.click()
	print("Job saved")
	time.sleep(1)

def get_element(element_type, element_string):
	i = 0
	while True:
		try:
			element = check_element_type(element_type, element_string)
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

def check_element_type(element_type, element_string):
	if element_type == CLASS_NAME:
		return WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, element_string)))
	elif element_type == CSS_SELECTOR:
		return WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_string)))
	elif element_type == ID:
		return WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.ID, element_string)))
	elif element_type == LINK_TEXT:
		return WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.LINK_TEXT, element_string)))
	elif element_type == NAME:
		return WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.NAME, element_string)))
	elif element_type == PARTIAL_LINK_TEXT:
		return WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, element_string)))
	elif element_type == TAG_NAME:
		return WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.TAG_NAME, element_string)))
	elif element_type == XPATH:
		return WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.XPATH, element_string)))

def press_any_key():
	input("Press any key...")
	browser.quit()

def myMain():	
	browser.get("https://uat.fieldmagic.co")
	sign_in_creds()
	# create_job()
	add_job_by_site()
	generate_scheduled_jobs()
	press_any_key()

myMain()