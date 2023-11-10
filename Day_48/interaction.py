from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

webpage = "http://secure-retreat-92358.herokuapp.com/"

chr_opt = webdriver.ChromeOptions()
chr_opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chr_opt)
driver.get(webpage)

# artc_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# artc_count.click()

# search = driver.find_element(By.ID, value="id-search-field")
# search.send_keys("Pandas")
# subm = driver.find_element(By.ID, value="submit")
# subm.click()
# search.send_key(Keys.ENTER)

# autofill form challenge
first_name_form = driver.find_element(By.NAME, value="fName")
sleep(random.randint(2,5))
first_name_form.send_keys("Mateus",Keys.ENTER)

last_name_form = driver.find_element(By.NAME, value="lName")
sleep(random.randint(2,5))
last_name_form.send_keys("Fonseca",Keys.ENTER)

email_form = driver.find_element(By.NAME, value="email")
sleep(random.randint(2,5))
email_form.send_keys("email@email.com",Keys.ENTER)

sig_btn = driver.find_element(By.CSS_SELECTOR, value='/html/body/form/button')
sig_btn.click()





# driver.quit()