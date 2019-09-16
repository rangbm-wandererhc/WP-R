from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = 'D:\\rangbm.wandererhc\\WMP\\3_WP_ver.2\\chromedriver.exe'
driver=webdriver.Chrome(path)

def parser_wordlisteng(url):
	driver.get(url)
	time.sleep(3)
	words = driver.find_elements_by_css_selector('.word-t') 
	for word in words:
		print('"'+word.get_attribute("innerText")+'",')

def parser_wordlistspa(url):
	driver.get(url)
	time.sleep(3)
	words = driver.find_elements_by_css_selector('.word-e') 
	for word in words:
		print('"'+word.get_attribute("innerText")+'",')

