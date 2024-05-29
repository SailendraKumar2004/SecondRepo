from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


def type_date(driver,ID,date):
    element = driver.find_element(By.ID,ID)
    element.click()
    for _ in range(10):
        element.send_keys(Keys.ARROW_LEFT)
    element.send_keys(date)
   


# ID of date from = ContentPlaceHolder1_txtDateOfRegistrationFrom, date to = ContentPlaceHolder1_txtDateOfRegistrationTo

# date_from=input("enter date from in DDMMYYYY format:")
#ID_from=input("enter ID of the date from text box:")
date_from='12022023' 
ID_from='ContentPlaceHolder1_txtDateOfRegistrationFrom'
# date_to=input("enter date from in DDMMYYYY format:")
date_to='12042023'
#ID_to=input("enter ID of the date to text box:")
ID_to='ContentPlaceHolder1_txtDateOfRegistrationTo'


options = Options()
options.add_experimental_option("detach",True) #by default it closes browser , to make browser stay without closing we adding this option

# Initialize the WebDriver (make sure the path to your WebDriver executable is set)
driver = webdriver.Chrome()

# Open the target website
driver.get("https://citizen.mahapolice.gov.in/Citizen/MH/PublishedFIRs.aspx")


type_date(driver,ID_from,date_from)
type_date(driver,ID_to,date_to)
# unit_dropdown=driver.find_element(By.ID,'ContentPlaceHolder1_ddlDistrict')
# input()
# unit_dropdown.click()   
# input()
# unit_dropdown = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_ddlDistrict'))
# # Select the second option
# input()
# unit_dropdown.select_by_index(1)  # Index starts from 0, so index 1 is the second option
dropdown_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ContentPlaceHolder1_ddlDistrict')))
    
# Click on the dropdown to trigger the options to appear
dropdown_element.click()
    
# Find the dropdown element by its ID
unit_dropdown = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_ddlDistrict'))
time.sleep(10)
# Wait for the options to be visible
WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//select[@id='ContentPlaceHolder1_ddlDistrict']/option")))
time.sleep(10)
# Select the second option
unit_dropdown.select_by_index(1) 

input()

