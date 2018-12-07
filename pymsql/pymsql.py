import pymysql.cursors


# 连接MySQL数据库
connection = pymysql.connect(host='172.18.18.203', port=23306, user='root', password='root', db='guest', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)


# 通过cursor创建游标
cursor = connection.cursor()

# 执行数据查询
sql = "SELECT `id`, `password` FROM `users` WHERE `email`='huzhiheng@itest.info'"
cursor.execute(sql)

#查询数据库单条数据
result = cursor.fetchone()
print(result)

print("-----------华丽分割线------------")

# 执行数据查询
sql = "SELECT `id`, `password` FROM `users`"
cursor.execute(sql)

#查询数据库多条数据
result = cursor.fetchall()
for data in result:
    print(data)


# 关闭数据连接
connection.close()