# 将1中的200条优惠券信息存储到mysql数据库。

import mysql.connector
from datetime import datetime
from a import *
conn = mysql.connector.connect(user='root', password='root', database='learn-sql')
cursor = conn.cursor()
cursor.execute('create table  if not exists coupon(id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, numbering VARCHAR(30), status TINYINT, createTime TIMESTAMP, updateTime TIMESTAMP)')
now = datetime.now()

for x in new_arr:
  cursor.execute('insert into coupon (numbering, status, createTime, updateTime) values(%s, %s, %s, %s)', [x, 1, now, now])
conn.commit()
cursor.close()