#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

#set the user-agent to the one specified for kernel.com
header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0',}


#the url we want to grab the ip from
url = r'https://www.kernel.org'
#build the request, with the proper user-agent in the custom header
r = requests.get(url, headers=header)


#convert html to soup
soup = BeautifulSoup(r.content)
#find the line with the latest_link in it
# which is in a td, with id 'latest_link'
kernel = soup.findAll('td', id='latest_link')[0]
latest_kernel = BeautifulSoup(kernel.text)

print "The Latest Kernel is %s" % kernel.text
