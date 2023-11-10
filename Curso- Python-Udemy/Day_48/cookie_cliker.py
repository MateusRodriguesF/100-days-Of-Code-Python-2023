from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from replit import clear

# ----------------------var------------------------------
url = "https://orteil.dashnet.org/experiments/cookie/"

# ----------------------settings keep chrome open------------------------------
chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option("detach", True)

# ----------------------driver settings ------------------------------
driver = webdriver.Chrome(options=chrome_opt)
driver.get(url)

# ----------------------bot settings-----------------------------

# cookie = driver.find_element(By.ID, value="cookie")
# cookie.click()
# sleep(1)

# money = driver.find_element(By.ID, value="money").text
# money_conv = int(money)


upgrades = driver.find_elements(By.CSS_SELECTOR, value="#store b")

for upgrade in upgrades:
    upgrade_str = upgrade.text
    upgrade_list = ' '.join(upgrade_str.split()[2:]) # remove the first two words from the string)

