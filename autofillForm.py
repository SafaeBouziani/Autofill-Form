from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_profile_path = r"C:/Users/SAFAE/AppData/Local/Google/Chrome/User Data"

chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={chrome_profile_path}")
chrome_options.add_argument("profile-directory=Default")


service = Service()  
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSf5dhbmAU71trmTI-KwjOnbVJnN8Sy52mf62o2z433OXeh51g/viewform"

people_data = [
    {"name": "Safae Bouziani", "email": "bouziani@example.com", "address": "Kenitra, Morocco"},
    {"name": "Salma Mahdioui", "email": "mahdioui@example.com", "address": "Rabat, Morocco"},
    {"name": "Fatima Zahra Boujrad", "email": "boujrad@example.com", "address": "Casablanca, Morocco"},

]


for person in people_data:
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(form_url)

    wait = WebDriverWait(driver, 10)
    text_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="text"]')))
    text_field.send_keys(person["name"])

    email_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="email"]')))
    email_field.send_keys(person["email"])

    address_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//textarea')))
    address_field.send_keys(person["address"])

    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="button"]')))
    submit_button.click()

    time.sleep(3)
    driver.quit()

    time.sleep(2)
