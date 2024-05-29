
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException,NoSuchElementException
from selenium.common.exceptions import TimeoutException
import os
import pyautogui
import pytesseract
from PIL import Image
from io import BytesIO
import re
from selenium.webdriver.common.action_chains import ActionChains

def initialize_driver():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    download_dir = os.path.abspath("D:\\all files\\Academics And Skills\\B.TECH\\2ND Year\\internship at IIIT H\\downloaded files for testing\\high court")
    chrome_prefs = {"download.default_directory": download_dir}
    chrome_options.add_experimental_option("prefs", chrome_prefs)

    # Initialize the Chrome driver with the configured options
    driver = webdriver.Chrome(options=chrome_options)
    return driver
def solve_captcha_25(driver):
    # Find the captcha image element
    captcha_element = driver.find_element(By.ID,'captcha_image')
    # Get the location and dimensions of the captcha image
    location = captcha_element.location
    print(location)
    size = captcha_element.size
    print(size)
    # Take a screenshot of the webpage
    driver.save_screenshot('screenshot.png')
    # Crop the screenshot to get only the captcha image
    captcha_image = Image.open('screenshot.png')
    # captcha_image.show()
    # left = location['x']
    # print(left)
    # top = location['y']
    # print(top)
    # right = location['x'] + size['width']
    # print(right)
    # bottom = location['y'] + size['height']
    # print(bottom)
    # captcha_image = captcha_image.crop((left, top, right, bottom))
    # captcha_image.show()
    # Use Pytesseract to extract text from the captcha image
    captcha_text = pytesseract.image_to_string(captcha_image)
    captcha_number=re.findall(r'\b\d{6}\b', captcha_text)
    return captcha_number
def solve_captcha(driver):
    time.sleep(3)
    # Find the captcha image element
    captcha_element = driver.find_element(By.ID,'captcha_image')
    # Get the location and dimensions of the captcha image
    location = captcha_element.location
    print(location)
    size = captcha_element.size
    print(size)
    # Take a screenshot of the webpage
    driver.save_screenshot('screenshot.png')
    # Crop the screenshot to get only the captcha image
    captcha_image = Image.open('screenshot.png')
    # captcha_image.show()
    # left = location['x']
    # print(left)
    # top = location['y']
    # print(top)
    # right = location['x'] + size['width']
    # print(right)
    # bottom = location['y'] + size['height']
    # print(bottom)
    # captcha_image = captcha_image.crop((left, top, right, bottom))
    # captcha_image.show()
    # Use Pytesseract to extract text from the captcha image
    captcha_text = pytesseract.image_to_string(captcha_image)
    captcha_number=re.findall(r'\b\d{6}\b', captcha_text)
    return captcha_number
'''def handle_captcha_popup(driver):
    try:
        # Debugging: Print page source to understand the HTML structure
        print(driver.page_source)
        
        # Try to locate the popup using different strategies
        popup = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.modal-content')))
        close_button = popup.find_element(By.CSS_SELECTOR, '.btn-close')
        close_button.click()
        print("Invalid Captcha, retrying...")
        return True
    except TimeoutException:
        return False'''
'''def handle_captcha_popup(driver):
    try:
        # Wait for the popup to appear
        popup = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.modal-content')))

        # Ensure the popup is fully visible before clicking
        WebDriverWait(driver, 5).until(EC.visibility_of(popup))
        
        # Scroll to the popup element to ensure it's in view
        ActionChains(driver).move_to_element(popup).perform()

        # Click on the popup to shift focus
        popup.click()
        
        # Find the close button within the popup
        close_button = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-close')))
        
        # Click the close button to dismiss the popup
        close_button.click()
        
        print("Popup closed successfully")
        return True
    except TimeoutException:
        # Popup did not appear within the timeout
        print("Popup did not appear within the timeout")
        return False'''

