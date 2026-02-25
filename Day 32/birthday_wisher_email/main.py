# Email sender
import smtplib

my_email = "m-sender@gmail.com"
password = "abcd1234()"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email, to_addrs="recepientemail@yahoo.com", 
#                     msg="Subject:Hello\n\nThis is the main message of my email")
# connection.close()


with smtplib.SMTP("smtp.gmail.com") as connection:
    # tls - transport layer security
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email, to_addrs="recepientemail@yahoo.com", 
                        msg="Subject:Hello\n\nThis is the main message of my email")
