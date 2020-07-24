#coding:UTF-8
import pyodbc

# Database Driver name & Database File path & Database userid & password
DBdriver="Microsoft Access Driver (*.mdb, *.accdb)"
DBfile="D:/test.accdb"
DBuid=""
DBpwd=""
conn = pyodbc.connect(
    "Driver={"+DBdriver+"};"+
    "DBQ="+DBfile+";"+
    "Uid="+DBuid+";"+
    "Pwd="+DBpwd+";"
    )
cursor=conn.cursor()
# SQL sentences
SQL='''
select * 
from table1;
'''
#found a list to contain pyodbc.row
rows=[]
for row in cursor.execute(SQL):
    rows.append(row)
#test result
print(rows)
a=rows[0].username
print(type(rows[0]))
print(a)
print(type(a))

cursor.close()
conn.close
