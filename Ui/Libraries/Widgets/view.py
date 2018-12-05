#!/usr/bin/python3

import pymysql

import plotly.plotly as py

import plotly.graph_objs as pg
# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "mysql")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
lists = [[], []]
lists[0].append('YOLO')
lists[0].append('SSD')
lists[0].append('MaskRCNN')
lists[0].append('FasterRCNN')

# 使用 execute()  方法执行 SQL 查询
cursor.execute("select avg(time) from algorithmtime where algorithm='YOLO';")
rows = cursor.fetchone()
print(rows)
lists[1].append(rows[0])
cursor.execute("select avg(time) from algorithmtime where algorithm='SSD';")
rows = cursor.fetchone()
print(rows)
lists[1].append(rows[0])
print(lists)
cursor.execute("select avg(time) from algorithmtime where algorithm='MaskRCNN';")
rows = cursor.fetchone()
lists[1].append(rows[0])
cursor.execute("select avg(time) from algorithmtime where algorithm='FasterRCNN';")
rows = cursor.fetchone()
lists[1].append(rows[0])


# print(lists)

# print(lists[0])

# print(([x[0] for x in lists]))

date_time = pg.Bar(x=lists[0], y=lists[1], name='运行时间')


data = [date_time]

# barmode = [stack,group,overlay,relative]

layout = pg.Layout(barmode='group', title="Average running time of the algorithm")

fig = pg.Figure(data=data, layout=layout)
py.sign_in('templarz', 'PtKMjV9gAzINZqmQRU4T')
py.image.save_as(fig, filename='algorithmtime.png')

from IPython.display import Image
Image('algorithmtime.png')


# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()

#
# -*- coding: utf-8 -*-

# import numpy

# import MySQLdb
#
# import plotly.plotly
#
# import plotly.graph_objs as pg
#
# host = "localhost"
#
# port = 3306
#
# user = "root"
#
# passwd = "mysql"
#
# charset = "utf8"
#
# dbname = "test"
#
# conn = None
#
# try:
#
#     conn = MySQLdb.Connection(
#
#         host=host,
#
#         port=port,
#
#         user=user,
#
#         passwd=passwd,
#
#         db=dbname,
#
#         charset=charset
#
#     )
#
#     cur = conn.cursor(MySQLdb.cursors.DictCursor)
#
#     cur.execute("select * from demo;")
#
#     rows = cur.fetchall()
#
#     # rows = numpy.array(rows)
#
#     lists = [[], [], [], []]
#
#     for row in rows:
#         lists[0].append(row["product"])
#
#         lists[1].append(row["price"])
#
#         lists[2].append(row["quantity"])
#
#         lists[3].append(row["amount"])
#
#     # print(lists)
#
#     # print(lists[0])
#
#     # print(([x[0] for x in lists]))
#
#     date_price = pg.Bar(x=lists[0], y=lists[1], name='价格')
#
#     date_quantity = pg.Bar(x=lists[0], y=lists[2], name='数量')
#
#     date_amount = pg.Bar(x=lists[0], y=lists[3], name='总价')
#
#     data = [date_price, date_quantity, date_amount]
#
#     # barmode = [stack,group,overlay,relative]
#
#     layout = pg.Layout(barmode='group', title="各产品销售情况")
#
#     fig = pg.Figure(data=data, layout=layout)
#
#     plotly.offline.plot(fig, filename="C:/Users/huangzecheng/Desktop/test.jpg")
#
#
#
# finally:
#
#     if conn:
#         conn.close()
#
#
