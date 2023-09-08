import readline
import os
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
  %sWrite the email manually\033[0m\n''' % red)



tool_closed = False

def handle_exit(signal, frame):
    global tool_closed
    tool_closed = True
    print("Bye")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit)

def send_email():
    try:
         #smtp input
        smtpinput = input("ENTER THE SMTP SERVER (ip or host name) > ")
        while True:
            portinput = input("ENTER THE PORT (examples: 587 - 25) > ")
            try:
                SMTP_PORT = int(portinput)
                break
            except ValueError:
                print("enter a valid port")
        SMTP_SERVER = smtpinput



        SMTP_USERNAME = input("ENTER THE USERNAME > ")
        SMTP_PASSWORD = input("ENTER THE PASSWORD > ")


        msg = MIMEMultipart()
        sender_name = input("ENTER THE SENDER NAME > ")
        sender_email = input("ENTER THE SENDER EMAIL > ")
        msg['From'] = f'{sender_name} <{sender_email}>'
        msg['To'] = input("ENTER THE TARGET EMAIL > ")
        add_cc = input('DO YOU WANT TO ADD MORE EMAILS? (y/n) > ')

        if add_cc.lower() == 'y':
            cc_emails = input("ENTER THE EMAILS (separated by semicolon) > ")
            msg['Cc'] = cc_emails

        msg['Subject'] = input("ENTER THE SUBJECT > ")
        body = input("ENTER THE BODY > ")
        msg.attach(MIMEText(body, 'plain'))


        attach_file = input('DO YOU WANT TO ATTACH A FILE? (y/n) > ')
        if attach_file.lower() == 'y':
            file_path = input('ENTER THE PATH OF THE FILE > ')
            if file_path:

                if os.path.exists(file_path):
                    with open(file_path, 'rb') as f:
                        attached_file = MIMEApplication(f.read())
                        attached_file.add_header('content-disposition', 'attachment', filename=os.path.basename(file_path))
                        msg.attach(attached_file)
                else:
                    print('Invalid file path')

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
   
    send_email()


if not tool_closed:
    input("Press Enter to exit...")
