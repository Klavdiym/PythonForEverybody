#PORT = 80

#URL = input('Please enter URL: ')
#if URL[0] == 'w' or URL[0] == 'W':
#        URL = 'http://'+ URL
#elif URL[0:3] != 'www.':
  #  URL = 'http://www.'+URL
#
#try:
 #   urlSplit = URL.split('/')
#except:
#    quit('Error: Improper URL formatting')

#try:
 #   HOST = urlSplit[2]
#except:
  #  quit('Error: Improper URL formatting')
#print(HOST)
#socket.getaddrinfo('localhost', 8080)

#mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mySock.connect((URL, PORT))

#while True:
   # data = mySock.recv(5120)
  #  if len(data) < 1:
    #    break
    #time.sleep(0.1)
   # count = count + len(data)
   # print(len(data), count)
   # picture = picture+data

#mySock.close()


#URL = input('Please enter URL: ')
#mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#HOST = URL.split('/')[2]
#mySock.connect((HOST, 80))
#toSend = ('GET' + ' ' + URL + ' ' + 'HTTP/1.0\r\n\r\n').encode()
#mySock.send(toSend)

#count = 0
#while True:
 #   data = mySock.recv(512)
 #   count += len(data)
  #  if (len(data) < 1) or (count >= 3000): break
  #  print(data.decode(), end='')
#mySock.close()
#print(count)
#import socket
#import urllib.request

#count = 0
#fhand = urllib.request.urlopen(input('Open URL: '))
#for line in fhand:
 #   count = count + len(line)
 #   if count >= 9000:
  #      print("Maximum value")
    #    quit()
  #  print(line.decode().strip())

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the paragraph tags
tags = soup('p')
print(len(tags))
#for tag in tags:
   # print(tag)