#!/usr/bin/python3
#MailBomber.py -> mass mailing script
import smtplib
import time
import getpass

RED = '\033[31m'
END = '\033[0m'
ascii_art = RED \
    + """                                                                                                                                                                                                                                                                                                                                                     
     ______  _______          ____    ____  ____              _____          _____         ______  _______         _____        ______        _____   
    |      \/       \    ____|\   \  |    ||    |        ___|\     \    ____|\    \       |      \/       \   ___|\     \   ___|\     \   ___|\    \  
   /          /\     \  /    /\    \ |    ||    |       |    |\     \  /     /\    \     /          /\     \ |    |\     \ |     \     \ |    |\    \ 
  /     /\   / /\     ||    |  |    ||    ||    |       |    | |     |/     /  \    \   /     /\   / /\     ||    | |     ||     ,_____/||    | |    |
 /     /\ \_/ / /    /||    |__|    ||    ||    |  ____ |    | /_ _ /|     |    |    | /     /\ \_/ / /    /||    | /_ _ / |     \--'\_|/|    |/____/ 
|     |  \|_|/ /    / ||    .--.    ||    ||    | |    ||    |\    \ |     |    |    ||     |  \|_|/ /    / ||    |\    \  |     /___/|  |    |\    \ 
|     |       |    |  ||    |  |    ||    ||    | |    ||    | |    ||\     \  /    /||     |       |    |  ||    | |    | |     \____|\ |    | |    |
|\____\       |____|  /|____|  |____||____||____|/____/||____|/____/|| \_____\/____/ ||\____\       |____|  /|____|/____/| |____ '     /||____| |____|
| |    |      |    | / |    |  |    ||    ||    |     |||    /     || \ |    ||    | /| |    |      |    | / |    /     || |    /_____/ ||    | |    |
 \|____|      |____|/  |____|  |____||____||____|_____|/|____|_____|/  \|____||____|/  \|____|      |____|/  |____|_____|/ |____|     | /|____| |____|
    \(          )/       \(      )/    \(    \(    )/     \(    )/        \(    )/        \(          )/       \(    )/      \( |_____|/   \(     )/  
     '          '         '      '      '     '    '       '    '          '    '          '          '         '    '        '    )/       '     '   
                                                                                                                                   '                                                                                           
                                                     [++] MailBomber is a mass mailer script or tool [++]
                                                                Coded By: Ankit Dobhal                                
                                                             Let's Begin To Bomb the mails..!            
-------------------------------------------------------------------------------------------------------------------------------------------------------
MailBomber version 1.0
""" \
    + END
print(ascii_art)
def get_smtp_server_and_port(server):
    smtp_server=""
    port=587
    if server == "gmail":
        smtp_server = "smtp.gmail.com"
    elif server == "yahoo":
        smtp_server = "smtp.mail.yahoo.com"
        port = 465
    elif server == "outlook":
        smtp_server = "smtp.live.com"
    else:
        raise ValueError('SMTP server and port not available')
    return(smtp_server,port)

def mass():
    try:
        server = input ("Server Mail:")
        smtp_server,port=get_smtp_server_and_port(server)
        smtpobj = smtplib.SMTP(smtp_server,port)
        #smtpobj is a SMTP object that represents a connection to an SMTP mail server and has methods for sending emails.
        my_email = input("What is your email address ? ")
        my_passw = getpass.getpass('Enter your password:')
        #input password from terminal
        recip_mail = input("What is the recipient\'s email address ? ")
        message = input("Enter the message that you want to mail:\n")
        times = int(input("How many times do you want to send mail ? "))
        smtpobj.ehlo()
        if smtp_server == "smtp.gmail.com":
            smtpobj.starttls()
            #This step enables encryption(TLS Encryption) for your connection.
        try:
            smtpobj.login(my_email,my_passw)
            #this will help user to logged in gmail account
            for i in range(0,times):
                smtpobj.sendmail(my_email,recip_mail,message)
                time.sleep(1)
                #sendmail() will help user to send mail to recipent user.
                print("mail sent {} times".format(i+1))
            print("Lets quit:\n",smtpobj.quit())
        except smtplib.SMTPAuthenticationError:
            print("The username or password you entered is incorrect.")
    except ValueError as err:
        print(err)

    #it will close your connection
if __name__=='__main__':
    mass()
