import pyautogui as pg
import datetime as dt
import smtplib
from email.message import EmailMessage
import os
import imghdr
import time

# Variáveis
name = str(dt.datetime.now())
name = name.replace(':','-')
name = name.replace('.','-')
name = name.replace(' ','-')
name = name + '_scr.png'

path = r'C:/Users/Public/Pictures/' + name

# Screenshot e salvar em pasta
def takeScreenshot(_path):
    pg.click(1156,604)
    time.sleep(2)
    myScr = pg.screenshot()
    myScr.save(_path)

#função para envio do email
def mailer(_name, _path):
    # Email responsável pelo envio
    sender = 'contato.welerson@gmail.com'
    # Array de email's que receberão
    receivers = ['contato.welerson@gmail.com']

    # Local Config
    port = 587
    msg = EmailMessage()


    msg['Subject'] = 'Mail test'
    msg['From'] = 'mail@mail.com.br'
    msg.set_content('Hello World')

    with open(_path, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = _name
    msg.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

    with smtplib.SMTP('mail.server.com.br', port) as server:
        server.login('mail@mail.com.br', 'mailPassword')
        server.sendmail(sender, receivers, msg.as_string())

# main
takeScreenshot(path)
mailer(name, path)
