from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options =  webdriver.ChromeOptions()
options.add_argument('--headless')
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


def testBrowser():
    try:
        driver.get('http://localhost:3000/')
        driver.find_element(By.ID,'my-text-id').send_keys('teste')
    except ValueError:
        print(ValueError())

testBrowser()
