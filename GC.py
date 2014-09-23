#!/usr/bin/python

import subprocess, os, sys
from time import gmtime, strftime, sleep

def findPID(server):
    if server=="local":
        p1=subprocess.Popen("ps -ef | grep -i 'java' | grep -v 'grep' | awk '{print $2}'", stdout=subprocess.PIPE, shell=True)
    else:
        p1=subprocess.Popen("ssh "+server+" ps -ef | grep -i 'java' | grep -v 'grep' | awk '{print $2}'", stdout=subprocess.PIPE, shell=True)
    (pid, err) = p1.communicate()
    return pid

def getCurrentGCStat(server):
    pid = findPID(server)
    if server=="local":
        p1=subprocess.Popen("jstat -gc "+pid, stdout=subprocess.PIPE, shell=True)
    else:
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
duration =int(sys.argv[2])

print(serverName)
fileWrite(getCurrentGCStat(serverName),"gclog","a")
sleep(duration)
fileWrite(getCurrentGCStat(serverName),"gclog","a")

logfile = open('gclog',"r")
logfile.readline()
itemString1 = logfile.readline()
logfile.readline()
itemString2 = logfile.readline()
logfile.close()
itemlist1 = itemString1.split()
itemlist2 = itemString2.split()
out = []

out.append("\n Hostname: %s" %serverName)
out.append("\nGC Details")
out.append("\n%d Full GC happened, consumed %f seconds" % (int(itemlist2[12])-int(itemlist1[12]), float(itemlist2[13])-float(itemlist1[13])))
out.append("\n%d Young GC happened, consumed %f seconds" % (int(itemlist2[10])-int(itemlist1[10]), float(itemlist2[11])-float(itemlist1[11])))
out.append("\nTotal time spent on GC is %f seconds" %(float(itemlist2[14])-float(itemlist1[14])))
print(out)
if os.path.exists('result.log'):
    os.remove('result.log')
print("GC files cleared...")
outlog = open('result.log',"a")
outlog.writelines(out)
outlog.close()

