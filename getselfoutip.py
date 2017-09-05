import smtplib
import email.mime.multipart
import email.mime.text
import os
import time


timestr = ''
timestr = time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))
print(timestr)

content = ''
command = 'curl icanhazip.com'
r = os.popen(command)
info = r.readlines()
for line in info:
    content += line

file_object = open('/home/*********/lastip')
try:
    lastip = file_object.read()
finally:
    file_object.close()
lastip = lastip.strip()
print('lastip: |' + lastip + '|')
content = content.strip()
print('content: |' + content+'|')

def sendEmail(content):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = '*********@163.com'
    msg['to'] = '*********@qq.com'
    msg['subject'] = '75出口IP变更'+timestr
    txt = email.mime.text.MIMEText(content, _subtype='html', _charset='gb2312')
    msg.attach(txt)
    smtp = smtplib
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com', '25')
    smtp.login('*********@163.com', '*********')
    # to
    smtp.sendmail('*********@163.com', '*********@qq.com', str(msg))
    smtp.quit()
    pass


if content == lastip:
    print('the are same');
else:
    sendEmail(content);
    file_object = open('/home/*********/lastip', 'w')
    file_object.write(content)
    file_object.close()