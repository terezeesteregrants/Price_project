import smtplib
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

def send_email(subject, message):
    email = "terezegrants@gmail.com"
    receiver_email = "terezegrants@gmail.com"
    text = f"Subject: {subject}\n\n{message}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, "ccptsllubqmrixtc")
    server.sendmail(email, receiver_email, text.encode('utf-8'))
    print("Epasts tika nosūtīts uz " + receiver_email)
    server.quit()

def check_price():
    service = Service()
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=option)

    
    # pirmā mājaslapa
    url1 = "https://www.tet.lv/veikals/plansetdatori/apple-ipad-10-9-wi-fi-64gb-blue-10th-gen-2022.html"
    driver.get(url1)
    time.sleep(2)
    price_element1 = driver.find_element(By.CLASS_NAME, "i-product-data__price-inner")
    price1 = float(price_element1.text.replace("€", "").replace(",", "."))