from selenium import webdriver
from selenium.webdriver.common.by import By # to find elements in the webpage

#------------------------------- Var's ---------------------------------
# webpage = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
webpage = "https://python.org"
#------------------------------------------------------------------------------------------------------------------------
#Keep Chrome open 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
#--------------------------------------------------------

driver = webdriver.Chrome(options=chrome_options)
driver.get(webpage)

# price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# print(f"The Price is: {price.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
print(button.size)
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)
# driver.close()
driver.quit()