from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumwire import webdriver as wire
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from utils import questions, get_element_by_text, subquestion
from selenium.webdriver import ActionChains

from getCredencials import getCredencials

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument("--window-size=1920,1080")

driver_wire = wire.Chrome()
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

email = getCredencials()['email']
passwd = "toolsmoon"

driver.get('https://app.sheetgo.com')

wait = WebDriverWait(driver, 10)
original_window = driver.current_window_handle

assert len(driver.window_handles) == 1

driver.find_element(By.ID, 'google-login').click()

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

identifier_passwd = driver.find_element(
    By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
identifier_passwd.send_keys('toolsmoon')
driver.find_element(By.ID, 'passwordNext').click()
wait.until(EC.staleness_of(identifier_passwd))

driver.find_element(By.ID, 'confirm').click()

driver.switch_to.window(original_window)

wait.until(EC.title_is('Welcome - Sheetgo'))


get_element_by_text(driver, "p", questions['job_role'])

get_element_by_text(driver, "span", "Next")

get_element_by_text(driver, "p", questions['like_to_do'])

driver.find_element(By.XPATH, "// p[contains(text(),\'Connect data')]").click()

get_element_by_text(driver, "span", subquestion)

get_element_by_text(driver, "span", "Next")

get_element_by_text(driver, "p", questions['spreadsheet'])

get_element_by_text(driver, "span", "Next")

get_element_by_text(driver, "p", questions['challange'])

get_element_by_text(driver, "span", "Finish")

wait.until(EC.title_is('My first workflow - Sheetgo'))


driver.implicitly_wait(30)

driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[1]/button').click()

div = driver.find_element(
    By.XPATH, '//*[@id="workflowPageWrapper"]/div/div/div[2]/div[2]/div[1]/div/div[1]').click()

get_element_by_text(driver, "h6", "Sheet file(s)")





driver.find_element(By.CSS_SELECTOR, '[value="No file selected"]').click()

assert len(driver.window_handles) == 1


original_window = driver.current_window_handle

assert len(driver.window_handles) == 1
driver.find_element(By.ID, 'google-oauth').click()

wait.until(EC.number_of_windows_to_be(2))

for window_handle in driver.window_handles:
    if window_handle != original_window:
        print('entrou na segunda janela')
        driver.switch_to.window(window_handle)
        break

get_element_by_text(driver, "div", email)

driver.implicitly_wait(50)

driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section[1]/div/div/div/div[1]/div[1]/div/div[3]/div/input').click()

driver.find_element(By.ID, 'submit_approve_access').click()

driver.switch_to.window(original_window)


driver.find_element(By.CSS_SELECTOR, '[data-id="team-drives"]').click()

folder = driver.find_element(By.XPATH, "// p[contains(text(),\'Sheetgo Files')]")

ActionChains(driver).double_click(folder).perform()

get_element_by_text(driver, "p", "File Teste")

redux = driver.get_cookie("REQUEST_FILE_TABS")

print(redux)

# driver_wire.wait_for_request("https://api.sheetgo.com/drive/sheets/**/tabs")


# driver.find_element(By.XPATH, '//*[@id="connection-builder"]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div/ul/li[4]/div[2]/div[1]/div/div/div[2]/button').click()



# get_element_by_text(driver, "span", "Source Tab")

# print('Teste Concluido!')
