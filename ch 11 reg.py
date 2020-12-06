import re

count = 0
hand = open('C:\\Users\\GamerPC\\Downloads\\mbox.txt')
command = input('Enter regular expression: ')
command = str(command)

for line in hand:
    line = line.rstrip()
    regexMatch = re.findall(command, line)
    if len(regexMatch) > 0:
        count += 1
print('mbox.txt has %g items matching' % count, command,  'regex command' )


#for line in hand:
   # line = line.rstrip()
    #if re.search('^F..m:', line):
      #  print(line)
#for line in hand:
#        line = line.rstrip()
#        x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
#        if len(x) > 0:
#            print(x)
#hand = open('C:\\Users\\GamerPC\\Downloads\\mbox.txt')
#for line in hand:
#    line = line.rstrip()
#    if re.search('^X\S*: [0-9.]+', line):
#        print(line)
#s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
#lst = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', s)
#print(lst)

#fhand = open('C:\\Users\\GamerPC\\Downloads\\mbox.txt')
#for line in fhand:
#    line = line.strip()
#    x = re.findall('^X\S*: ([0-9.]+)', line)
#    if len(x) > 0:
#        print(x)

#hand1 = open('C:\\Users\\GamerPC\\Downloads\\mbox.txt')
#for line1 in hand1:
#    line1 = line1.rstrip()
#    x1 = re.findall('^Details:.*rev=([0-9.]+)', line1)
#    if len(x1) > 0:
#        print(x1)