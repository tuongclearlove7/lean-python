mport smtplib
conn = smtplib.SMTP('imap.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('youremail@gmail.com', 'your_password')
 
conn.sendmail('from@gmail.com','to@gmail.com','Subject: What you like? \n\n Reply Reply Reply')
conn.quit()