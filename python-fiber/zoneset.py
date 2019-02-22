#
#       demo vsan 10 zoning script
#
#
from itertools import izip
import subprocess
import re



#this contains the zones
z=open("h10","r")
#this file contains a list of pwwns
pw=open("v10","r")


for x,y in izip(z,pw):
        x = x.strip()
        y = y.strip()

        print "member {0}" .format(x)
	



