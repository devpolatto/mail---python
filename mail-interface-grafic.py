import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64



print("********* Enviar email usando GMAIL *********")

user = input("User: ")
passwd = input("Password: ")

'''structure'''
sender = input("Remetente: ")
recipient = input("Destinatário: ")
subject = input("Assunto: ")
message = input("Menssagem: ")
file = input("caminnho do arquivo: ")

#door SMTP of GMAIL
gmail = smtplib.SMTP('smtp.gmail.com', 587)

#protocolo de incripitaçao de dados utilizados pelo GMAIL
gmail.starttls()

#credenciais
gmail.login(user, passwd)

#debug do processo de envio 1=true
gmail.set_debuglevel(1)

header = MIMEMultipart()
header['Subject'] = assunto
header['From'] = remetente
header['to'] = destinatario

menssage_format = MIMEText(menssage, 'html')#content-type:text/html

#send email
gmail.sendmail(remetente, destinatario, header.as_string())


