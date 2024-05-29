from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
import os
import csv
import inspect
def create_csv():
    # Create the CSV file
        with open("dcourts.csv", "w", newline="") as csvfile:
            fieldnames = ["state","district id", "court id","court name","url","key value to Navigate"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write column names to the CSV file
            writer.writeheader()
            print("Created CSV file")
def old_website(driver,URL1,district,state):
    # Define the CSV file name
    csv_file = "old_websites.csv"

    # Check if the file exists
    file_exists = os.path.isfile(csv_file)
    # Create the CSV file
    with open(csv_file, "a" if file_exists else "w", newline="") as csvfile:
        fieldnames = ["state","district id","url"]
        # Create a DictWriter object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Write column names to the CSV file if it does not exist
        if not file_exists:
            writer.writeheader()
            print("Created CSV file and added header")

        # Write the row
        writer.writerow({"state": state, "district id": district, "url": URL1})
        print(f"Added row: {state}, {district}, {URL1}")
def get_Values(driver,state):
    print(f"inside {state} function")
    # Find the dropdown element by its ID and wait for options to be visible
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'sateist')))
    select_element = Select(driver.find_element(By.ID, 'sateist'))

    # Extract option values 
    options = select_element.options

    # Print the number of options found
    print(f"Number of options found: {len(options)}")
    # Create an empty list to store the values
    district_list = []
    # Iterate through options and extract values
    for option in options:
        value = option.get_attribute("value")
        if value:  # Check if value is not empty
            district_list.append(value)
    print(district_list)

    for i, district in enumerate(district_list):
        print(f"Selecting district {district} (index {i})")
        # if i==0 or i==1:
        #     continue
        try:
            # Find the dropdown element by its ID
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'sateist')))
            dropdown_element = driver.find_element(By.ID, 'sateist')
            
            # Click the dropdown to expand it
            dropdown_element.click()
            time.sleep(1)  # Short sleep to allow dropdown to expand

            # Select the state by index
            select_element = Select(driver.find_element(By.ID, 'sateist'))
            select_element.select_by_index(i+1)
            time.sleep(5)
            # Get the current URL
            URL1 = driver.current_url
            old=".ecourts.gov.in" in URL1
            if ".ecourts.gov.in" in URL1:
                print(f"{district} of {state} is still in old website")
                
                old_website(driver,URL1,district,state)
            else:
                # Simulate pressing the Tab key multiple times
                actions = webdriver.ActionChains(driver)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(1)
                # Find the element with title attribute "Order Date"
                order_date_element = driver.find_element(By.XPATH, '//*[@title="Order Date"]')

                # Scroll the element into view
                driver.execute_script("arguments[0].scrollIntoView(true);", order_date_element)

                # Wait for a while to observe the action or allow the page to update if needed
                time.sleep(2)

                # Click the element
                order_date_element.click()

                # Wait for a while to observe the action or allow the page to update if needed
                time.sleep(2)

                # Find the element with the specified attributes
                Court_Establishment_button = driver.find_element(By.XPATH, '//input[@value="courtEstablishment" and @data-view="courtEstablishment" and @type="radio" and @class="serviceType" and @id="chkNo" and @name="service_type"]')
                # Click the element
                Court_Establishment_button.click()

                # Wait for a while to observe the action or allow the page to update if needed
                time.sleep(1)

                # Find the dropdown element by its ID and wait for options to be visible
                WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'court_establishment')))
                select_element = Select(driver.find_element(By.ID, 'court_establishment'))

                # Extract option values 
                options = select_element.options

                # Print the number of options found
                print(f"Number of options found: {len(options)}")
                # Create an empty list to store the values
                Court_Establishment_list = []
                # Iterate through options and extract values
                for option in options:
                    value = option.get_attribute("value")
                    name = option.text
                    if value:  # Check if value is not empty
                        Court_Establishment_list.append((value, name))
                # Define the CSV file name based on the function name
                csv_filename ="dcourts.csv"

                # Check if the file exists
                file_exists = os.path.isfile(csv_filename)
                # Get the current URL
                URL = driver.current_url
                # Extract words between 'https://' and '.dcourts.gov'
                start = URL.find("https://") + len("https://")
                end = URL.find(".dcourts.gov")
                Dsubstring = URL[start:end]
                # Writing to the CSV file
                with open(csv_filename, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    # Write the header if the file doesn't exist
                    if not file_exists:
                        writer.writerow(['State','District', 'Value', 'Name','URL','key value to Navigate'])
            
                    # Write the rows
                    for index, (value, name) in enumerate(Court_Establishment_list):
                        writer.writerow([state,district, value, name,URL,Dsubstring])
                print(f"{district} Data appended to {csv_filename}")
                
                


                print(f"URL after selecting district: {driver.current_url}")

                # Perform any specific tasks for the selected state here
                # For example, print the current state being processed
                print(f"Processing district: {district}")

        except TimeoutException as e:
            print(f"TimeoutException: URL did not change after selecting state {district}: {e}")
        except NoSuchElementException as e:
            print(f"NoSuchElementException: An element was not found: {e}")
        except StaleElementReferenceException as e:
            print(f"StaleElementReferenceException: An element reference became stale: {e}")
        except ElementClickInterceptedException as e:
            print(f"ElementClickInterceptedException: An element click was intercepted: {e}")
        print("hi")
        # Navigate back to the main page
        if not old:
            driver.back()
        print(f" saved {district} data")
        driver.back()
        
        
        # Wait for the page to load again
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'sateist')))
    else:
        print(f"complete {state} data appended")
        #input("anadaman completed press enter to continue")
