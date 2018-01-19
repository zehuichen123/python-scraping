#!/usr/bin/env python3
# encoding: utf-8
import requests
'''using cookie by import manually
cookie={}
cookie_raw='bid=k86QP9e_ikc; __yadk_uid=2RMKcINjdFCwt5ESQtf26clVJdXqTDEq; gr_user_id=eca3edb0-a1a8-42d3-a6fe-c0eef0d157f1; ll="108296"; _vwo_uuid_v2=BB93221C39E7E912FA5A3084152EDF74|c4c49b3ebfe17acb44c5c4712b3fdec0; __utmc=30149280; ap=1; viewed="27061630_26945535"; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1516103807%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1440207950.1511260631.1515828240.1516103808.9; __utmz=30149280.1516103808.9.9.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; _ga=GA1.2.1440207950.1511260631; _gid=GA1.2.876665339.1516103817; _gat_UA-7019765-1=1; dbcl2="152654498:f+IckSQodPE"; ck=Ctqr; _pk_id.100001.8cb4=4fe2f09967b87834.1511260631.5.1516103820.1515650018.; push_noty_num=0; push_doumail_num=0; __utmv=30149280.15265; __utmb=30149280.3.10.1516103808'
for line in cookie_raw.split(';'):
    key,value=line.split('=',1)
    cookie[key]=value

print(cookie)
url='https://www.douban.com/people/152654498/'
req=requests.get(url,cookies=cookie)
print(req.text)
'''
form_data={
    'source':None,
    'redir':'https://www.douban.com/people/152654498/',
    'form_email':'18117352126',
    'form_password':'chlxgy5573108',
    'login':'登录',
}
url='https://www.douban.com/login'
req=requests.post(url,data=form_data)