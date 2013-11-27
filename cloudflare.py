#! /usr/bin/env python
import json
import requests
 
data = {'a': 'rec_load_all','tkn': "d25237c11898bc00914be18d1d8df7933ac8e", 'u': "tylerb@trix2voip.com", 'z': "kingswatchrepair.com"}
 
url = r"https://www.cloudflare.com/api_json.html"
 
r = requests.post(url, data=data)
j = json.dumps(r)
print r.headers
print j
#print r.text['response']
