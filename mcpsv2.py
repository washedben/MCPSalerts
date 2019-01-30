import requests
import time
import smtplib
from time import sleep
import sys


print (" ----------------------------------------------")
print ("                MCPS TEXT ALERTS               ")
print ("                Developed by Ben                    ")
print (" ----------------------------------------------")

provider = 'smtp.gmail.com' #IGNORE
port = 587 #IGNORE
phone_num = str(input("Number to Notify: "))
gmail_address = str(input("Enter Gmail Address: "))
password = str(input("Enter Gmail Password: "))
msg1 = 'School cancelled lets go!!!'
msg2 = 'School delayed lets go!!!'
text_amount = 3 #IGNORE
carrier = str(input("What Carrier do you have? (tmobile, sprint, verizon, att): "))




print('Thanks! We will notify when a change of school schedule occurs.')

#--------------------------------------------------------------------------------



carrier_email = ""
target_email = phone_num+"@"+carrier_email

if carrier == "tmobile":
	carrier_email = "tmomail.net"
elif carrier == 'sprint':
	carrier_email = "messaging.sprintpcs.com"
elif carrier == "att":
	carrier_email = "txt.att.net"
elif carrier == "verizon":
	carrier_email = "vtext.com"
else:
	print("Entered Carrier Wrong!")



def sms(message):
    carrier_email = "vtext.com"
    target_email = phone_num+"@"+carrier_email
    wait = 2 #DELAY
    server = smtplib.SMTP(provider, port)
    server.starttls()
    server.login(gmail_address, password)
    for _ in range(0,text_amount):
        server.sendmail(gmail_address,target_email,msg2)
        print("Sent "+phone_num+" - "+msg2)
        time.sleep(wait)
    server.quit()


while True:
    c = requests.get('https://montgomeryschoolsmd.org').text.count('delayed') #Can be edited with other website for other school
    d = requests.get('https://montgomeryschoolsmd.org').text.count('closed') #Same as here

    if c > 0:
        print('School delayed! Sending texts...')
        sms(msg2)
        print("{} texts were sent! -  happy sleeping".format(text_amount))
        sys.exit()
    else:
        print('School not delayed, scanning again')
        time.sleep(2)
        if d > 0:
            print('School cancelled! Sending texts...')
            sms(msg1)
            print("{} texts were sent! -  happy sleeping".format(text_amount))
            sys.exit()
        else:
            print('School not cancelled, scanning again')
            time.sleep(2)
