import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): #test scenario
    

    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_search_in_saucedemo(self): #test case
        driver=self.browser
        driver.get("https://www.saucedemo.com/") 
        time.sleep(1)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('Product', response_data)

    def tearDown(self):
        self.browser.close()
if __name__ == "__main__":
    unittest.main()
