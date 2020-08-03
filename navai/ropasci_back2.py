#!/usr/bin/python3.5 -tt


"""
Author Nav Don
"""
import os
import sys
import time
import random

global msg1,msg2,msg3,msg4,msg5

#msg1 = myBannerPrint()
msg2 = "To play this game you have to select rock, paper or scissors.\n"
msg3 = "You press 1 for rock, 2 for paper and 3 for scissors.\n"
msg4 = "To leave this game you may press 9 but you can play for how long you like.\n"
msg5 = "There is no time limit to select you hand.\n"
msg6 = "Pressing a worng key is immediate disqualification, so pick your cards  wisely.\n"
yes_list = ['y','Y','Yes','yes','YES','Yeh']
no_list = ['n','N','No','no','NO','nah']
def main():
	msg1 = myBannerPrint()
	global yes_list
	os.system('clear')
	global msg1
	myMsgPrint()
	print(msg1)
	myMiniMsgPrint()
	time.sleep(5)
	os.system('clear')
	time.sleep(3)
	print('HELLO... I AM LOOKING FOR A PERSON TO SPEND SOME TIME WITH...\n')
	time.sleep(1)
	print('WOULD YOU LIKE TO BE THAT PERSON: \n')
	time.sleep(1)
	question1 = input('Y/N : ')
	if question1 in yes_list:
		time.sleep(1)
		print('GREAT!\n')
		time.sleep(1)
		print('SORRY DID NOT CATCH YOUR NAME\n')
		time.sleep(1)
		name = input('COULD YOU PLEASE TELL ME IT: ')
		time.sleep(1)
		print('ANYWAYS {0},\n' .format(name))
		time.sleep(1)
		print('WE SHALL PLAY THE GAME OF ROCK PAPER SCISSORS\n')
		time.sleep(1)
		print('SO...{0}, DO YOU WANT TO PLAY\n'.format(name))
		question2 = input('Y/N : ')
		if question2 in yes_list:
			time.sleep(1)
			print('EXCELLENT!\n')
			time.sleep(1)
			print('FINNALY, SOMEONE TO KILL TIME WITH\n')
			time.sleep(1)
			print('LETS GET STARTED\n')
			time.sleep(3)
			print('CLEARING...........')
			time.sleep(3)
			os.system('clear')
			ropasciStart()
			
		elif question2 in no_list:
			time.sleep(1)
			print("OH THAT'S FINE\n")
			time.sleep(2)
			print('YOU CAN COME BACK {0} WHENEVER YOU WANT, BUT I MAY NOT REMEMBER YOU\n'.format(name))
			time.sleep(3)
			os.system('clear')
			return
		else:
			time.sleep(1)
			print('SORRY...I DONT KNOW WHAT YOU SAID\n')
			time.sleep(1)
			print('BUT I WILL ASK YOU AGAIN, AND I MAY LEAVE IF YOU DONT GIVE A PROPER ANSWER\n')
			time.sleep(1)
			print('DO YOU WANT TO PLAY {0}\n'.format(name))
			question4 = input('Y/N')
			if question4 in yes_list:
				time.sleep(1)
				print('EXCELLENT!\n')
				time.sleep(1)
				print('I AM GLAD YOU SAID THAT {0}\n'.format(name))
				time.sleep(1)
				print('SORRY ABOUT NOT UNDERSTANDING WHAT YOU SAID EARLIER\n')
				time.sleep(1)
				print('LETS GET STARTED\n')
				time.sleep(3)
				print('CLEARING...........')
				time.sleep(3)
				os.system('clear')
				ropasciStart()
			elif question4 in no_list:
				time.sleep(1)
				print('OHH OK\n')
				time.sleep(1)
				print('NO WORRIES {0}\n')
				time.sleep(1)
				print('SORRY FOR NOT UNDERSTANDING YOU EARLIER\n')
				time.sleep(1)
				print('YOU CAN COME BACK {0} WHENEVER YOU WANT, BUT I MAY NOT REMEMBER YOU\n'.format(name))
				time.sleep(3)
				os.system('clear')
				return
			else:
				time.sleep(1)
				print('I DONT UNDERSTAND WHAT YOU SAID\n')
				time.sleep(1)
				print('ANWAYS I THINK I GOT TO GO NOW\n')
				time.sleep(1)
				print('SEE YOU {0}, BUT I MAY NOT REMEMBER YOU\n'.format(name))
				time.sleep(2)
				os.system('clear')
				return
	elif question1 in no_list:
		time.sleep(1)
		print('OK THEN STRANGER\n')
		time.sleep(1)
		print('BYE\n')
		time.sleep(3)
		os.system('clear')
		return
	else:
		time.sleep(1)
		print('I DO NOT KNOW WHAT YOU SAID\n')
		time.sleep(1)
		print('BUT I WILL ASK YOU ONE MORE TIME\n')
		time.sleep(1)
		print('SO DO YOU WANT TO PLAY A GAME\n')	
		time.sleep(1)
		question5 = input('Y/N : ')
		if question5 in yes_list:
			time.sleep(1)
			print('GREAT!\n')
			time.sleep(1)
			print('SORRY DID NOT CATCH YOUR NAME\n')
			time.sleep(1)
			name = input('COULD YOU PLEASE TELL ME IT: ')
			time.sleep(1)
			print('ANYWAYS {0},\n' .format(name))
			time.sleep(1)
			print('WE SHALL PLAY THE GAME OF ROCK PAPER SCISSORS\n')
			time.sleep(1)
			print('SO...{0}, DO YOU WANT TO PLAY\n'.format(name))
			question6 = input('Y/N : ')
			if question6 in yes_list:
				time.sleep(1)
				print('EXCELLENT!\n')
				time.sleep(1)
				print('FINNALY, SOMEONE TO KILL TIME WITH\n')
				time.sleep(1)
				print('LETS GET STARTED\n')
				time.sleep(3)
				print('CLEARING...........')
				time.sleep(3)
				os.system('clear')
				ropasciStart()
			elif question6 in no_list:
				time.sleep(1)
				print("OH THAT'S FINE\n")
				time.sleep(2)
				print('YOU CAN COME BACK {0} WHENEVER YOU WANT, BUT I MAY NOT REMEMBER YOU\n'.format(name))
				time.sleep(3)
				os.system('clear')
				return
			else:
				time.sleep(1)
				print('SORRY...I DONT KNOW WHAT YOU SAID\n')
				time.sleep(1)
				print('BUT I WILL ASK YOU AGAIN, AND I MAY LEAVE IF YOU DONT GIVE A PROPER ANSWER\n')
				time.sleep(1)
				print('DO YOU WANT TO PLAY {0}\n'.format(name))
				question7 = input('Y/N : ')
				if question7 in yes_list:
					time.sleep(1)
					print('EXCELLENT!\n')
					time.sleep(1)
					print('I AM GLAD YOU SAID THAT {0}\n'.format(name))
					time.sleep(1)
					print('SORRY ABOUT NOT UNDERSTANDING WHAT YOU SAID EARLIER\n')
					time.sleep(1)
					print('LETS GET STARTED\n')
					time.sleep(3)
					print('CLEARING...........')
					time.sleep(3)
					os.system('clear')
					ropasciStart()
					
				elif question7 in no_list:
					time.sleep(1)
					print('OHH OK\n')
					time.sleep(1)
					print('NO WORRIES {0}\n')
					time.sleep(1)
					print('SORRY FOR NOT UNDERSTANDING YOU EARLIER\n')
					time.sleep(1)
					print('YOU CAN COME BACK {0} WHENEVER YOU WANT, BUT I MAY NOT REMEMBER YOU\n'.format(name))
					time.sleep(3)
					os.system('clear')
					return
				else:
					time.sleep(1)
					print('I DONT UNDERSTAND WHAT YOU SAID\n')
					time.sleep(1)
					print('ANWAYS I THINK I GOT TO GO NOW\n')
					time.sleep(1)
					print('SEE YOU {0}, BUT I MAY NOT REMEMBER YOU\n'.format(name))
					time.sleep(2)
					os.system('clear')
					return
		elif question5 in no_list:
			time.sleep(1)
			print('OK THEN STRANGER\n')
			time.sleep(1)
			print('BYE\n')
			time.sleep(3)
			os.system('clear')
			return
		else:
			time.sleep(1)
			print('I DONT UNDERSTAND WHAT YOU SAID\n')
			time.sleep(1)
			print('ANWAYS I THINK I GOT TO GO NOW\n')
			time.sleep(1)
			print('BYE\n'.format(name))
			time.sleep(2)
			os.system('1clear')
