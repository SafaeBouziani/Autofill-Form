# Autofill Form Script  

This Python script automates filling out a simplistic Google Form using Selenium.  

![Form Automation Preview](https://github.com/user-attachments/assets/48d2692c-7f02-403d-aca1-7ddd2f76c3ab)  

---

## Prerequisites  

To run this script, ensure the following:  

### 1. Google Chrome and WebDriver  

- **Install Google Chrome**.  
- **Download a WebDriver version compatible with your Chrome version**.  
  - Example:  
    - **Chrome Version:** 132.0.6834.111  
    - **WebDriver Version:** 132.0.6834.110  

### 2. Install Selenium Package  

Run the following command to install Selenium:  

```bash  
pip install selenium  
```  

---

## Configuration  

### 1. Chrome Profile Path  

Update the `chrome_profile_path` variable in the script to match your Chrome profile path. For example:  

```python  
chrome_profile_path = r"C:/Users/SAFAE/AppData/Local/Google/Chrome/User Data"  
```  

### 2. Google Form URL  

Replace the `form_url` variable with the URL of the Google Form you want to autofill.  

### 3. Data to Autofill  

Update the `people_data` list in the script with the names, emails, and addresses you want to submit.  

---

## Running the Script  

1. Save the script in a `.py` file (e.g., `autofill_form.py`).  
2. Run the script in a terminal or Python IDE:  

   ```bash  
   python autofill_form.py  
   ```  

The script will:  
- Launch Google Chrome.  
- Fill out the form for each person in the `people_data` list.  
- Automatically submit the form.  

---

## Notes  

- Ensure that the Google Form fields match the expected inputs in the script:  
  - **Text** for names.  
  - **Email** for email addresses.  
  - **Textarea** for addresses.  

- The script uses Chrome in profile mode. Ensure you have logged into Chrome at least once using the specified profile.
