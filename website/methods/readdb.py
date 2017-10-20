
from website.methods.db import *

def select_table(col,table,condition,value):
    sql="select "+col+" from "+table+" where "+condition+"= '"+value+"'"
    cursor.execute(sql)
    lines=cursor.fetchall()
    return lines

def insert_table(table,username,password):
    # 此处sql语句注意引号和空格的位置
    sql="insert into %s(username,password) values ('%s','%s')" % (table,username,password)
    cursor.execute(sql)
    db.commit()
    return 'success'

def select_cols(table,col):
    sql="select "+col+" from "+table
    cursor.execute(sql)
    lines = cursor.fetchall()
    return lines