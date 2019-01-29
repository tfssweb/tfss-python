#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


def sendEmail():
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置QQ服务器
    # mail_host = "smtp.exmail.qq.com"  # 设置公司服务器
    mail_user = "michaelq@qq.com"  # 用户名
    mail_pass = "Michael"  # 口令

    sender = 'michael@qq.com'
    to_reciver =['xxx@qq.com']
    cc_reciver = ['1255791430@qq.com']

    receivers = to_reciver + cc_reciver # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    print(receivers)

    mail_msg = """
                   <html>
                     <head> 
                      <title>警报</title> 
                      <style type="text/css">
                        /* gridtable */
                        table.gridtable {
                        font-size:11px;
                        color:#333333;
                        border-width: 1px;
                        border-color: #666666;
                        border-collapse: collapse;
                        }
                        table.gridtable th {
                        border-width: 1px;
                        padding: 8px;
                        border-style: solid;
                        border-color: #666666;
                        background-color: #dedede;
                        }
                        table.gridtable td {
                        border-width: 1px;
                        padding: 8px;
                        border-style: solid;
                        border-color: #666666;
                        background-color: #ffffff;
                        text-align:center
                        }
                        .exp{font-size:16px; text-indent:32px}
                      </style> 
                     </head> 
                     <body> 
                      <div> 
                       <p>您好：</p> 
                       <p class="exp">爬虫在爬取<span style="color:red;">2019年01月13日12时</span>国省控数据时发生异常，请及时登录<span style="color:blue;">127.0.0.1</span> 服务器进行查看。</p> 
                       <h4>登录方式如下：</h4> 
                      </div> 
                      <div> 
                       <table class="gridtable"> 
                        <tbody>
                         <tr> 
                          <th>IP</th> 
                          <th>USERNAME</th> 
                          <th>PASSWORD</th> 
                         </tr> 
                         <tr> 
                          <td>192.168.13.10</td>
                          <td>root</td>
                          <td>C***8</td> 
                         </tr> 
                        </tbody>
                       </table> 
                      </div> 
                      <div> 
                       <p><a href="http://www.tfssweb.com/">颓废书生</a></p> 
                      </div>   
                     </body>
                    </html>
                """

    # html plain
    message = MIMEText(mail_msg, 'html', 'utf-8')

    message['From'] = Header("张家口智慧环保平台", 'utf-8')  # 发送人
    # message['To'] = Header("运维组", 'utf-8')  # 接收人
    # message['Cc'] = Header("运维组", 'utf-8')  # 接收人
    message['To'] = ";".join(to_reciver)  # 接收人
    message['Cc'] = ";".join(cc_reciver)  # 接收人


    subject = '异常提醒'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功！")

    except smtplib.SMTPException:
        print("Error: 邮件发送失败！")


if __name__ == '__main__':
    sendEmail()