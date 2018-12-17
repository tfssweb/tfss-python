# flask+webuploader实现大文件上传
----
使用步骤：

1. git clone https://github.com/tfssweb/pythons.git
2. pip install -r requirement.txt
3. mkdir upload
4. gunicorn -w4 -k gevent -b 0:34567 run:app
5. 访问`ip:34567`即可

---
![](test.png)
