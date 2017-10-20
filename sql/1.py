import pymysql

db=pymysql.connect('localhost','root','123456','python')
cursor=db.cursor()
# 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
# sql = """CREATE TABLE TEST (
#          ID  INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
#
# cursor.execute(sql)
# db.close()


sql="""
insert into test(ID,FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
VALUES ('%d','%s','%s','%d','%c','%d')
""" %(2,'zhou','qinghui',25,'m',3000)

try:
    cursor.execute(sql)
    print('success')
    db.commit()
except:
    db.rollback()

db.close()