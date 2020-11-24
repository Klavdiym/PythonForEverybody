#def chop(shortList):
#    x = len(shortList)
#    t = shortList.pop(x-1)
#    t = shortList.pop(0)

#def middle(middleList):
#    x = len(middleList)
#    centerList = middleList[1:x-1]
#    return centerList

#t = ['Stallone', 'Van-Damm', 'Norris', 'Schwarznegger', 'Rocky', 'Terminator']

#j = middle(t)
#chop(t)

#print(t, j)

#fhand = open('C:\\Users\\Lordicode\\Desktop\\mbox-short.txt')
#count = 0
#for line in fhand:
    #words = line.split()
    #print('Debug:', words)
   # if len(words) == 0 or words[0] != 'From' or len(words) < 3 :
  #      continue
 #   else :
#        print(words[2])

#romeoList = []

#fRomeoOpen = open('C:\\Users\\Lordicode\\Desktop\\romeo.txt')
#for line in fRomeoOpen:
    #word = line.rstrip().split()
    #element = word
    #if element in romeoList:
    #    continue
    #else:
    #    romeoList.append(element)


#print(sorted(romeoList))
#count = 0
#mail = open(input('Location of mailbox data: '))
#for line in mail:
   # if line.startswith('From'):
      #  count = count + 1
      #  x = line.split()
      # try:
       #     print(x[1:2])

       # except:
       #     print('Our of index')
      #      quit()
#print("There are %d sender's adresses in the file" % count)
#C:\Users\Lordicode\Downloads\mbox-short.txt
#smallest = None
#biggest = 0

floatsToCompare = []

while True:
    toList = input('What integer to add? - ')
    try:
        if toList == 'done':
            print(floatsToCompare)
            print(max(floatsToCompare))
            print(min(floatsToCompare))
        if toList not in floatsToCompare:
            floatsToCompare.append(toList)

    except:
        print('Error')


    #try:
     #   toList = float(toList)
     #   if smallest is None:
     #       smallest = toList
     #   if toList < smallest:
       #     smallest = toList
      #  elif toList > biggest:
      #      biggest = toList
   # except:
     #   print('Type in integer or float')

    #if toList == 'done':
    #    print('Smallest: %f' % smallest, 'Biggest: %f' % biggest)
    #    quit()
