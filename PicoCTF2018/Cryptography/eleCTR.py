from pwn import *
from base64 import b64decode, b64encode

def xor(s1, s2):
	s = ''
	for a, b in zip(s1, s2):
		s += chr(ord(a) ^ ord(b))
	return s

def main():
	r = remote('2018shell3.picoctf.com', 36150)
	r.recvuntil('Please choose: ')

	r.sendline('i')
	flag_plain = r.recvuntil('Please choose: ').split('\n')[2].strip()

	known_plain = 'aaaaaaaaaaaaaaaaaaaaaaaaa'
	r.sendline('n')
	r.sendline(known_plain)
	r.sendline('a')
	known_cipher = b64decode(r.recvuntil('Please choose: ').split('\n')[2])

	flag_cipher = b64encode(xor(flag_plain, xor(known_cipher, '{}.txt'.format(known_plain))))
	r.sendline('e')
	r.sendline(flag_cipher)
	solution = r.recvuntil('Please choose: ')

	r.close()

	print(solution)

main()