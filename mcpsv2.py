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
cancelledgang = 'School cancelled lets go!!!'
msg2 = 'School delayed lets go!!!'
msg3 = 'UPDATE: SCHOOL CANCELLED!!!!!!! GO BACK TO SLEEP!'
text_amount = 3 #IGNORE
carrier = str(input("What Carrier do you have? (tmobile, sprint, verizon, att): "))




print('Thanks! We will notify when a change of school schedule occurs.')

#--------------------------------------------------------------------------------



arrier_email = ""
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
        server.sendmail(gmail_address,target_email,message)
        print("Sent "+phone_num+" - " + message)
        time.sleep(wait)
    server.quit()

def schoolAlreadyDelayed():
    while True:
        dd = requests.get('https://montgomeryschoolsmd.org').text.count('closed')
        if dd > 0:
            Time = time.strftime("%I:%M:%S %p", time.localtime())
            print(Time + '  |  ' + 'School cancelled! Finally! Sending texts...')
            sms(msg3)
            print("{} texts were sent! -  happy sleeping".format(text_amount))
            sys.exit()
        else:
            print('School still not cancelled. Pls MCPS!!! Scanning again')
            time.sleep(2)




while True:
    c = requests.get('https://montgomeryschoolsmd.org').text.count('delayed') #Can be edited with other website for other school
    d = requests.get('https://montgomeryschoolsmd.org').text.count('closed') #Same as here

    if c > 0:
        Time = time.strftime("%I:%M:%S %p", time.localtime())
        print(Time + '  |  ' + 'School delayed! Sending texts...')
        sms(msg2)
        Time = time.strftime("%I:%M:%S %p", time.localtime())
        print(Time + '  |  ' + "{} texts were sent! -  happy sleeping".format(text_amount))
        time.sleep(2)
        print("------------------------------------------------------")
        print("     School is currently delayed my friend")
        print("We will continue to scan + notify you if school is cancelled")
        print("-------------------------------------------------------")
        time.sleep(2)
        schoolAlreadyDelayed()
    else:
        Time = time.strftime("%I:%M:%S %p", time.localtime())
        print(Time +'  |  ' + 'School not delayed, scanning again')
        time.sleep(2)
        if d > 0:
            Time = time.strftime("%I:%M:%S %p", time.localtime())
            print(Time + '  |  ' + 'School cancelled! Sending texts...')
            sms(cancelledgang)
            Time = time.strftime("%I:%M:%S %p", time.localtime())
            print(Time + '  |  ' + "{} texts were sent! -  happy sleeping".format(text_amount))
            sys.exit()
        else:
            Time = time.strftime("%I:%M:%S %p", time.localtime())
            print(Time + '  |  ' + 'School not cancelled, scanning again')
            time.sleep(2)
