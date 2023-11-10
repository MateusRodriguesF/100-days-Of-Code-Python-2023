from selenium import webdriver
from selenium.webdriver.common.by import By

class InternetSpeedBot():
    
    from time import sleep
    def __init__(self):
        self.url = "https://www.speedtest.net/"
        self.chrome_opts = webdriver.ChromeOptions()
        self.chrome_opts.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_opts)
        self.driver.get(self.url)

    def get_internet_speed(self):

        self.acpt_cookie = self.driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.go_btn = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.biln_test_btn = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.download_value = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.upload_value = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.acpt_cookie.click()
        self.go_btn.click()
        self.sleep(45)
        self.biln_test_btn.click()
        print(f"Download: {self.download_value.text}\nUpload: {self.upload_value.text}")
        self.driver.close()



bot_start = InternetSpeedBot()
bot = bot_start.get_internet_speed()

