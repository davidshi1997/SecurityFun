#!/usr/bin/python#!/usr/bin/python
f = open('littleschoolbus.bmp', 'rb')
data = bytearray(f.read())
out = ""
for byte in data[54:]:
    out += str(byte & 1)
print out
