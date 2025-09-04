import mysql.connector

# 连接数据库
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sF$8kL!pQ2vB&m9*",
    database="mysql"
)

cursor = conn.cursor()

# 执行查询
cursor.execute("SELECT user,host FROM user")
result = cursor.fetchall()
for row in result:
    print(row)

# # 插入数据
# sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
# val = ("Bob", 25)
# cursor.execute(sql, val)
# conn.commit()  # 提交事务
# print(cursor.rowcount, "记录插入成功")

# 关闭连接
cursor.close()
conn.close()