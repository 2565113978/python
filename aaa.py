# -*- coding: cp936 -*
import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = '2565113978@qq.com'
msg['to'] = '1164244516@qq.com'
msg['subject'] = 'test'
content = "你好,这是一封自动发送的邮件。"
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.126.com', '25')
smtp.login('2565113978@qq.com', '199707190623mcs.')
smtp.sendmail('2565113978@qq.com', '1164244516@qq.com', str(msg))
smtp.quit()