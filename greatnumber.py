#!/usr/bin/python3.5 -tt
#!/usr/bin/python3.5 -tt


def main():
   inputlist = [65555555,50,2,17,9,8,10,6,5,12,4,15,12,22,65555555]    
   great = findGreatNumber(inputlist)
   print('The largest number in the list {0} is {1}'.format(inputlist,great))

def findGreatNumber(listofnumbers):
    list = listofnumbers
    large = list[0]
    for i in list:
       if (large - i) < 0:
          large = i
    return(large)

if __name__ == "__main__" :
   main()
