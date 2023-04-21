from selenium.webdriver.common.by import By


questions = {"job_role": ['CEO','C-Level','Director','Manager','Analyst','Intern','Student'], 
"like_to_do": ['Create and publish forms','Start from a template','Generate documents'],
"spreadsheet":['Beginner','Basic','Advanced','Expert'],
"challange": ['Copying and pasting','Unorganised spreadsheets','Inefficient system','Collaboration','Other']
}

subquestion = ['Google Sheets','Excel','CSV','TSV','BigQuery']


def get_element_by_text(driver,tag_name,text):

	is_string = type(text) is str

	if is_string == True:
		driver.find_element(By.XPATH,f"// {tag_name}[contains(text(),\'{text}')]").click()
	else:
		for value in text:
			driver.find_element(By.XPATH,f"// {tag_name}[contains(text(),\'{value}')]").click()
