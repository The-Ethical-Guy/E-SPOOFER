import readline
import sys
import signal
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

os.system("clear")

red = '\033[91m'



print('''\033[1;97m
                                 
 _______      _______  _______  _______  _______  _______  _______  _______ 
(  ____ \    (  ____ \(  ____ )(  ___  )(  ___  )(  ____ \(  ____ \(  ____ )
| (    \/    | (    \/| (    )|| (   ) || (   ) || (    \/| (    \/| (    )|
| (__  _____ | (_____ | (____)|| |   | || |   | || (__    | (__    | (____)|
|  __)(_____)(_____  )|  _____)| |   | || |   | ||  __)   |  __)   |     __)
| (                ) || (      | |   | || |   | || (      | (      | (\ (   
| (____/\    /\____) || )      | (___) || (___) || )      | (____/\| ) \ \__
(_______/    \_______)|/       (_______)(_______)|/       (_______/|/   \__/
  %sSend HTML file\033[0m\n''' % red)




tool_closed = False

def handle_exit(signal, frame):
    global tool_closed
    tool_closed = True
    print("Bye")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit)

def send_email():
    try:
        smtp_input = input("ENTER THE SMTP SERVER (IP or host name) > ")
        while True:
            portinput = input("ENTER THE PORT (examples: 587 - 25) > ")
            try:
                SMTP_PORT = int(portinput)
                break
            except ValueError:
                print("enter a valid port")
        username = input("ENTER THE USERNAME > ")
        password = input("ENTER THE PASSWORD > ")
        sender_name = input("ENTER THE SENDER NAME > ")
        sender_email = input("ENTER THE SENDER EMAIL > ")
        target_email = input("ENTER THE TARGET EMAIL > ")
        subject = input("ENTER THE SUBJECT > ")

        

        SMTP_USERNAME = username
        SMTP_PASSWORD = password
        SMTP_SERVER = smtp_input
        SMTP_PORT = portinput


        msg = MIMEMultipart()
        msg['From'] = f'{sender_name} <{sender_email}>'
        msg['To'] = target_email
        msg['Subject'] = subject


        add_cc = input('DO YOU WANT TO ADD MORE EMAILS? (y/n) > ')
        cc_email_list = []  
        if add_cc.lower() == 'y':
            cc_emails = input("ENTER THE EMAILS (separated by semicolon) > ")
            cc_email_list = cc_emails.split(',')
            msg['Cc'] = ','.join(cc_email_list)


        html_path = input("ENTER THE PATH OF THE HTML FILE > ")
        if os.path.exists(html_path):
            with open(html_path, 'r') as f:
                html_content = f.read()
                html_part = MIMEText(html_content, 'html')
                msg.attach(html_part)
        else:
            print('Invalid HTML file path')
        smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()

        smtp_server.login(SMTP_USERNAME, SMTP_PASSWORD)

        recipients = [msg['To']]
        if 'Cc' in msg:
            recipients.extend(msg['Cc'].split(';'))
        smtp_server.sendmail(msg['From'], recipients, msg.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print('Error sending email:', e)

if __name__ == "__main__":
    # الآن يمكنك استدعاء الدالة send_email() بدلاً من وضع الكود المباشر هنا
    send_email()

# اختبار إذا كان البرنامج مغلقًا بسبب الاستثناء أو تم إغلاقه بشكل صحيح
if not tool_closed:
    input("Press Enter to exit...")
