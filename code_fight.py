from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os.path import expanduser
from time import sleep
from time import time

def start_fight():
	my_pass = '*'

	driver = webdriver.Chrome(expanduser(r'~\Dropbox\Work\Python\chromedriver.exe'))
	driver.get('https://codefights.com/')
	driver.implicitly_wait(60)
	driver.maximize_window()

	login_button = driver.find_element_by_xpath("//a[@class='dropdown-toggle']/span[@class='in']")
	email_field = driver.find_element_by_xpath("//input[@name='username_or_email']")
	password_field = driver.find_element_by_xpath("//div/label/input[@name='password']")
	sign_in_button = driver.find_element_by_xpath("//button[@class='btn btn-primary -e-signin btn-block']")

	login_button.click()
	driver.implicitly_wait(5)
	email_field.send_keys('g.mishchevskii@gmail.com')
	password_field.send_keys(my_pass)
	sign_in_button.click()


delay_time = int(input('Input a wait time: '))
current_time = time()

delay_time *= 60
wanted_time = current_time + delay_time

while time() < wanted_time:
	sleep(60)

start_fight()

exit()