def initialize():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    # Initialize the Chrome driver with the configured options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://districts.ecourts.gov.in/")
    return driver

def selecting_all_states(driver):
    # Find the dropdown element by its ID and wait for options to be visible
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'sateist')))
    select_element = Select(driver.find_element(By.ID, 'sateist'))

    # Extract option values 
    options = select_element.options

    # Print the number of options found
    print(f"Number of options found: {len(options)}")
    # Create an empty list to store the values
    values_list = []
    # Iterate through options and extract values
    for option in options:
        value = option.get_attribute("value")
        if value:  # Check if value is not empty
            values_list.append(value)
    print(values_list)

    for i, state in enumerate(values_list):
        print(f"Selecting state {state} (index {i})")
        
        try:
            # Find the dropdown element by its ID
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'sateist')))
            dropdown_element = driver.find_element(By.ID, 'sateist')
            
            # Click the dropdown to expand it
            dropdown_element.click()
            time.sleep(1)  # Short sleep to allow dropdown to expand

            # Select the state by index
            select_element = Select(driver.find_element(By.ID, 'sateist'))
            select_element.select_by_index(i+1)
            time.sleep(5)
            # Get the function object from the global namespace using the dictionary lookup
            # func = globals()[state]
            
            # # Call the function
            # func()
            get_Values(driver,state)

            

            print(f"URL after selecting state: {driver.current_url}")

            # Perform any specific tasks for the selected state here
            # For example, print the current state being processed
            print(f"Processing state: {state}")

        except TimeoutException as e:
            print(f"TimeoutException: URL did not change after selecting state {state}: {e}")
        except NoSuchElementException as e:
            print(f"NoSuchElementException: An element was not found: {e}")
        except StaleElementReferenceException as e:
            print(f"StaleElementReferenceException: An element reference became stale: {e}")
        except ElementClickInterceptedException as e:
            print(f"ElementClickInterceptedException: An element click was intercepted: {e}")

        # Navigate back to the main page
        driver.back()
        
        # Wait for the page to load again
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'sateist')))

# Initialize the driver
driver = initialize()
create_csv()
# Select all states
selecting_all_states(driver)

