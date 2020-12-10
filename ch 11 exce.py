import socket
import urllib.request

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
count = 0
fhand = urllib.request.urlopen(input('Open URL: '))
for line in fhand:
    count = count + len(line)
    if count >= 3000:
        print("Maximum value")
        quit()
    print(line.decode().strip())
