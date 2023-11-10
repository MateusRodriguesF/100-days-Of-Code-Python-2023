from selenium import webdriver
from selenium.webdriver.common.by import By
#------------------------------- Var's ---------------------------------

webpage = "https://www.python.org/"

#------------------------------- Keep Chrome Open --------------------------------
crhome_options = webdriver.ChromeOptions()
crhome_options.add_experimental_option("detach", True)
#------------------------------------------------------------------------------------------------

driver = webdriver.Chrome(options=crhome_options)
driver.get(webpage)
upcoming_events = []
upcoming_events = driver.find_elements(By.CSS_SELECTOR, value='#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li:nth-child(1) > time')

for event in upcoming_events:
    (event.text)

driver.quit()