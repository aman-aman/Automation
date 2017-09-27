#aman kumar jha

import smtplib

sender =input("Enter your Email ID: ")
receivers = input("Enter the receiver Email ID:")
MY_ADDRESS=input("Enter your Email ID: ")
PASSWORD=input("Enter your Password: ")
message = input("Enter your message: ")

try:
   s=smtplib.SMTP("smtp.gmail.com",587)
   s.ehlo()
   s.starttls()
   s.login(MY_ADDRESS, PASSWORD)
   s.sendmail(sender, receivers,message)
   s.close()
   print ("Successfully sent email")

except:
   print ("Error: unable to send email")