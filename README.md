Autofill Form Script
This Python script automates filling out a simplistic Google Form using Selenium.
![image](https://github.com/user-attachments/assets/48d2692c-7f02-403d-aca1-7ddd2f76c3ab)

Prerequisites
To run this script, ensure the following:

Google Chrome and WebDriver

Install Google Chrome.
Download a WebDriver version compatible with your Chrome version. For example in my case:
Chrome Version: 132.0.6834.111
WebDriver Version: 132.0.6834.110
Install Selenium Package
Use the following command to install Selenium:
pip install selenium  

Configuration

Chrome Profile Path:
Update the chrome_profile_path variable in the script to match your Chrome profile path. For example:
chrome_profile_path = r"C:/Users/SAFAE/AppData/Local/Google/Chrome/User Data"  
Google Form URL:
Replace the form_url variable with the URL of the Google Form you want to autofill.
Data to Autofill:
Update the people_data list in the script with the names, emails, and addresses to be submitted.

Running the Script

Save the script in a .py file (e.g., autofill_form.py).
Run the script in a terminal or Python IDE:
python autofill_form.py  
The script will launch Chrome, fill out the form for each person in the people_data list, and submit the form.

Notes
Ensure the Google Form fields correspond to the expected inputs in the script ( text, email, textarea).
The script uses Chrome in profile mode, so you must have logged into Chrome at least once using the specified profile.
