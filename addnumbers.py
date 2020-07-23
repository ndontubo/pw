#!/usr/bin/python3.5 -tt


import sys
import os
inputarguments = sys.argv
print (inputarguments)
def add():
  print ("This is two number addition")
  num1 = int(input("Enter number1:"))
  num2 = int(input("Enter number2:"))
  num = num1 + num2
  print ('Sum of the {0} , {1} is {2}'.format(num1,num2,num))
  extra = raw_input('Do you want find sum even or odd: "Y or N"  ') 
  if (extra == 'Y'):
     eveOdd(num)
  else :
     print ('Thank you')
def eveOdd(num):
    if (num % 2 == 0): 
       print ('This is even number') 
    else :
       print ('This is odd number') 
def febo():
    cnt = int(input("Enter the febonaci range. eg 4 or 10 100"))
    pyrmid = raw_input("Do you also want pyramid : Y or N")
    a = 0
    b = 1
    febList = [a,b]
    for i in range(cnt-2):
	c = a+b
	febList.append(c)
	a = b
	b = c
    return febList

def main():
  febonacilist = febo()
  print(febonacilist)
  urname = raw_input('Enter you name please :  ')
  print ('########################################')
  print ("Hello" + ' ' + urname + ' Thank you for using this program')
  print ('########################################')
  inc = raw_input('Do you want add two numbers "Y or N"  : ')
  if (inc == 'Y') :
    while (inc == 'Y' ) :
      add()
      inc = raw_input('Do you want to continue add two numbers "Y or N" : ')
      if (inc == 'N') :
        print ("Wonderful, Thank you !!!")
	return 
  elif (inc == 'N') :
    print ("Thank you !!!")
  else :
    print ("Oops , wrong input,")
    main()

if __name__ == '__main__':
  main()