def handle_captcha_popup(driver):
    try:
        # Wait for the popup to appear
        popup = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.modal-content')))
        
        # Execute JavaScript to click on the popup
        driver.execute_script("arguments[0].click();", popup)
        
        # Find the close button within the popup
        close_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-close')))
        
        # Click the close button to dismiss the popup
        close_button.click()
        
        print("Popup closed successfully")
        return True
    except TimeoutException:
        # Popup did not appear within the timeout
        print("Popup did not appear within the timeout")
        return False

def main_process(driver):
    # Open the target website
    driver.get("https://judgments.ecourts.gov.in/pdfsearch/?p=pdf_search/index&escr_flag=&app_token=15d87ad1e90efad3d1360349ff183d7ba7999b82270b80e215c09276066de92d")
    driver.maximize_window()
    dropdown_locator = (By.ID, 'fcourt_type')
    safe_click(driver, dropdown_locator)

    # Find the dropdown element by its ID and wait for options to be visible
    type_dropdown = Select(driver.find_element(By.ID, 'fcourt_type'))
    WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//select[@id='fcourt_type']/option")))
    type_dropdown.select_by_index(1)
    while True:
        captcha_text = solve_captcha(driver)
        element = driver.find_element(By.ID, 'captcha')
        element.click()
        # captcha = input("Enter captcha by seeing browser: ")
    
        #captcha_text=985432
        print("Captcha text:", captcha_text)
        element.send_keys(captcha_text)
        # Execute JavaScript to set the value of the captcha input field
        # driver.execute_script("arguments[0].value = arguments[1];", element, captcha_text)
        
        search_locator = (By.ID, 'main_search')
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(search_locator))
        element = driver.find_element(*search_locator)
        element.click()
        time.sleep(10)
                # Check if captcha is incorrect
        if handle_captcha_popup(driver):
            time.sleep(2)
            continue
        else:
            break

def safe_click(driver, locator, retries=5):
    for i in range(retries):
        try:
            element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(locator))
            element.click()
            alert_flag = False
            # Check if the alert is present
            if EC.alert_is_present()(driver):
                # Switch to the alert and accept it (click OK button)
                alert = driver.switch_to.alert
                alert.accept()
                print("No files found alert handled")
                alert_flag = True
                return alert_flag
            break   
        except (StaleElementReferenceException, ElementClickInterceptedException, TimeoutException):
            if i < retries - 1:
                time.sleep(1)
                print(f"Retrying click on element {locator}. Attempt {i + 2}/{retries}")
                continue
            else:
                print(f"Failed to click element {locator} after {retries} attempts.")
                raise
    return alert_flag
def perform_download(driver, click_locator, download_button_x, download_button_y, save_button_x, save_button_y):
    retries = 5
    for _ in range(retries):
        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located(click_locator))
            click_element = driver.find_element(*click_locator)
            body = driver.find_element(By.TAG_NAME, 'body')
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            # Wait for the overlay to disappear
            WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'overlay-class')))
            safe_click(driver, click_locator)
            time.sleep(5)

            # Debugging: Print current URL to verify the new tab is correct
            print("Current URL:", driver.current_url)
            time.sleep(17)  # wait a moment to ensure the page is fully loaded change to 10 after testing
            pyautogui.moveTo(download_button_x, download_button_y)
            pyautogui.click()
            print(f"Clicked at coordinates ({download_button_x}, {download_button_y})")

            time.sleep(10)  # wait a moment to ensure the page is fully loaded change to 10
            pyautogui.moveTo(save_button_x, save_button_y)
            pyautogui.click()
            print(f"Clicked at coordinates ({save_button_x}, {save_button_y})")

            time.sleep(2)

            # Wait for the close button to be clickable
            close_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "modal_close")))

            # Click the button
            close_button.click()

            break  # Exit the loop if the download is successful
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error occurred during download attempt: {e}. Retrying...")
            time.sleep(1)
    else:
        print("Download failed after multiple retries.")

