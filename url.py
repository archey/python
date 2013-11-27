#!/usr/bin/env python
import requests

header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0',}

url= r"https://piratebay.sx"
r = requests.get(url, headers=header, verify=False)
print r.content
