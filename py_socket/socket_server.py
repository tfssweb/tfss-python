#服务器端
import socket

server_receive = socket.socket()
#确定IP
ip_port = ("localhost", 10010)
#bind()绑定
server_receive.bind(ip_port)
#listen监听
server_receive.listen(5)
#建立客户端链接
#accept 接受请求链接
conn, addr = server_receive.accept()
while True:
    #接受数据
    data = conn.recv(1024)
    if not data:
        break
    else:
        #输出数据
        print(str(data, encoding="utf-8"))
    msg = input("请回复：").strip()
    if len(data) == 0:
        continue
    conn.sendall(bytes(msg, encoding="utf-8"))
#关闭连接
conn.close()
server_receive.close()
