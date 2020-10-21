#!/usr/bin/env python3

import os
import json
from dotenv import load_dotenv

import requests
import ssl
from smtplib import SMTP_SSL
from email.message import EmailMessage


def main():
    load_dotenv()
    last_ip = get_last_ip()
    current_ip = get_external_ip()
    if current_ip != last_ip:
        send_email(current_ip)
        save_ip(current_ip)


def get_last_ip() -> str:
    filename = os.getenv('LAST_IP_FILE')
    if not os.path.isfile(filename):
        return "0.0.0.0"
    with open(filename) as json_file:
        data = json.load(json_file)
        return data['last_ip']


def save_ip(ip:str):
    filename = os.getenv('LAST_IP_FILE')
    with open(filename, 'w') as json_file:
        json.dump({'last_ip': ip}, json_file)


def get_external_ip() -> str:
    # See https://stackoverflow.com/a/36205547
    return requests.get("https://api.ipify.org").text


def send_email(ip:str):
    message = EmailMessage()
    message['Subject'] = os.getenv('EMAIL_SUBJECT')
    message['From'] = os.getenv('SENDER_EMAIL')
    message['To'] = os.getenv('RECEIVER_EMAIL')
    message.set_content(ip)
    sender_password = os.getenv('SENDER_PASSWORD')
    port = int(os.getenv('GMAIL_SMTP_SSL_PORT'))
    
    context = ssl.create_default_context()
    with SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(message['From'], sender_password)
        server.send_message(message)


if __name__ == '__main__':
    main()
