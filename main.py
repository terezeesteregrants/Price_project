import smtplib
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime
import pandas as pd

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
    time.sleep(1)
    price_element1 = driver.find_element(By.CLASS_NAME, "i-product-data__price-inner")
    price1 = float(price_element1.text.replace("€", "").replace(",", "."))

    #otrā mājaslapa
    url2 = "https://www.euronics.lv/it/plansetdatori/plansetdatori/mpq13hcfsa/apple-ipad-10-2022-wi-fi-64-gb-zila-plansetdators"
    driver.get(url2)
    time.sleep(1)
    price_element2 = driver.find_element(By.XPATH, "//span[@class='price__original']")
    price2 = float(price_element2.text.replace("€", "").replace("&nbsp;", "").replace(",", "."))

    # trešā mājaslapa
    url3 = "https://www.rdveikals.lv/products/lv/149/452645/sort/5/filter/0_0_0_0/iPad-10th-Gen-10.9-64GB-Wi-Fi-Blue-MPQ13HC-A-planšetdators.html"
    driver.get(url3)
    time.sleep(1)
    price_element3 = driver.find_element(By.XPATH, "//strong[contains(text(),'579.00')]") 
    price3 = float(price_element3.text)

    driver.quit() 

    if price1 < price2 and price1 < price3:
        send_email("Lielisks darījums Tavam izvēlētjama Apple produktam!", f"Cena no Tet.lv ir viszemāka. Iepērcies: {url1}")
    elif price2 < price1 and price2 < price3:
        send_email("Lielisks darījums Tavam izvēlētjama Apple produktam!", f"Cena no Euronics.lv ir viszemāka. Iepērcies: {url2}")
    elif price3 < price1 and price3 < price2:
        send_email("Lielisks darījums Tavam izvēlētjama Apple produktam!", f"Cena no rdveikals.lv ir viszemāka. Iepērcies: {url3}")
    else:
        send_email("Lielisks darījums Tavam Apple produktam!", f"Cenas visās vietnēs ir vienādas. Iepērcies no Tet. lv: {url1}\nIepērcies no Euronics.lv: {url2}\nIepērcies no rdveikals. lv: {url3}")

check_price()


