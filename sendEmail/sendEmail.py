import requests
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import datetime as d
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

receiver = 'michael.liu@chinaentropy.com' #收件人邮箱
sender_qq = '1255791430' #发件人qq号
pwd = 'xxx' #qq邮箱授权吗
sender_qq_mail = '1255791430@qq.com' #发件人qq邮箱
sender_qq_mail = '1255791430@qq.com' #发件人qq邮箱
mail_title = d.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")

def pastebin(content,type): #content为文本，type为代码语言
    headers={  #请求头
    "User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Upgrade-Insecure-Requests':'1',
    'Origin':'https://paste.ubuntu.com',
    'Referer':'https://paste.ubuntu.com/',
    'Host':'paste.ubuntu.com',
    'Content-Type':'application/x-www-form-urlencoded',
    'Content-Length':'100',
    'Connection':'keep-alive',
    'Cache-Control':'max-age=0',
    'Accept-Language':'zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'Accept-Encoding':'Accept-Encoding',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }
    datas={ #请求数据
    "poster":"Yang",
    "syntax":type,
    "expiration":"",
    "content":content
    }
    url="https://paste.ubuntu.com/"
    r=requests.post(url, data = datas,headers=headers)
    return r.url



def made_text(mail_content):
    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    return msg


def made_photo(file_name):
    msg = MIMEMultipart()
    body = """
        <h3>Hi，all</h3>
        <p>附件为本次FM_自动化测试报告。</p>
        <p>请解压zip，并使用Firefox打开index.html查看本次自动化测试报告结果。</p>
        <p>
        <br><img src="cid:image1"></br> 
        </p>
        <p>
    """
    mail_body = MIMEText(body, _subtype='html', _charset='utf-8')
    msg.attach(mail_body)
    fp = open("/home/yang/"+file_name, 'rb')
    images = MIMEImage(fp.read())
    fp.close()
    images.add_header('Content-ID', '<image1>')
    msg.attach(images)
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver

    return msg

def made_file(file_name):
    att = MIMEText(open('/home/yang/'+file_name, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename=file_name'
    msg = MIMEMultipart('mixed')
    msg.attach(att)
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver

    return msg

def made_code(content):
    code=open('/home/yang/'+content[0]).read()
    mail_content=pastebin(code,content[1])
    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver

    return msg


def send_mail(msg):
    host_server = 'smtp.qq.com'
    sender_qq_mail = sender_qq+'@qq.com'
    smtp = SMTP_SSL(host_server)
    smtp.set_debuglevel(0)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    try:
        smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    except:
        print("邮件发送失败！！")
    else:
        print("邮件发送成功")
    finally:
        smtp.quit()\

def selet(opnion):
    content=input("文件名或内容，代码则以空格分割文件名与type：\n").split()
    if (len(content)==1):
        content=str(content[0])
    number={
        "1":made_text,
        "2":made_photo,
        "3":made_file,
        "4":made_code
    }
    msg=number[opinion](content)
    send_mail(msg)


if __name__ == "__main__":
    print("1:text\n2:photo\n3:file\n4:code")
    opinion=input("opinion:\n")
    selet(opinion)