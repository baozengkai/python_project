# -*- coding: UTF-8 -*-
import smtplib
import traceback
from email.mime.text import MIMEText

"""
    配置smtp服务器，由163向qq发送邮件
    注意点:
        1.网易邮箱和qq邮箱都需要开通pop3、IMAP、SMTP协议
        2.网易邮箱还需要开通客户端授权密码，下面出现的密码也是授权码
        3.不要用菜鸟上那个教程，该教程在本例子下有误
"""

# 测试
mail_host = "smtp.163.com"
mail_user = "m17702137349@163.com"
mail_pass = "1314101hehe"

sender = 'm17702137349@163.com'
receivers = ['421557259@qq.com']
subject = "cesi"

message = MIMEText('123', 'plain', 'utf-8')
message['From'] = "m17702137349@163.com"
message['To'] = "421557259@qq.com"
message['Subject'] = subject

try:
    smtpObj = smtplib.SMTP(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "发送成功"
except smtplib.SMTPException as e:
    print str(smtplib.SMTPException)
    print traceback.print_exc()
