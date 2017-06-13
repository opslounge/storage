#
#       demo vsan 20 zoning script
#
#
from itertools import izip
import subprocess
import re


#zoning for demo nodes in rack b08
zold = """
member pwwn 52:4a:93:7a:b5:44:7f:02
member pwwn 52:4a:93:7a:b5:44:7f:12
member pwwn 52:4a:93:79:be:55:2c:02
member pwwn 52:4a:93:79:be:55:2c:12
member pwwn 52:4a:93:77:2d:2d:54:01
member pwwn 52:4a:93:77:2d:2d:54:11
member pwwn 52:4a:93:77:2d:2d:54:00
member pwwn 52:4a:93:77:2d:2d:54:10
member pwwn 52:4a:93:77:2d:2d:54:07
member pwwn 52:4a:93:77:2d:2d:54:17
"""
#zoning for demo nodes in rack b07
v= """
member pwwn 52:4a:93:7a:b5:44:7f:02
member pwwn 52:4a:93:7a:b5:44:7f:12
member pwwn 52:4a:93:7a:d1:8c:3d:03
member pwwn 52:4a:93:7a:d1:8c:3d:13
member pwwn 52:4a:93:7a:d1:8c:3d:11
member pwwn 52:4a:93:7a:d1:8c:3d:01
"""

#this contains the zones
z=open("h20","r")
#this file contains a list of pwwns
pw=open("v20","r")


for x,y in izip(z,pw):
        x = x.strip()
        y = y.strip()
        print "zone name {0} vsan 20 \n member pwwn {1}" .format(x,y)
	print v
#	print "zone name {0}" .format(x,)
