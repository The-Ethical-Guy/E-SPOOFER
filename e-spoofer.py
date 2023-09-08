import readline
import subprocess
import os
import time
import signal
import sys

os.system("clear")

red = '\033[91m'



email = """
     'okOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkd,     
  ;l. .oKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd' .lc. 
  lNKo. .oKWMMMMMMMMMMMMMMMMMMMMMMMMMMMXd' .l0Wk. 
  lWMWKo. .oKWMMMMMMMMMMMMMMMMMMMMMMMXd' .c0WMMk. 
  lWMMMWKo. .oKWMMMMMMMMMMMMMMMMMMMXd' .c0WMMMMk. 
  lWMMMMMWKo. .oKWMMMMMMMMMMMMMMMXd' .c0WMMMMMMk. 
  lWMMMMMMMWKo. .oKWMMMMMMMMMMMXd' .c0WMMMMMMMMk. 
  lWMMMMMMMMMWKl. .oKWMMMMMMMXx' .c0WMMMMMMMMMMk. 
  lWMMMMMMMMMMMNd.  .oXMMMMXx,  .oNMMMMMMMMMMMMk. 
  lWMMMMMMMMMW0c. ,:. .oOOd, .;' .c0WMMMMMMMMMMk. 
  lWMMMMMMMW0c. ,xNWKl.    .c0WXd' .c0WMMMMMMMMk. 
  lWMMMMMW0c. ,xXMMMMWKl,,cOWMMMMXd' .l0WMMMMMMk. 
  lWMMMW0c. ,xXMMMMMMMMWWWWMMMMMMMMXd' .l0WMMMMk. 
  lWMW0c. ,xXMMMMMMMMMMMMMMMMMMMMMMMMXd' .l0WMMk.               YOU WILL BE WHOEVER YOU WANT NO MORE LIMITES
  :K0c. 'dXMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd' .l0No  
   '.   ,:MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM:,   .'


"""
  
name = """




 _______      _______  _______  _______  _______  _______  _______  _______ 
(  ____ \    (  ____ \(  ____ )(  ___  )(  ___  )(  ____ \(  ____ \(  ____ )
| (    \/    | (    \/| (    )|| (   ) || (   ) || (    \/| (    \/| (    )|
| (__  _____ | (_____ | (____)|| |   | || |   | || (__    | (__    | (____)|
|  __)(_____)(_____  )|  _____)| |   | || |   | ||  __)   |  __)   |     __)
| (                ) || (      | |   | || |   | || (      | (      | (\ (   
| (____/\    /\____) || )      | (___) || (___) || )      | (____/\| ) \ \__
(_______/    \_______)|/       (_______)(_______)|/       (_______/|/   \__/



"""

email_lines = email.split("\n")
name_lines = name.split("\n")

for email_line, name_line in zip(email_lines, name_lines):
    print(f"\033[1;97m\033[91m{email_line}\033[0m\033[1;97m{name_line}")

print('''\033[1;97m\033[34m                    THE BEST EMAIL SPOOFING TOOL!!
  %s                                            by TheEthicalGuy\033[0m\n''' % red)






tool_closed = False

def handle_exit(signal, frame):
    global tool_closed
    tool_closed = True
    print("Tool closed")
    sys.exit(0)


signal.signal(signal.SIGINT, handle_exit)


def print_message(message, color):
    for char in message:
        print("\033[91m\033[1;97m" + char + "\033[0m\033[1;97m", end="", flush=True)
        time.sleep(0.03)  # تأخير لمدة 0.1 ثانية
    print()  # طباعة سطر جديد
    print("\033[34m{}\033[0m".format("https://www.youtube.com/@TheEthicalGuy"))  # طباعة الرسالة الثانية باللون الأزرق

message = "SUBSCRIBE TO MY CHANNEL FOR MORE TOOLS"
color = "\033[91m\033[1;97m"  # اللون الأحمر 

print_message(message, color)

print("")
print("Choose an option\n[1] Write the email manually\n[2] Send HTML file\n")


user_choice = input("\033[91m$~> ")

if user_choice == "1":
    path_to_file = "tools/textmail.py"
    subprocess.call(["python", path_to_file])


elif user_choice == "2":
      path_to_file = "tools/htmlmail.py"
      subprocess.call(["python", path_to_file])
      
else:
    print('Invalid option selected')