"""
below section for methods
"""
def ropasciStart():
	global msg2, msg3, msg4, msg5
	print('*' * 30)
	time.sleep(2)
	print(msg2)
	time.sleep(2)
	print(msg3)
	time.sleep(2)
	print(msg4)
	time.sleep(2)
	print(msg5)
	time.sleep(2)
	print('*' * 30)
	time.sleep(1)
	x = input("PRESS 'ENTER' TO CONTINUE")
	resultDict = {'1 1':4, '1 2':2, '1 3':1, '2 1':2, '2 2':4, '2 3':3, '3 1':1, '3 2':3, '3 3':4}
	if x == '':
		ui_ctr = 0
		mi_ctr = 0
		input_list = [1,2,3,9]
		while True:
			time.sleep(1)
			ui = int(input("CHOOSE YOUR HAND, 1 FOR ROCK, 2 FOR PAPER, 3 SCISSORS, 9 TO EXIT : "))
			mi = random.randint(1,3)
			if ui not in input_list:
				time.sleep(1)
				print('The user has pressed a worng key, this results in an immediate disqualification\n')
				time.sleep(1)
				print('LOOKS LIKE YOU PRESSED A WORNG KEY {0}, THATS BAD LUCK\n')
				if ui_ctr == 0:
					time.sleep(1)
					print('The user has forfeited before he/she could play a hand\n')
					time.sleep(1)
					print('Nobody wins\n')
					time.sleep(1)
					print('IT HAS BEEN NICE PLAYING WITH YOU\n')
					time.sleep(1)
					print('BYE\n')
					time.sleep(5)
					os.system('clear')
				elif ui_ctr > mi_ctr:
					time.sleep(1)
					print('The user has more points than the computer\n')
					time.sleep(1)
					print('The user wins\n')
					time.sleep(1)
					print('NICE, YOU WON... GOOD JOB\n')
					time.sleep(1)
					print('Your score = {0} and computer score = {1}'.format(ui_ctr,mi_ctr))
					time.sleep(5)
					os.system('clear')
				elif ui_ctr < mi_ctr:
					time.sleep(1)
					print('The computer has more points than the user\n')
					time.sleep(1)
					print('The computer wins\n')
					time.sleep(1)
					print('AWW...NICE TRY, HOPE TO SEE YOU NEXT TIME\n')
					time.sleep(1)
					print('Your score = {0} and computer score = {1}'.format(ui_ctr,mi_ctr))
					time.sleep(5)
					os.system('clear')
				elif ui_ctr == mi_ctr:
					time.sleep(1)
					print('Both players have the same amount of points, thus resulting in a tie\n')
					time.sleep(1)
					print('The nobody wins\n')
					time.sleep(1)
					print('WELL THAT WAS ANTI-CLIMATIC BUT IT WAS FUN PLAYING WITH YOU\n')
					time.sleep(1)
					print('Your score = {0} and computer score = {1}'.format(ui_ctr,mi_ctr))
					time.sleep(5)
					os.system('clear')
				break
			if ui == 9:
				if ui_ctr == 0:
					time.sleep(1)
					print('The user has forfeited before he/she could play a hand\n')
					time.sleep(1)
					print('Nobody wins\n')
					time.sleep(1)
					print('IT HAS BEEN NICE PLAYING WITH YOU\n')
					time.sleep(1)
					print('BYE\n')
					time.sleep(5)
					os.system('clear')
				elif ui_ctr > mi_ctr:
					time.sleep(1)
					print('The user has more points than the computer\n')
					time.sleep(1)
					print('The user wins\n')
					time.sleep(1)
					print('NICE, YOU WON... GOOD JOB\n')
					time.sleep(1)
					print('Your score = {0} and computer score = {1}'.format(ui_ctr,mi_ctr))
					time.sleep(5)
					os.system('clear')
				elif ui_ctr < mi_ctr:
					time.sleep(1)
					print('The computer has more points than the user\n')
					time.sleep(1)
					print('The computer wins\n')
					time.sleep(1)
					print('AWW...NICE TRY, HOPE TO SEE YOU NEXT TIME\n')
					time.sleep(1)
					print('Your score = {0} and computer score = {1}'.format(ui_ctr,mi_ctr))
					time.sleep(5)
					os.system('clear')
				elif ui_ctr == mi_ctr:
					time.sleep(1)
					print('Both players have the same amount of points, thus resulting in a tie\n')
					time.sleep(1)
					print('The nobody wins\n')
					time.sleep(1)
					print('WELL THAT WAS ANTI-CLIMATIC BUT IT WAS FUN PLAYING WITH YOU\n')
					time.sleep(1)
					print('Your score = {0} and computer score = {1}'.format(ui_ctr,mi_ctr))
					time.sleep(5)
					os.system('clear')
				break
			res = matchInputs(ui,mi)
			if res == 4:
				time.sleep(1)
				print('Both the user and the computer have chosen the same hand which is {0}\n'.format(ui))
				time.sleep(1)
				print('Tie\n')
			elif res == ui:
				time.sleep(1)
				print('The user has won this round with the hand, {0}\n'.format(ui))
				time.sleep(1)
				print('User is the winner\n')
				ui_ctr = ui_ctr + 1
			elif res == mi:
				time.sleep(1)
				print('The computer has won this round with the hand, {0}\n'.format(ui))
				time.sleep(1)
				print('Computer is the winner\n')
				mi_ctr = mi_ctr + 1
		  	
