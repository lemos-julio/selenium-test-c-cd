from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC

# from getCredencials import getCredencials

options =  webdriver.ChromeOptions()
options.add_argument('--headless')
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

email = "user-sheetgo-153@gedu-demo-sheetgo.com"
passwd = "toolsmoon"


def testBrowser():
    try:
        driver.get('https://app.sheetgo.com')
        
        wait = WebDriverWait(driver, 10)
        original_window = driver.current_window_handle

        assert len(driver.window_handles) == 1

        driver.find_element(By.ID,'google-login').click()

        wait.until(EC.number_of_windows_to_be(2))

        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        
        wait.until(EC.title_is("Fazer login nas Contas do Google"))
        driver.find_element(By.ID, 'identifierId').send_keys(email)
        driver.find_element(By.ID, "identifierNext").click()
        driver.find_element(By.NAME, 'password').send_keys("toolsmoon")
        
        
        print('Teste Concluido!')
        
    except ValueError:
        print(ValueError())

testBrowser()
