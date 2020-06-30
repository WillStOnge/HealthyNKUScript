# Healthy@NKU Script

Author: Will St. Onge

This script is made to fill out and submit the Health@NKU form that NKU made for the Fall 2020 semester because of COVID-19.
It doesn't run by itself so, you will need to schedule it yourself or manually run it.
Currently, only Mozilla Firefox, Google Chrome, and Edge are supported.

To run this script, you need to install Python 3 or later (https://www.python.org/downloads/) and run "pip install selenium" in your terminal to install the Selenium library.
You will also need to download Mozilla's geckodriver (https://github.com/mozilla/geckodriver/releases) and add it to your PATH (https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/).
Once you've added it to your PATH, you will probably need to restart your computer for the script to run.
 
Usage: python firefox.py NKU_Username NKU_Password
 
Example: python firefox.py stongew1 password123
 
If the script is clicking to early (error being spat out), increase the numbers in the time.sleep() calls.
I made the times fairly long to accomidate bad/inconsistent Internet, but it could be too short in some situations. 
We don't need to wait between pages since it is all stored locally. We only need to wait after logging in and submitting the form (just in case).

If you find a bug, report it on the GitHub repository (https://github.com/WillStOnge/HealthyNKUScript/issues). Please include a copy of the log generated.