#!/usr/bin/python2

import commands
import cgi
import time 
import os
import cgitb


print "Content-Type: text/html"
print ""

data=cgi.FieldStorage()


# Get filename here.

d_type=data.getvalue('t')
drive_name=data.getvalue('sn')
drive_size=data.getvalue('ss')

print "documnet type : "
if d_type =='d':
	print "data" 
elif d_type =='m':
	print "music" 
elif d_type =='w':
	print "web" 
print "drive name : ", drive_name 
print "drive size : ", drive_size 



