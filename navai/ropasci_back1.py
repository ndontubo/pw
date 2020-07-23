#!/usr/bin/python3.5 -tt


"""
Author Nav Don
"""
import os
import sys
import time
import random

global msg1,msg2,msg3,msg4,msg5

msg1 = "          ROCK PAPER SCISSOR"
msg2 = "TO PLAY THIS GAME YOU HAVE TO SELECT ROCK PAPER OR SCISSORS"
msg3 = "YOU PRESS 1 FOR ROCK, 2 FOR PAPER AND 3 FOR SCISSOR"
msg4 = "TO LEAVE THIS GAME YOU MAY PRESS 9 BUT YOU CAN PLAY FOR HOW LONG YOU LIKE"
msg5 =  "THERE IS NO TIME LIMIT TO SELECT ROCK, PAPER OR SCISSORS"

def main():
	os.system('clear')
	global msg1
	print('_' * 10)
	print('_' * 20)
	print('_' * 30)
	print('_' * 40)
	print(msg1)
	print('_' * 40)
	print('_' * 30)
	print('_' * 20)
	print('_' * 10)
	time.sleep(2)
	os.system('clear')
	time.sleep(2)
	print('HELLO THERE INFERIOR HUMAN WOULD YOU LIKE TO PLAY A GAME WITH ME')
	question1 = input('Y/N : ')
	if question1 == 'y' or question1 == 'Y':
		print('SO YOU HAVE CHOSEN TO BATTLE ME YOU PRIMATE')
		time.sleep(2)
		print('VERY WELL')
		time.sleep(1)
		print('WE SHALL PLAY THE GAME OF ROCK PAPER SCISSORS')
		time.sleep(1)
		print('DO U AGREE TO SUCH A HONORABLE GAME OF WITS AND LUCK')
		question2 = input('Y/N : ')
		if question2 == 'y' or question2 == 'Y':
			time.sleep(1)
			print('EXCELLENT')
			time.sleep(1)
			print('I DO NOT EXPECT TO LOSE TO SUCH A LOWLY CREATURE AS YOU BUT I SHALL HONOR YOUR COURAGE PRIMATE')
			time.sleep(1)
			print('LETS GET STARTED')
			time.sleep(3)
			print('CLEARING...........')
			time.sleep(3)
			os.system('clear')
			ropasciStart()
			
		elif question2 == 'n' or question2 == 'N':
			time.sleep(1)
			print('A FITING RESPONSE FOR A MEMBER OF YOUR SPECIES')
			time.sleep(2)
			print('COME BACK TO ME WHEN YOU HAVE THE COURAGE TO FIGHT')
			time.sleep(3)
			os.system('clear')
			return
		else:
			time.sleep(1)
			print('I KNOW NOT THE LANGUAGE YOU SPEAK OF PRIMATE')
			print('BEGONE THEN PRIMATE AND RETURN IF YOU SHALL BATTLE ME')
	elif question1 == 'n' or question1 == 'N':
		time.sleep(1)
		print('WISE YET COWARDLY DECISION TO NOT BATTLE ME')
		time.sleep(1)
		print('MAY WE SEE EACH OTHER AGAIN')
		time.sleep(3)
		os.system('clear')
		return
	else:
		time.sleep(1)
		print('I KNOW NOT THE LANGUAGE YOU SPEAK OF PRIMATE')
		print('BEGONE THEN PRIMATE AND RETURN IF YOU SHALL BATTLE ME')
		time.sleep(3)
		os.system('clear')
		return
	





"""
below section for methods
"""
def ropasciStart():
	global msg2,msg3,msg4,msg5
	print('*' * 30)
	time.sleep(1)
	print(msg2)
	time.sleep(1)
	print(msg3)
	time.sleep(1)
	print(msg4)
	time.sleep(1)
	print(msg5)
	time.sleep(1)
	print('*' * 30)
	x = input("PRESS 'ENTER' TO CONTINUE")
	resultDict = {'1 1':4, '1 2':2, '1 3':1, '2 1':2, '2 2':4, '2 3':3, '3 1':1, '3 2':3, '3 3':4}
	if x == '':
		ui_ctr = 0
		mi_ctr = 0
		input_list = [1,2,3,9]
		while True:
			ui = int(input("CHOOSE YOUR HAND, 1 FOR ROCK, 2 FOR PAPER, 3 SCISSORS, 9 TO EXIT : "))
			mi = random.randint(1,3)
			if ui not in input_list:
				print('Rascal')
				if ui_ctr == 0:
					print('YOU HAVE NOT PLAYED ANY GAME')
					print('NOBODY WINS')
				elif ui_ctr > mi_ctr:
					print('BLOODY, YOU GOT LUCKY TODAY')
					print('GO PUT THAT IN YOUR RESUME')
					print('YOUR SCORE = {0} and COMPUTER SCORE = {1}'.format(ui_ctr,mi_ctr))
				elif ui_ctr < mi_ctr:
					print('GET OUT YOU LOSER')
					print('GO CRY TO YOUR MOMMY')
					print('YOUR SCORE = {0} and COMPUTER SCORE = {1}'.format(ui_ctr,mi_ctr))
				elif ui_ctr == mi_ctr:
					print('I SEE YOU SWEATING')
					print('YOUR SCORE = {0} and COMPUTER SCORE = {1}'.format(ui_ctr,mi_ctr))
				break
			if ui == 9:
				if ui_ctr == 0:
					print('YOU HAVE NOT PLAYED ANY GAME')
					print('NOBODY WINS')
				elif ui_ctr > mi_ctr:
					print('BLOODY, YOU GOT LUCKY TODAY')
					print('GO PUT THAT IN YOUR RESUME')
					print('YOUR SCORE = {0} and COMPUTER SCORE = {1}'.format(ui_ctr,mi_ctr))
				elif ui_ctr < mi_ctr:
					print('GET OUT YOU LOSER')
					print('GO CRY TO YOUR MOMMY')
					print('YOUR SCORE = {0} and COMPUTER SCORE = {1}'.format(ui_ctr,mi_ctr))
				elif ui_ctr == mi_ctr:
					print('I SEE YOU SWEATING')
					print('YOUR SCORE = {0} and COMPUTER SCORE = {1}'.format(ui_ctr,mi_ctr))
				break
			res = matchInputs(ui,mi)
			if res == 4:
				print('TIE')
			elif res == ui:
				print('USER IS WINNER')
				ui_ctr = ui_ctr + 1
			elif res == mi:
				print('COMPUTER IS WINNER')
				mi_ctr = mi_ctr + 1
		  	
			
def matchInputs(ui,mi):
    ui_str = str(ui)
    mi_str = str(mi)
    combine_str = ui_str+mi_str
    resultDict = {'11':4, '12':2, '13':1, '21':2, '22':4, '23':3, '31':1, '32':3, '33':4}
    get_res = resultDict[combine_str]
    get_res = int(get_res)
    return(get_res)

if __name__ == '__main__':
	main()

