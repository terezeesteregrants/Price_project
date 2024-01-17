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