'''def perform_download(driver, click_locator, download_button_x, download_button_y, save_button_x, save_button_y):
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(click_locator))
    click_element = driver.find_element(*click_locator)
    # Get the updated location of the element
    #click_location = click_element.location_once_scrolled_into_view
    # Scroll to the element to ensure it's in view
    # driver.execute_script("window.scrollTo(0, arguments[0]);", click_location['y'] - 1000)
    # Scroll to the element to ensure it's in view
    # driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", click_element)
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    # Wait for the overlay to disappear
    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'overlay-class')))
    
    # Wait for the element to be clickable
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(click_locator))
    
    # Click the element
    # click_element.click()
    safe_click(driver, click_locator)
    # Wait for the element to be clickable
    #for attempt in range(5):
        #try:
            #WebDriverWait(driver, 20).until(EC.element_to_be_clickable(click_locator))
            #click_element.click()
            #break
        #except ElementClickInterceptedException:
            #print(f"Element {click_locator} not clickable. Attempt {attempt + 1}") 
            #driver.execute_script("window.scrollBy(0, -200);")
            #time.sleep(1)
        #except TimeoutException:
            #print(f"Element {click_locator} could not be clicked. Retrying...")
            #time.sleep(1)
    
    time.sleep(5)

    # Switch to the latest tab
    # driver.switch_to.window(driver.window_handles[-1])
    # driver.maximize_window()
    # Debugging: Print current URL to verify the new tab is correct
    print("Current URL:", driver.current_url)
    time.sleep(10)  # wait a moment to ensure the page is fully loaded change to 10 after testing
    pyautogui.moveTo(download_button_x, download_button_y)
    pyautogui.click()
    print(f"Clicked at coordinates ({download_button_x}, {download_button_y})")

    time.sleep(10)  # wait a moment to ensure the page is fully loaded change to 10
    pyautogui.moveTo(save_button_x, save_button_y)
    pyautogui.click()
    print(f"Clicked at coordinates ({save_button_x}, {save_button_y})")

    time.sleep(2)

    # Wait for the close button to be clickable
    close_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "modal_close")))

    # Click the button
    close_button.click()

    # driver.close()'''

# def click_5th_option(driver, dropdown_id):
#     retries = 5
#     for attempt in range(retries):
#         try:
#             # Wait for the dropdown to be visible and find it
#             dropdown = WebDriverWait(driver, 10).until(
#                 EC.visibility_of_element_located((By.ID, dropdown_id))
#             )
#             # Create a Select object from the dropdown
#             select = Select(dropdown)
#             # Wait for all options to be available
#             WebDriverWait(driver, 10).until(
#                 EC.visibility_of_all_elements_located((By.XPATH, f"//select[@id='{dropdown_id}']/option"))
#             )
#             # Select the 5th option (index 4 as it's 0-based)
#             select.select_by_index(4)
#             print("Successfully selected the 5th option.")
#             break
#         except (StaleElementReferenceException, ElementClickInterceptedException, TimeoutException, NoSuchElementException) as e:
#             print(f"Exception occurred: {e}. Attempt {attempt + 1} of {retries}")
#             if attempt < retries - 1:
#                 time.sleep(1)
#                 continue
#             else:
#                 print("Failed to select the 5th option after several retries.")
#                 raise
def click_5th_option(driver, dropdown_name):
    retries = 5
    for attempt in range(retries):
        try:
            # Wait for the dropdown to be visible and find it by name attribute
            dropdown = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, dropdown_name))
            )
            # Create a Select object from the dropdown
            select = Select(dropdown)
            # Wait for all options to be available
            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, f"//select[@name='{dropdown_name}']/option"))
            )
            # Select the 5th option (index 4 as it's 0-based)
            select.select_by_index(4)
            print("Successfully selected the 5th option.")
            time.sleep(8)#change to 8
            break
        except (StaleElementReferenceException, ElementClickInterceptedException, TimeoutException, NoSuchElementException) as e:
            print(f"Exception occurred: {e}. Attempt {attempt + 1} of {retries}")
            if attempt < retries - 1:
                time.sleep(1)
                continue
            else:
                print("Failed to select the 5th option after several retries.")
                raise


