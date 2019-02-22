
import os

#this loop will add colons : to a wwn 

with open("sed", "r") as lines:
    for line in lines:
        ip = line.strip()
        if ip <> "":
            print "resetting ", ip
            cmd = "echo {0} | sed 's/../&:/g;s/:$//'" .format(ip)
            retvalue = os.system(cmd)
            print retvalue
