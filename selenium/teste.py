from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from utils import questions, get_element_by_text, subquestion

from getCredencials import getCredencials

options =  webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument("--window-size=1920,1080")

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

email = getCredencials()['email']
passwd = "toolsmoon"

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

indetifier = driver.find_element(By.ID, 'identifierId')
indetifier.send_keys(email)

next_page = driver.find_element(By.ID, "identifierNext")
next_page.click()

wait.until(EC.staleness_of(indetifier))

identifier_passwd = driver.find_element(By.XPATH , '//*[@id="password"]/div[1]/div/div[1]/input')
identifier_passwd.send_keys('toolsmoon')
driver.find_element(By.ID, 'passwordNext').click()
wait.until(EC.staleness_of(identifier_passwd))

driver.find_element(By.ID, 'confirm').click()

driver.switch_to.window(original_window)

wait.until(EC.title_is('Welcome - Sheetgo'))


get_element_by_text(driver,"p", questions['job_role'])

get_element_by_text(driver, "span","Next")

get_element_by_text(driver, "p" , questions['like_to_do'])

driver.find_element(By.XPATH,"// p[contains(text(),\'Connect data')]").click()

get_element_by_text(driver, "span", subquestion)

get_element_by_text(driver, "span","Next")

get_element_by_text(driver, "p" , questions['spreadsheet'])

get_element_by_text(driver, "span","Next")

get_element_by_text(driver, "p" , questions['challange'])

get_element_by_text(driver, "span","Finish")

wait.until(EC.title_is('My first workflow - Sheetgo'))

wait.until(driver.find_element(By.CSS_SELECTOR, '[title="Close"]'))
print('Teste Concluido!')
    

   
