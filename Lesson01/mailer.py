#coding: utf-8
import smtplib
import socket
from email.mime.text import MIMEText
from email.header import Header

s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #get ip address
s.connect(("1.1.1.1",80))
ipaddr=s.getsockname()[0]


receiver = 'xxxxxxx@qq.com'  #information
sender = 'xxxxxxxx@qq.com'
smtpserver = 'smtp.qq.com'
username = 'xxxxxxx@qq.com'
password = 'xxxxxxxxxxxxxx' #authorization code not pw

mail_title = 'IP address' #email title
mail_body = ipaddr 

message = MIMEText( mail_body, 'plain', 'utf-8' ) 
message ['From'] = sender                                              
message['To'] = receiver                                                   
message['Subject'] = Header( mail_title, 'utf-8' ) 

smtp = smtplib.SMTP()                                                     
smtp.connect( smtpserver )                                            
smtp.login( username, password )                               
smtp.sendmail( sender, receiver, message.as_string() ) 
smtp.quit()