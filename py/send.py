import smtplib
server = smtplib.SMTP('cucmamnon1970@gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("lol00sever@gmail.com", "password")
msg = "HI!"
server.sendmail("lol00sever@gmail.com", "lol00sever@gmail.com", msg)
server.sendmail("lol00sever@gmail.com", "lol00sever@gmail.com", msg)
server.sendmail("lol00sever@gmail.com", "lol00sever@gmail.com", msg)
server.sendmail("lol00sever@gmail.com", "lol00sever@gmail.com", msg)
server.quit()