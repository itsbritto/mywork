GC


Script to get the GC details for given hostname

command

./GC.py local 5

local - running on test box
5- duration in seconds

./GC.py 10.10.10.10 5

10.10.10.10 - host box ( you need ssh permission)

ssh without password 

http://brittoc.wordpress.com/2011/07/12/ssh-login-without-password/


Output:

Hostname: local
GC Details
27 Full GC happened, consumed 13.709000 seconds
139 Young GC happened, consumed 92.277000 seconds
Total time spent on GC is 105.987000 seconds



