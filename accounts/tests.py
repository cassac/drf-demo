# from django.test import TestCase

import requests

# with requests.Session() as s:
# 	url = "http://localhost:8000/api-auth/login/"
# 	s.get(url)
# 	csrftoken = s.cookies['csrftoken']
# 	cookies = dict(s.cookies)
# 	payload = {'username': 'u1', 'password': 'user', 'next': 'http://localhost:8000/users/'}
# 	headers = {"X-CSRFToken":csrftoken}
# 	p = s.post(url, data=payload, headers=headers, cookies=cookies)

url = "http://localhost:8000/users/1/fortunes/"
# r = requests.post(url)
# csrftoken = s.cookies['csrftoken']
# cookies = dict(s.cookies)
payload = {'content': ['new fortune yes!']}
files = {'pictures': open('/home/c/Desktop/pro.jpeg', 'rb')}
# headers = {"X-CSRFToken":csrftoken}
p = requests.post(url, data=payload, files=files)#, headers=headers, cookies=cookies)
print p