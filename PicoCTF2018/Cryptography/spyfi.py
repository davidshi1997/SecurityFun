#!/usr/bin/python2 -u
from pwn import *

def main():
    flag = "picoCTF{"
    block = "de is: picoCTF{"
    incomplete = True

    while incomplete:
        for i in range(32,128):
            q = remote('2018shell3.picoctf.com', 31123)
            q.recvuntil('Please enter your situation report: ')
            msg = 'A'*11+block+chr(i)+"B"*(48-len(flag))
            q.sendline(msg)
            size = 400-(len(flag)/16)*16
            enc_rcv = q.recvn(size).decode('hex')
            q.close()
            if enc_rcv[64:80] == enc_rcv[144:160]:
                flag += chr(i)
                block = block[1:]+chr(i)
                if chr(i) == '}':
                    incomplete = False
                break
    print(flag)

main()