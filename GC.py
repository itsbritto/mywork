#!/usr/bin/python

import subprocess, os, sys
from time import gmtime, strftime

def findPID(server):
    p1=subprocess.Popen("ssh "+server+" ps -ef | grep -i 'java' | grep -v 'grep' | awk '{print $2}'", stdout=subprocess.PIPE, shell=True)
    (pid, err) = p1.communicate()
    return pid

def getCurrentGCStat(server):
    pid = findPID(server)
    p1=subprocess.Popen("ssh "+server+" jstat -gc "+pid, stdout=subprocess.PIPE, shell=True)
    (gcstat, err) = p1.communicate()
    return gcstat


def fileWrite(msg, filename, mode):
    fileop = open(filename, mode)
    fileop.write(msg)
    fileop.close()
    return

if os.path.exists('gclog'):
        os.remove('gclog')
print("Temp files cleared...")
serverName =  str(sys.argv[1])

print(serverName)
fileWrite(getCurrentGCStat(serverName),"gclog","a")
