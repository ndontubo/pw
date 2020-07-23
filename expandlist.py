#!/usr/bin/python3.5 -tt


import sys
import os

def main():
  newlist = []
  #list = [1,2,[3,4,[5,6],7],8,9]
  list = [1,[2,3],4,5,6,7,8,9]
  for i in list:
    print('in i', type(i))
    if type(i) is list:
	for j in i:
          print('in j')
	  if type(j) is list:
	     for k in j:
	       print('in k')
	       newlist.append(k)
	  else:
	      newlist.append(j)
	#print(i)
    else:
	newlist.append(i)
	
        
  print(newlist)
 
def isitalist(list):
  length = len(list)
  print(length)
  if (lenght > 1):
     return(1)
  else:
     return(0)
 
if __name__ == '__main__':
  main()