def myMsgPrint():
	print('_' * 5, ' ' * 90, '_' * 5)
	print('_' * 10, ' ' * 80, '_' * 10)
	print('_' * 15, ' ' * 70, '_' * 15)
	print('_' * 20, ' ' * 60, '_' * 20)
	print('_' * 25, ' ' * 50, '_' * 25)
	print('_' * 30, ' ' * 40, '_' * 30)
	print('_' * 35, ' ' * 30, '_' * 35)
	print('_' * 40, ' ' * 20, '_' * 40)
	print('_' * 45, ' ' * 10, '_' * 45)
	print('_' * 100)
def myMiniMsgPrint():
	print(' ' * 25, '_' * 50)
	print(' ' * 30, '_' * 40)
	print(' ' * 35, '_' * 30)
	print(' ' * 40, '_' * 20)
	print(' ' * 45, '_' * 10)				
def matchInputs(ui,mi):
    ui_str = str(ui)
    mi_str = str(mi)
    combine_str = ui_str+mi_str
    resultDict = {'11':4, '12':2, '13':1, '21':2, '22':4, '23':3, '31':1, '32':3, '33':4}
    get_res = resultDict[combine_str]
    get_res = int(get_res)
    return(get_res)
    
def myBannerPrint():
	return('''****************************************************************************************************
rrrrrrrrrrrrrrrrrrrrrrrrr        ppppppppppppppppppppppppp  sssssssssssssssssssssssss
rrrrrrrrrrrrrrrrrrrrrrrrrr       pppppppppppppppppppppppppp sssssssssssssssssssssssss
rrrr                  rrrr       pppp                  pppp ssss
rrrr                  rrrr       pppp                  pppp ssss
rrrr                  rrrr       pppp                  pppp ssss
rrrr                  rrrr       pppp                  pppp ssss
rrrr                  rrrr       pppp                  pppp  ssss
rrrr                 rrrr        pppp                 pppp    ssss
rrrr                rrrr         pppp                pppp      ssss
rrrr               rrrr          pppp               pppp        ssss
rrrr     rrrrrrrrrrrr            pppp    pppppppppppppp          ssssssssssssssssssss
rrrr            rrrr             pppp                                            ssss      
rrrr             rrrr            pppp                                            ssss
rrrr              rrrr           pppp                                            ssss
rrrr               rrrr          pppp                                            ssss
rrrr                rrrr         pppp                                            ssss
rrrr                 rrrr        pppp                                            ssss
rrrr                  rrrr       pppp                       ssssssssssssssssssssssss
rrrr                  rrrr O C K pppp A P E R               ssssssssssssssssssssssss  C I S S O R S''')
	
	


if __name__ == '__main__':
	main()

