#
#   Made by Andy Parsons
#this script takes wwns with out : and inserts : in the correct format.
#requires a txt file called "wn" with a list of fibre channel pwwn's 

import os

with open("wn", "r") as lines:
    for line in lines:
        ip = line.strip()
        if ip <> "":
            cmd = "echo " + "'" + ip + "'" + "| sed 's/../&:/g;s/:$//'"
            retvalue = os.system(cmd)
