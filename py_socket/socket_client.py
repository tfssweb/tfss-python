#客户端
import socket
#创建socket对象
client_send = socket.socket()
#确定IP
ip_port = ("localhost", 10010)
#建立客户端链接
client_send.connect(ip_port)

while True:
    #发送消息
    msg = input("请输入消息：")
    if len(msg) == 0:
        continue
    elif msg == "exit":
        break
    client_send.sendall(bytes(msg, encoding="utf-8"))
    #接受消息
    data = client_send.recv(1024)
    print(str(data, encoding="utf-8"))

#断开链接
client_send.close()