clicked_ids = set()

print("start")
driver = initialize_driver()
main_process(driver)
attempt_count=0
while True:
    click_5th_option(driver,'example_pdf_length')
    # Find all clickable elements
    click_elements = driver.find_elements(By.XPATH, "//*[contains(@id, 'link')]")
    click_ids = [element.get_attribute('id') for element in click_elements if element.get_attribute('id') not in clicked_ids]
    print(len(click_ids))
    # if not click_ids:
    #     print("No more new links to click. Exiting.")
    #     driver.quit()
    #     break
    
    original_window = driver.current_window_handle
    for i,IDs in enumerate(click_ids):#len(click_ids)-1
        print(IDs)
        print(i)
        click_locator = (By.ID,IDs)
        perform_download(driver, click_locator, download_button_x=2526, download_button_y=525, save_button_x=1268, save_button_y=936)
        if i==24:
            input()
        clicked_ids.add(IDs)
        
        if i!=0 and i%25==0:
            print(i)
            input()
            if i==25:
                print("26th download")
            while True:
                # # Wait for the captcha popup to appear
                # WebDriverWait(driver, 20).until(EC.alert_is_present())
                # alert = driver.switch_to.alert
                # captcha_text = solve_captcha_25(driver)
                # element = driver.find_element(By.ID, 'captchapdf')
                # element.click()
                # # captcha = input("Enter captcha by seeing browser: ") 
                # captcha_text=solve_captcha(driver)   
                # print("Captcha text:", captcha_text)
                # element.send_keys(captcha_text)
                # submit_locator = (By.XPATH, "//input[@value='submit']")
                # # Wait for the submit button to be both visible and clickable
                # element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(submit_locator))
                # # Click the submit button
                # element.click()
                # # WebDriverWait(driver, 20).until(EC.visibility_of_element_located(submit_locator))
                # # element=WebDriverWait(driver, 10).until(EC.element_to_be_clickable(submit_locator))
                # # element = driver.find_element(*submit_locator)
                # # element.click()
                # time.sleep(10)

                # Wait for the popup to appear
                popup = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.modal-content')))
        
                # Execute JavaScript to click on the popup
                driver.execute_script("arguments[0].click();", popup)
                # Solve the captcha and enter it into the input field
                captcha_text = solve_captcha_25(driver)
                captcha_element = driver.find_element(By.ID, 'captchapdf')
                # Execute JavaScript to click on the captcha element
                driver.execute_script("arguments[0].click();", captcha_element)
                # Send the captcha text using JavaScript
                driver.execute_script("arguments[0].value = arguments[1];", captcha_element, captcha_text)

                # Find and click the submit button using JavaScript
                submit_locator = (By.XPATH, "//input[@value='submit']")
                submit_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(submit_locator))
                # Execute JavaScript to click on the submit button
                driver.execute_script("arguments[0].click();", submit_button)

                # Wait for the next action to take place
                time.sleep(10)
               
                try:
                    WebDriverWait(driver, 20).until(EC.alert_is_present())
                    alert = driver.switch_to.alert
                    alert.accept()
                    continue
                except TimeoutException:
                    break
            time.sleep(1)  # Adjust the sleep time based on the time needed for each download to complete change to 2
    else:
        print("else-block")
        # next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "modal_close")))
        # print("hello")
        # # Click the button
        # next_button.click()
        try:
            next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "modal_close")))
            print("hello")
            next_button.click()
            attempt_count = 0  # Reset the counter after a successful click
        except TimeoutException:
            body = driver.find_element(By.TAG_NAME, 'body')
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            attempt_count += 1
            print(f"Next button not clickable. Attempt {attempt_count}")
            if attempt_count >= 20:
                print("Next button not clickable after 20 attempts. Exiting loop.")
                break
            time.sleep(1)

print("completed main")



