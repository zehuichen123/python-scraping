#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: lovesnowbest
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
 
sender='672604803@qq.com'
password='jkledvzxulydbdgg'   #就是上面的那张照片里的密码
user='lovesnowbest@gmail.com' #这里可以指定发给多个人
def mail():
    ret=True
    try:
        #邮件的内容
		msg=MIMEText('xxx 我喜欢你😘','plain','utf-8')
		#括号内对应发件人的昵称和发件人的账号
		msg['From']=formataddr(["loveSnowBest",sender])
		#括号内对应收件人的昵称和收件人的账号
		msg['To']=formataddr(["xxx",user])
		#邮件的主题
		msg['Subject']="表白💕～"
		#发件人邮箱中的SMTP服务器
		server=smtplib.SMTP_SSL("smtp.qq.com",465)
		#登陆
		server.login(sender,password)
		#括号内对应发件人，收件人，邮件信息
		server.sendmail(sender,[user,],msg.as_string())
		server.quit()
	# 如果 try 中的语句没有执行，则会执行下面的 ret=False
    except Exception:  
        ret=False
    return ret

ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")