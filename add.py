#!/usr/bin/python3.5 -tt
#!/usr/bin/python3.5 -tt


def main():
    while 1 :
        prompt=raw_input('what do you add two numbers? y or n ')
    	if prompt == 'y':
       		addTwoNum()
		return
    	elif prompt == 'n':
		print('Thank you')
		return
    	else:
       		prompt = raw_input('Please type letter y for adding number or type letter no for come out from this procedure. Typing any other letter now will abort the program. Please type "y" or "n" :   ')
		if prompt == 'y':
			break
		elif prompt == 'n':
			continue
		else :
			print('Thank you , you have chosen to exit this program')
			return



def addTwoNum():
    num1 = int(input("enter 1st number:"))
    num2 = int(input('enter 2nd number:'))
    sum = num1+num2
    print ('Sum of numbers {0} and {1} is {2}'.format(num1,num2,sum))


if __name__ == "__main__" :
   main()
