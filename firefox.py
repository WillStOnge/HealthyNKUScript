# Author: Will St. Onge
#
# This script is made to fill out and submit the Health@NKU form that NKU made for the Fall 2020 semester because of COVID-19.
# It doesn't run by itself so, you will need to schedule it yourself or manually run it.
# This script only supports Mozilla Firefox, if you need another version download it from the GitHub repo (https://github.com/WillStOnge/HealthyNKUScript)
#
# To run this script, you need to install Python 3 or later (https://www.python.org/downloads/) and run "pip install selenium" in your terminal to install the Selenium library.
# You will also need to download Mozilla's geckodriver (https://github.com/mozilla/geckodriver/releases) and add it to your PATH (https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/).
# Once you've added it to your PATH, you will probably need to restart your computer for the script to run.
# 
# Usage: python firefox.py NKU_Username NKU_Password
# 
# Example: python firefox.py stongew1 password123
# 
# If the script is clicking to early (error being spat out), increase the numbers in the time.sleep() calls.
# I made the times fairly long to accomidate bad/inconsistent Internet, but it could be too short in some situations. 
# We don't need to wait between pages since it is all stored locally. We only need to wait after logging in and submitting the form (just in case).
#
# If you find a bug, report it on the GitHub repository (https://github.com/WillStOnge/HealthyNKUScript/issues). Please include a copy of the log generated.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys

# Make sure script was fed a username and password.
if len(sys.argv) < 3:
    print('Usage: python firefox.py username password')
    exit(3)

# Get username and password from command line.
username = sys.argv[1]
password = sys.argv[2]

# Open a new Firefox web driver and go to the Healthy@NKU form.
driver = webdriver.Firefox()
driver.get('https://mynku.nku.edu/irj/portal?NavigationTarget=navurl://8264b83338e13d3ad78fef60b572fdcb&NavMode=3')

# Login with provided username and password.
driver.find_element_by_id('userNameInput').send_keys(username)
driver.find_element_by_id('passwordInput').send_keys(password + Keys.RETURN)

# Wait for the first page to load.
time.sleep(5)

# Go into the iFrame and scroll far enough to get past to cookies toast.
driver.switch_to.frame('sap-application')
driver.execute_script("window.scrollBy(0, 2000);")

# Dismiss the CC warning and click the no and next buttons. 
driver.find_element_by_class_name('cc-dismiss').click()
driver.find_element_by_css_selector('#symptoms_no').click()
driver.find_element_by_css_selector('div.panel:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > a:nth-child(1)').click()

# Scroll down.
driver.execute_script("window.scrollBy(0, 2000);")

# Do the second page and move on to the third.
driver.find_element_by_css_selector('#household_symptoms_no').click()
driver.find_element_by_css_selector('#contact_no').click()
driver.find_element_by_css_selector('a.btn:nth-child(2)').click()

# Scroll down.
driver.execute_script("window.scrollBy(0, 2000);")

# Do the third page and submit the form.
driver.find_element_by_css_selector('#tab3 > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > label:nth-child(4)').click()
driver.find_element_by_css_selector('button.btn').click()

# Wait for a second to make sure the form submission goes through.
time.sleep(1)

# Close the driver so it doesn't stay open.
driver.close()