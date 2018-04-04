#!/usr/bin/python
import socket

s = socket.socket()
host = socket.gethostname()
port = 30277  s.connect((host, port))
string = s.recv(130)
split = string.split("'")

char = “u”
repeat = 528
end = "3"
ret = "" 

for i in range(0, int(repeat)):
    ret += char
else:
    ret += end 
print s.recv(46) 
print(str(ret))
s.send(str(ret))
print s.recv(20)
s.close()
