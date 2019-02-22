#
#       demo vsan 10 zoning script
#
#
from itertools import izip
import subprocess
import re


#for zoning nodes in rack b08
notz = """
member pwwn 52:4a:93:79:be:55:2c:00
member pwwn 52:4a:93:79:be:55:2c:10
member pwwn 52:4a:93:7a:b5:44:7f:00
member pwwn 52:4a:93:7a:b5:44:7f:10
member pwwn 52:4a:93:77:2d:2d:54:02
member pwwn 52:4a:93:77:2d:2d:54:12
member pwwn 52:4a:93:77:2d:2d:54:03
member pwwn 52:4a:93:77:2d:2d:54:13
member pwwn 52:4a:93:77:2d:2d:54:06
member pwwn 52:4a:93:77:2d:2d:54:16
"""

#for zoning nodes in rack b07
v = """
 member pwwn 52:4a:93:7a:d1:8c:3d:02
 member pwwn 52:4a:93:7a:d1:8c:3d:12
 member pwwn 52:4a:93:7a:b5:44:7f:00
 member pwwn 52:4a:93:7a:b5:44:7f:10
 member pwwn 52:4a:93:7a:d1:8c:3d:00
 member pwwn 52:4a:93:7a:d1:8c:3d:10
"""

#this contains the zones
z=open("h10","r")
#this file contains a list of pwwns
pw=open("v10","r")


for x,y in izip(z,pw):
        x = x.strip()
        y = y.strip()

        print "zone name {0} vsan 10 \n member pwwn {1}" .format(x,y)
	print v
	
#	print "zone name {0}" .format(x,)



