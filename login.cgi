#!/usr/bin/python2
import cgi,cgitb
cgitb.enable()
print "Content-type:test/html"
print ""
data=cgi.FieldStorage()
email=data.getvalue('e')
password=data.getvalue('p')

print email
print password
conn=mysql.connect(user='root',password='123',host='localhost', database='adhoc')
cur=conn.cursor()
cur.execute("select email and pasword from student")
output=cursor.fetchall()


