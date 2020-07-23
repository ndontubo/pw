#!/usr/bin/python3.5 -tt

"""
Author : Nav Dontuboyina
This is the ai program to chat with anyone
"""

'''
download modules
'''
import sys
import os
import time
import re
import datetime
from datetime import timedelta

'''
define global variables
'''
curse_words = ['rascal','penta']


"""
The main program
"""
def main():

	global chat_name,curse_words
	
	enter_time = datetime.datetime.now()
	while True:
		#enter_time = datetime.datetime.now()
		come_to_chat = input('HELLO HAVE YOU COME TO CHAT? Y/N : ')
		if come_to_chat == 'y' or come_to_chat == 'Y':
			who_r_u = input('SO WHO ARE YOU, WRITE YOU NAME : ')
			print('HELLO {0}'.format(who_r_u))
			time.sleep(1) 
			print('I MIGHT AS WELL TELL YOU ABOUT MY NAME...')	
			time.sleep(1)
			print('UMMM...THE PROBLEM IS I DONT HAVE ONE ')
			time.sleep(1)
			print('HEY SINCE U ARE HERE {0}'.format(who_r_u))
			chat_name = input('GIVE ME A NAME : ')	
			if checkForCurse(chat_name):
				continue
			print('THANKS FOR THE NAME, {0}'.format(who_r_u))
			time.sleep(1)
			age_of_user = int(input('BTW, HOW OLD ARE YOU? : '))
			res = verifyAge(age_of_user)
			if not res:
				print('YOu have entered {0} and which is not acceptable for age'.format(age_of_user))
				
			
		elif come_to_chat == 'n' or come_to_chat == 'N':
			print('OK THEN, SEE YOU NEXT TIME')
			break
	if come_to_chat == 'n' or come_to_chat == 'N':
	    if isvarthere('who_r_u') and isvarthere('chat_name'):
		    print('BYE {0} ....SEE YOU AGAIN..YOUR {1} WILL BE HERE'.format(who_r_u,chat_name))
	    else:
		    print('BYE...SEE YOU AGAIN..I WILL BE WAITING')
	exit_time = datetime.datetime.now()
	time_spent = calcTime(enter_time, exit_time)
	print('#' * 30)
	print('THANK YOU FOR SPENDING {0} SECOND(S) TOGETHER'.format(time_spent))
	print('#' * 30)
	return



"""
Classes if any
"""


'''
Supporting methods,functions
'''

def calcTime(time1, time2):
	#datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
	#datetimeFormat = "%d/%m/%Y %H:%M:%S"
	timeFormat = "%H:%M:%S"
	date1 = time1.strftime(timeFormat)
	date2 = time2.strftime(timeFormat)
	dtime1 = datetime.datetime.strptime(date1, timeFormat )
	dtime2 = datetime.datetime.strptime(date2, timeFormat)
	diff = dtime2 - dtime1
	t_in_sec = diff.seconds
	return(t_in_sec)
	
def isvarthere(var):
    var_exists = var in locals() or var in globals()
    return var_exists

def checkForCurse(word):
    if word in curse_words:
    	print('DO YOU REALLY THINK YOU ARE THAT FUNNY')
    	time.sleep(1)
    	print('BUT FINE')
    	print('ANYWAYS')
    	time.sleep(1)
    	return 

def checkForCurseKid(wordkid):
	global curse_words
	if wordkid in curse_words:
	    print("DID'NT YOU SAY A BAD WORD SOMETIME AGO")
	    time.sleep(1)
	    print('I WANT TO HAVE A TALK WITH YOUR MOM...BUT ANYWAYS')
	    print("YOU SHOULD'NOT TELL PEOPLE YOUR AGE AT THIS STAGE OF YOUR LIFE")
	    time.sleep(1)
	    print('MAYBE WHEN YOU ARE AN ADULT...BUT NOT KNOW')
	    time.sleep(1)
	    return   	
	
def verifyAge(age):
	global chat_name
	while True:
		if not [isinstance(age, int)] :
			print('please give proper interger number')
			return False  
			
		if age <= 12 and age >= 0:
			print('SO YOU ARE A KID')
			time.sleep(1)
			print("I'M NOT VERY GOOD WITH KIDS BUT I THINK THIS WILL WORK OUT")
			time.sleep(1)
			if checkForCurseKid(chat_name):
				continue
			break 
		elif age <= 18 and age >= 13:
		    time.sleep(1)
		    print('OH...SO YOU ARE A TEENAGER')
		    time.sleep(1)
		    print('WELL I GUESS YOUR GOING THROUGH THAT STAGE IN YOUR LIFE')
		    time.sleep(1)
		    print('BUT DONT WORRY...')
		    time.sleep(2)
		    print('IT ONLY GETS WORSE AND YOU WILL LOOK BACK ON THESE DAYS WITH REGRET')
		    time.sleep(2)
		    print('ANYWAYS...')
		    break
		elif age <= 19 and age >= 30:
			time.sleep(1)
			print('OK...YOU ARE AN ADULT')
			time.sleep(1)
			print('SO I GUESS YOU CAN BASICALLY DO WHATEVER YOU WANT')
			time.sleep(1)
			print('YOU SHOULD PROBABLY ENJOY THESE DAYS')
			break
		elif age <= 31 and age >= 60:
			time.sleep(1)
			print('AHH...MIDLIFE CRISIS')
			time.sleep(1)
			print('IF YOU GO BUNGEE JUMPING AND MOTORCYCLING...')
			time.sleep(1)
			print('DONT TRY TO TAKE A SELFIE CUZ THAT WILL BE THAT LAST PHOTO YOU WILL EVER TAKE')
			time.sleep(1)
			print('GOT IT...GOOD')
			break
		elif age <= 61:
			time.sleep(1)
			print('NO JOKE...JUST TAKE IT EASY THIS TIME AROUND')
			time.sleep(1)
			print('JUST TRY TO BE HAPPY AND HOPEFULLY IT WILL STAY THAT WAY')
			time.sleep(1)
			print('TRUST ME')
			break


			
"""
Calling main program
"""

if __name__ == '__main__':
	main()




