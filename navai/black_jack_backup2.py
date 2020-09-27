#!/usr/bin/python3.5 -tt


"""
Author Nav Don
"""
import os
import time
import random
import re
from typing import Any, Union

global msg1, msg2, msg3, msg4, name, deck, mi_res

deck = ['ace_spades', 'ace_hearts', 'ace_diamonds', 'ace_clubs', '2_spades', '2_hearts', '2_diamonds', '2_clubs', '3_spades' , '3_hearts', '3_diamonds', '3_clubs', '4_spades', '4_hearts', '4_diamonds', '4_clubs', '5_spades', '5_hearts', '5_diamonds', '5_clubs', '6_spades', '6_hearts', '6_diamonds', '6_clubs', '7_spades', '7_hearts', '7_diamonds', '7_clubs', '8_spades', '8_hearts', '8_diamonds', '8_clubs', '9_spades', '9_hearts', '9_diamonds', '9_clubs', '10_spades', '10_hearts', '10_diamonds', '10_clubs', 'jack_spades', 'jack_hearts', 'jack_diamonds', 'jack_clubs', 'queen_spades', 'queen_hearts', 'queen_diamonds', 'queen_clubs', 'king_spades', 'king_hearts', 'king_diamonds', 'king_clubs']

yes_list = ['y', 'Y', 'Yes', 'yes', 'YES', 'Yeah','yeah', 'YEAH']
no_list = ['n', 'N', 'No', 'no', 'NO', 'nah']

myRules = ('''-------------------------------------------------------------------------------------------------------------------------------------------
The following are the rules of black jack, if you already know them you may press enter to skip ahead but please take
into account that we will not use chips to bet or play in the usual - you vs dealer - fashion. This being said I will
now say the rules. We will take turns starting first. Both players will be given two cards each, and the value of the
cards is as follows: Ace is either 1 or 11, number cards correspond to their number, face cards are 10. The objective
of the game is to get your hand's value as close to 21 as possible without going over - if you go over, you lose the
round. There are multiple ways to do this: You can "hit" which means that you are asking for one more card and you
can hit how many times you like during your turn but remember not to go over 21, press 1 to hit; you can stand that
means that you like the way your cards are and will end your turn, but remember you only get one turn to make your
hand press 2 to stand. There is also doubling down, surrendering, and splitting but since we do not play with money
because my programmer is broke - we will not play with these. The cards will be presented to the user as the value 
of the card followed by the suit. An example would be for ace of spades it is ace_spades.Each person only gets one 
turn to set their hand before presenting it and ending the round, so choose your moves carefully. There is no time limit
to how many rounds you wish to play, but at the end whoever wins the most rounds is the winner press 3 to exit. 
Pressing a wrong key results in immediate disqualification. I suggest a good way to learn the rules is to start the game
and play from there but you can choose when to start by pressing enter.
------------------------------------------------------------------------------------------------------------------------------------------
								''')

def myMsgPrint():
	return('''	
				   __________________________________ 
				  |                                  | 
				  |   A                              |
				  |                *         	     |
				  |           	  ***                |
				  |          	 *****               |
				  |            *********             |
				  |           ***********            |
				  |         ***************          |
				  |   	 *********************       |
				  |    **************************    |
				  |  ******************************  |
				  |   ****************************   |
				  |  	********** ** **********     |
				  |                **                |
				  |   	       	   **           A    |
				  |                                  |
				   __________________________________''')

def bannerPrint2():
	return('''************************************************************************************************************
BBBBBBBBB  LL          AAAAAAA 	 CCCCCCCC KK      KK | JJJJJJJJJJ  AAAAAAA   CCCCCCCCC KK      KK
BB      BB LL         AA     AA	CC        KK      KK |       JJ   AA     AA CC         KK      KK
BB      BB LL         AA     AA	CC        KK     KK  |       JJ   AA     AA CC         KK     KK
BB   BBBB  LL         AAAAAAAAA CC        KK   KKK   |       JJ   AAAAAAAAA CC         KK   KKK
BB      BB LL         AA     AA	CC        KK     KK  |       JJ   AA     AA CC         KK     KK
BB      BB LL         AA     AA	CC        KK      KK |  J    JJ   AA     AA CC         KK      KK
BBBBBBBBB  LLLLLLLLLL AA     AA	 CCCCCCCC KK      KK |  JJJJJJ    AA     AA  CCCCCCCCC KK      KK      ''')

def blackjack():
	time.sleep(1)
	shame = 'Because of your incompetence to select a proper value I shall choose it for you randomly\n'
	game_start = input('Press ENTER when ready\n')	
	if game_start == '':
		ui_ctr = 0
		mi_ctr = 0
		input_list = {1, 2, 3}
		round_ctr = 2
		while True:
			if (round_ctr % 2) == 0:
				thicc_cards = deck.copy()
				ui_card1 = random.choice(thicc_cards)
				thicc_cards.remove(ui_card1)
				ui_card2 = random.choice(thicc_cards)
				thicc_cards.remove(ui_card2)
				mi_card1 = random.choice(thicc_cards)
				thicc_cards.remove(mi_card1)
				mi_card2 = random.choice(thicc_cards)
				thicc_cards.remove(mi_card2)
				time.sleep(1)
				print('These are your cards {0}, {1}\n'.format(ui_card1, ui_card2))
				ui_cards = [ui_card1,ui_card2]
				for i in range(0,len(ui_cards)):
					if re.search("(ace_.)",ui_cards[i]):
						time.sleep(1)
						ace_quest = int(input('You have an ace would you like to regard it as a 1 or 11 : '))
						if ace_quest == 1:
							time.sleep(1)
							print('You have chosen your ace to be a 1\n')
							ui_cards[i] = 1
						elif ace_quest == 11:
							time.sleep(1)
							print('You have chosen your ace to be a 11\n')
							ui_cards[i] = 11
						else:
							time.sleep(1)
							print(shame)
							ui_cards[i] = random.randint(1,11)
							print('Your ace is chosen to be a {0}\n'.format(ui_cards[i]))
					elif re.search("(2_.)",ui_cards[i]):
						ui_cards[i] = 2
					elif re.search("(3_.)",ui_cards[i]):
						ui_cards[i] = 3
					elif re.search("(4_.)",ui_cards[i]):
						ui_cards[i] = 4
					elif re.search("(5_.)",ui_cards[i]):
						ui_cards[i] = 5
					elif re.search("(6_.)",ui_cards[i]):
						ui_cards[i] = 6						
					elif re.search("(7_.)",ui_cards[i]):
						ui_cards[i] = 7	
					elif re.search("(8_.)",ui_cards[i]):
						ui_cards[i] = 8
					elif re.search("(9_.)",ui_cards[i]):
						ui_cards[i] = 9
					elif re.search("(10_.)",ui_cards[i]):
						ui_cards[i] = 10
					elif re.search("(jack_.)",ui_cards[i]):
						ui_cards[i] = 10
					elif re.search("(queen_.)",ui_cards[i]):
						ui_cards[i] = 10
					elif re.search("(king_.)",ui_cards[i]):
						ui_cards[i] = 10
				ui_card_total = ui_cards[0] + ui_cards[1]
				time.sleep(1)
				print('Your hands total value currently is {0}\n'.format(ui_card_total))
				time.sleep(1)
				print("Now that your hand's value is established we will move onto 'hitting' or 'standing'\n")
				while True:
					if ui_card_total > 21:
						time.sleep(1)
						print("Your hand's value has gone over 21\n")
						time.sleep(1)
						print("But since you have started first in this round and hence you are the dealer you only "
							  "lose if the computer also busts\n")
						time.sleep(1)
						print("So it is now the computer's turn to select its hand")
						time.sleep(3)
						break
					print("Would you like to 'hit' to gain more cards or 'stand' because you are comfortable with your hand's value\n")
					time.sleep(1)
					hit_or_stand = int(input('Press 1 to hit and press 2 to stand : '))
					if hit_or_stand == 1:
						ui_card_extra = random.choice(thicc_cards)
						thicc_cards.remove(ui_card_extra)
						ui_cards.append(ui_card_extra)
						if re.search("(ace_.)",ui_cards[-1]):
								time.sleep(1)
								ace_quest2 = int(input('You have an ace would you like to regard it as a 1 or 11 : '))
								if ace_quest2 == 1:
									time.sleep(1)
									print('You have chosen your ace to be a 1\n')
									ui_cards[-1] = 1
								elif ace_quest2 == 11:
									time.sleep(1)
									print('You have chosen your ace to be a 11\n')
									ui_cards[-1] = 11
								else:
									time.sleep(1)
									print(shame)
									ui_cards[-1] = random.randint(1,11)
									print('Your ace is chosen to be a {0}\n'.format(ui_cards[-1]))
						elif re.search("(2_.)",ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 2
						elif re.search("(3_.)",ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 3
						elif re.search("(4_.)",ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 4
						elif re.search("(5_.)",ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 5
						elif re.search("(6_.)",ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 6						
						elif re.search("(7_.)",ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 7	
						elif re.search("(8_.)",ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 8
						elif re.search("(9_.)",ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 9
						elif re.search("(10_.)",ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 10
						elif re.search("(jack_.)",ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 10
						elif re.search("(queen_.)",ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 10
						elif re.search("(king_.)",ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 10
						ui_card_total = ui_card_total + ui_cards[-1]
						time.sleep(1)
						print('Your hands total value currently is {0}\n'.format (ui_card_total))
						continue
					elif hit_or_stand == 2:
						time.sleep(1)
						print('So you are confident in your hand\n')
						time.sleep(1)
						print('So now it is the computer turn to select its hand\n')
						time.sleep(3)
						break
						
					else:
						time.sleep(1)
						print('Because you are incompetent to select an action you will stand\n')
						time.sleep(1)
						print('So now it is the computer turn to select its hand\n')
						time.sleep(3)
						break
						
				os.system('clear')
				time.sleep(1)
				print('COMPUTER, these are your cards {0}, {1}\n'.format(mi_card1, mi_card2))
				mi_cards = [mi_card1, mi_card2]
				ace_ctr = 1
				for y in range(0, len(mi_cards)):
					if re.search("(ace_.)", mi_cards[y]):
							time.sleep(1)
							print('COMPUTER, you have an ace would you like to regard it as a 1 or 11 : ')
							if re.search("(ace_.)", mi_card1) and re.search("(ace_.)", mi_card2):
								if ace_ctr == 1:
									ace_ctr = ace_ctr + 1
									ace_quest = 11
									time.sleep(1)
									print('I WOULD LIKE TO REGARD IT AS 11\n')
								else:
									ace_quest = 1
									time.sleep(1)
									print('I WOULD LIKE TO REGARD IT AS 1\n')
							else:
								ace_quest = 11
								time.sleep(1)
								print('I WOULD LIKE TO REGARD IT AS 11\n')
							if ace_quest == 11:
								time.sleep(1)
								print('COMPUTER, so you have chosen your ace to be an 11\n')
								mi_cards[y] = 11
							elif ace_quest == 1:
								time.sleep(1)
								print('COMPUTER, so you have chosen your ace to be an 1\n')
								mi_cards[y] = 1
							else:
								time.sleep(1)
								print(shame)
								mi_cards[y] = random.randint(1,11)
								print('Your ace is chosen to be a {0}\n'.format(mi_cards[y]))
					elif re.search("(2_.)",mi_cards[y]):
						mi_cards[y] = 2
					elif re.search("(3_.)",mi_cards[y]):
						mi_cards[y] = 3
					elif re.search("(4_.)",mi_cards[y]):
						mi_cards[y] = 4
					elif re.search("(5_.)",mi_cards[y]):
						mi_cards[y] = 5
					elif re.search("(6_.)",mi_cards[y]):
						mi_cards[y] = 6						
					elif re.search("(7_.)",mi_cards[y]):
						mi_cards[y] = 7	
					elif re.search("(8_.)",mi_cards[y]):
						mi_cards[y] = 8
					elif re.search("(9_.)",mi_cards[y]):
						mi_cards[y] = 9
					elif re.search("(10_.)",mi_cards[y]):
						mi_cards[y] = 10
					elif re.search("(jack_.)",mi_cards[y]):
						mi_cards[y] = 10
					elif re.search("(queen_.)",mi_cards[y]):
						mi_cards[y] = 10
					elif re.search("(king_.)",mi_cards[y]):
						mi_cards[y] = 10
				mi_card_total = mi_cards[0] + mi_cards[1]
				time.sleep(1)
				print('COMPUTER, your hands total value currently is {0}\n'.format(mi_card_total))
				time.sleep(1)
				print("Now that your hand's value is established we will move onto 'hitting' or 'standing'\n")
				while True:
					if mi_card_total > 21:
						time.sleep(1)
						print("COMPUTER, your hand's value has gone over 21\n")
						time.sleep(1)
						print('If the user has also busted then it is a tie but if the user has not busted then the user wins\n')
						break
					print("COMPUTER, would you like to 'hit' to gain more cards or 'stand' because you are comfortable "
						  "with your hand's value\n")
					time.sleep(1)
					print('Press 1 to hit and press 2 to stand : ')
					len_in_deck = len(thicc_cards)
					if 21 >= mi_card_total >= 17:
						mi_res = 2
					else:
						if 50 >= len_in_deck >= 40:
							mi_res = 1
						elif 39 >= len_in_deck >= 20:
							if 16 >= mi_card_total >= 10:
								if (len(ui_cards) <= 4 and len(mi_cards) <= 4) or (
										len(ui_cards) <= 4 and re.findall("ace|king|jack|queen", mi_cards)):
									mi_res = 1
								elif ui_cards >= 4 >= mi_cards:
									mi_res = 2
							elif 9 >= mi_card_total >= 2:
								mi_res = 1
						elif 19 >= len_in_deck >= 0:
							if 16 >= mi_card_total >= 5:
								if (len(ui_cards) <= 4 and len(mi_cards <= 4)) or (
										len(ui_cards) <= 4 and re.findall("ace|king|jack|queen", mi_cards)):
									mi_res = 1
								elif len(ui_cards) >= 4 >= len(mi_cards):
									mi_res = 2
							elif 4 >= mi_card_total >= 0:
								mi_res = 1
					if mi_res == 1:
						time.sleep(1)
						print('I THINK I WILL HIT\n')
						mi_card_extra = random.choice(thicc_cards)
						thicc_cards.remove(mi_card_extra)
						mi_cards.append(mi_card_extra)
						if re.search("(ace_.)", mi_cards[-1]):
							time.sleep(1)
							print('COMPUTER, you have an ace would you like to regard it as a 1 or 11 : ')
							if re.search("(ace_.)", mi_card1) and re.search("(ace_.)", mi_card2):
								if ace_ctr == 1:
									ace_ctr = ace_ctr + 1
									ace_quest = 11
									time.sleep(1)
									print('I WOULD LIKE TO REGARD IT AS 11\n')
								else:
									ace_quest = 1
									time.sleep(1)
									print('I WOULD LIKE TO REGARD IT AS 1\n')
							elif 21 - mi_card_total <= 10:
								ace_quest = 1
								time.sleep(1)
								print('I WOULD LIKE TO REGARD IT AS 1\n')
							else:
								ace_quest = 11
								time.sleep(1)
								print('I WOULD LIKE TO REGARD IT AS 11\n')
							if ace_quest == 11:
								time.sleep(1)
								print('COMPUTER, so you have chosen your ace to be an 11\n')
								mi_cards[y] = 11
							elif ace_quest == 1:
								time.sleep(1)
								print('COMPUTER, so you have chosen your ace to be an 1\n')
								mi_cards[y] = 1
							else:
								time.sleep(1)
								print(shame)
								mi_cards[y] = random.randint(1,11)
								print('Your ace is chosen to be a {0}\n'.format(mi_cards[y]))
						elif re.search("(2_.)",mi_cards[-1]):
							print('COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 2
						elif re.search("(3_.)",mi_cards[-1]):
							print('COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 3
						elif re.search("(4_.)",mi_cards[-1]):
							print('COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 4
						elif re.search("(5_.)",mi_cards[-1]):
							print('COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 5
						elif re.search("(6_.)",mi_cards[-1]):
							print('COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 6						
						elif re.search("(7_.)",mi_cards[-1]):
							print('COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 7	
						elif re.search("(8_.)",mi_cards[-1]):
							print('COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 8
						elif re.search("(9_.)",mi_cards[-1]):
							print('COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 9
						elif re.search("(10_.)",mi_cards[-1]):
							print('COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 10
						elif re.search("(jack_.)",mi_cards[-1]):
							print('COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 10
						elif re.search("(queen_.)",mi_cards[-1]):
							print('COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 10
						elif re.search("(king_.)",mi_cards[-1]):
							print('COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 10
						mi_card_total = mi_card_total + mi_cards[-1]
						time.sleep(1)
						print('COMPUTER, your hands total value currently is {0}\n'.format (mi_card_total))
						continue
					elif mi_res == 2:
						time.sleep(1)
						print('I THINK I WILL STAND\n')
						time.sleep(1)
						print('COMPUTER, so you are confident in your hand\n')
						time.sleep(1)
						print('COMPUTER, So now it is to reveal hands\n')
						break
					else:
						time.sleep(1)
						print('COMPUTER, because you are incompetent to select an action you will stand\n')
						time.sleep(1)
						print('COMPUTER, it is time to reveal hands\n')
						break
				time.sleep(2)
				os.system('clear')
				time.sleep(1)
				print('These are the results\n')
				time.sleep(1)
				print('COMPUTER has the score of {0} and {1} has the  score of {2}\n'.format(mi_card_total, name, ui_card_total))
				if ui_card_total > 21 and mi_card_total > 21:
					time.sleep(1)
					print('{0} has busted but so has COMPUTER and because {0} started first, it is a tie\n'.format(name))
					time.sleep(2)
					print('WELL THAT WAS ANTI-CLIMACTIC\n')
				else:
					if ui_card_total > 21:
						time.sleep(1)
						print('{0} has busted without COMPUTER going over so COMPUTER wins\n'.format(name))
						mi_ctr = mi_ctr + 1
						time.sleep(2)
						print('HEY YOU CANT BLAME YOURSELF, YOU JUST CANT WIN AGAINST A MACHINE\n')
					elif mi_card_total > 21:
						time.sleep(1)
						print('COMPUTER has busted without {0} going over so {0} wins\n'.format(name))
						ui_ctr = ui_ctr + 1
						time.sleep(2)
						print('NICE ONE {0}\n'.format(name))
					elif ui_card_total > mi_card_total:
						time.sleep(1)
						print('{0} has a closer hand value to 21 than COMPUTER has\n'.format(name))
						ui_ctr = ui_ctr + 1
						time.sleep(2)
						print('NICE ONE {0}\n'.format(name))
					elif mi_card_total > ui_card_total:
						time.sleep(1)
						print('COMPUTER has a closer hand value to 21 than {0} has\n'.format(name))
						mi_ctr = mi_ctr + 1
						time.sleep(2)
						print('HEY YOU CANT BLAME YOURSELF, YOU JUST CANT WIN AGAINST A MACHINE\n')
					elif mi_card_total == ui_card_total:
						time.sleep(1)
						print('COMPUTER has the same value as {0}, so its a tie\n'.format(name))
						time.sleep(2)
						print('WELL THAT WAS ANTI-CLIMACTIC\n')
						break
				time.sleep(2)
				os.system('clear')
				time.sleep(1)
				another_match = input('HEY, DO YOU WANNA PLAY ANOTHER GAME {0}, PRESS 3 TO EXIT OR PRESS ANY OTHER KEY TO CONTINUE : '.format(name))
				if another_match == '3':
					time.sleep(1)
					print('OK THEN {0}, HOPE TO SEE YOU AGAIN\n'.format(name))
					time.sleep(1)
					print('BYE\n')
					time.sleep(2)
					os.system('clear')
					return
				else:
					time.sleep(1)
					print('OK THEN {0}, LETS GO ANOTHER ROUND\n'.format(name))
					time.sleep(1)
					print('LETS GET STARTED\n')
					time.sleep(2)
					os.system('clear')
					round_ctr = round_ctr + 1
					continue
			else:
				thicc_cards = deck.copy()
				mi_card1 = random.choice(thicc_cards)
				thicc_cards.remove(mi_card1)
				mi_card2 = random.choice(thicc_cards)
				thicc_cards.remove(mi_card2)
				ui_card1 = random.choice(thicc_cards)
				thicc_cards.remove(ui_card1)
				ui_card2 = random.choice(thicc_cards)
				thicc_cards.remove(ui_card2)
				time.sleep(1)
				print('COMPUTER, these are your cards {0}, {1}\n'.format(mi_card1, mi_card2))
				mi_cards = [mi_card1, mi_card2]
				mi_card_total = mi_cards[0] + mi_cards[1]
				ace_ctr = 1
				for y in range(0, len(mi_cards)):
					if re.search("(ace_.)", mi_cards[y]):
						time.sleep(1)
						print('COMPUTER, you have an ace would you like to regard it as a 1 or 11 : ')
						if re.search("(ace_.)", mi_card1) and re.search("(ace_.)", mi_card2):
							if ace_ctr == 1:
								ace_ctr = ace_ctr + 1
								ace_quest = 11
								time.sleep(1)
								print('I WOULD LIKE TO REGARD IT AS 11\n')
							else:
								ace_quest = 1
								time.sleep(1)
								print('I WOULD LIKE TO REGARD IT AS 1\n')
						else:
							ace_quest = 11
							time.sleep(1)
							print('I WOULD LIKE TO REGARD IT AS 11\n')
						if ace_quest == 11:
							time.sleep(1)
							print('COMPUTER, so you have chosen your ace to be an 11\n')
							mi_cards[y] = 11
						elif ace_quest == 1:
							time.sleep(1)
							print('COMPUTER, so you have chosen your ace to be an 1\n')
							mi_cards[y] = 1
						else:
							time.sleep(1)
							print(shame)
							mi_cards[y] = random.randint(1, 11)
							print('Your ace is chosen to be a {0}\n'.format(mi_cards[y]))
					elif re.search("(2_.)", mi_cards[y]):
						mi_cards[y] = 2
					elif re.search("(3_.)", mi_cards[y]):
						mi_cards[y] = 3
					elif re.search("(4_.)", mi_cards[y]):
						mi_cards[y] = 4
					elif re.search("(5_.)", mi_cards[y]):
						mi_cards[y] = 5
					elif re.search("(6_.)", mi_cards[y]):
						mi_cards[y] = 6
					elif re.search("(7_.)", mi_cards[y]):
						mi_cards[y] = 7
					elif re.search("(8_.)", mi_cards[y]):
						mi_cards[y] = 8
					elif re.search("(9_.)", mi_cards[y]):
						mi_cards[y] = 9
					elif re.search("(10_.)", mi_cards[y]):
						mi_cards[y] = 10
					elif re.search("(jack_.)", mi_cards[y]):
						mi_cards[y] = 10
					elif re.search("(queen_.)", mi_cards[y]):
						mi_cards[y] = 10
					elif re.search("(king_.)", mi_cards[y]):
						mi_cards[y] = 10
				mi_card_total = mi_cards[0] + mi_cards[1]
				time.sleep(1)
				print('COMPUTER, your hands total value currently is {0}\n'.format(mi_card_total))
				time.sleep(1)
				print("Now that your hand's value is established we will move onto 'hitting' or 'standing'\n")
				while True:
					if mi_card_total > 21:
						time.sleep(1)
						print("COMPUTER, your hand's value has gone over 21\n")
						time.sleep(1)
						print('But since you went first; you are the dealer and so you only lose if {0} does not bust\n'.format(name))
						break
					print("COMPUTER, would you like to 'hit' to gain more cards or 'stand' because you are comfortable with your hand's value\n")
					time.sleep(1)
					print('Press 1 to hit and press 2 to stand : ')
					len_in_deck = len(thicc_cards)
					if 21 >= mi_card_total >= 17:
						mi_res = 2
					else:
						if 50 >= len_in_deck >= 40:
							mi_res = 1
						elif 39 >= len_in_deck >= 20:
							if 16 >= mi_card_total >= 10:
								if (len(ui_cards) <= 4 and len(mi_cards) <= 4) or (
										len(ui_cards) <= 4 and re.findall("ace|king|jack|queen", mi_cards)):
									mi_res = 1
								elif ui_cards >= 4 >= mi_cards:
									mi_res = 2
							elif 9 >= mi_card_total >= 2:
								mi_res = 1
						elif 19 >= len_in_deck >= 0:
							if 16 >= mi_card_total >= 5:
								if (len(ui_cards) <= 4 and len(mi_cards <= 4)) or (len(ui_cards) <= 4 and re.findall("ace|king|jack|queen", mi_cards)):
									mi_res = 1
								elif len(ui_cards) >= 4 >= len(mi_cards):
									mi_res = 2
							elif 4 >= mi_card_total >= 0:
								mi_res = 1
					if mi_res == 1:
						time.sleep(1)
						print('I THINK I WILL HIT\n')
						mi_card_extra = random.choice(thicc_cards)
						thicc_cards.remove(mi_card_extra)
						mi_cards.append(mi_card_extra)
						if re.search("(ace_.)", mi_cards[-1]):
							time.sleep(1)
							print('COMPUTER, you have an ace would you like to regard it as a 1 or 11 : ')
							if re.search("(ace_.)", mi_card1) and re.search("(ace_.)", mi_card2):
								if ace_ctr == 1:
									ace_ctr = ace_ctr + 1
									ace_quest = 11
									time.sleep(1)
									print('I WOULD LIKE TO REGARD IT AS 11\n')
								else:
									ace_quest = 1
									time.sleep(1)
									print('I WOULD LIKE TO REGARD IT AS 1\n')
							elif 21 - mi_card_total <= 10:
								ace_quest = 1
								time.sleep(1)
								print('I WOULD LIKE TO REGARD IT AS 1\n')
							else:
								ace_quest = 11
								time.sleep(1)
								print('I WOULD LIKE TO REGARD IT AS 11\n')
							if ace_quest == 11:
								time.sleep(1)
								print('COMPUTER, so you have chosen your ace to be an 11\n')
								mi_cards[y] = 11
							elif ace_quest == 1:
								time.sleep(1)
								print('COMPUTER, so you have chosen your ace to be an 1\n')
								mi_cards[y] = 1
							else:
								time.sleep(1)
								print(shame)
								mi_cards[y] = random.randint(1, 11)
								print('Your ace is chosen to be a {0}\n'.format(mi_cards[y]))
						elif re.search("(2_.)", mi_cards[-1]):
							print(
								'COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 2
						elif re.search("(3_.)", mi_cards[-1]):
							print(
								'COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 3
						elif re.search("(4_.)", mi_cards[-1]):
							print(
								'COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 4
						elif re.search("(5_.)", mi_cards[-1]):
							print(
								'COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 5
						elif re.search("(6_.)", mi_cards[-1]):
							print(
								'COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 6
						elif re.search("(7_.)", mi_cards[-1]):
							print(
								'COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 7
						elif re.search("(8_.)", mi_cards[-1]):
							print(
								'COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 8
						elif re.search("(9_.)", mi_cards[-1]):
							print(
								'COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 9
						elif re.search("(10_.)", mi_cards[-1]):
							print(
								'COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 10
						elif re.search("(jack_.)", mi_cards[-1]):
							print(
								'COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 10
						elif re.search("(queen_.)", mi_cards[-1]):
							print(
								'COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 10
						elif re.search("(king_.)", mi_cards[-1]):
							print(
								'COMPUTER, the card that you have been given randomly is a {0}\n'.format(mi_cards[-1]))
							mi_cards[-1] = 10
						mi_card_total = int(mi_card_total) + mi_cards[-1]
						time.sleep(1)
						print('COMPUTER, your hands total value currently is {0}\n'.format(mi_card_total))
						continue
					elif mi_res == 2:
						time.sleep(1)
						print('I THINK I WILL STAND\n')
						time.sleep(1)
						print('COMPUTER, so you are confident in your hand\n')
						time.sleep(1)
						print('COMPUTER, so it is {0} turn\n'.format(name))
						break
					else:
						time.sleep(1)
						print('COMPUTER, because you are incompetent to select an action you will stand\n')
						time.sleep(1)
						print('COMPUTER, now it is {0} turn\n'.format(name))
						break
				os.system('clear')
				time.sleep(1)
				print('These are your cards {0}, {1}\n'.format(ui_card1, ui_card2))
				ui_cards = [ui_card1, ui_card2]
				for i in range(0, len(ui_cards)):
					if re.search("(ace_.)", ui_cards[i]):
						time.sleep(1)
						ace_quest = int(input('You have an ace would you like to regard it as a 1 or 11 : '))
						if ace_quest == 1:
							time.sleep(1)
							print('You have chosen your ace to be a 1\n')
							ui_cards[i] = 1
						elif ace_quest == 11:
							time.sleep(1)
							print('You have chosen your ace to be a 11\n')
							ui_cards[i] = 11
						else:
							time.sleep(1)
							print(shame)
							ui_cards[i] = random.randint(1, 11)
							print('Your ace is chosen to be a {0}\n'.format(ui_cards[i]))
					elif re.search("(2_.)", ui_cards[i]):
						ui_cards[i] = 2
					elif re.search("(3_.)", ui_cards[i]):
						ui_cards[i] = 3
					elif re.search("(4_.)", ui_cards[i]):
						ui_cards[i] = 4
					elif re.search("(5_.)", ui_cards[i]):
						ui_cards[i] = 5
					elif re.search("(6_.)", ui_cards[i]):
						ui_cards[i] = 6
					elif re.search("(7_.)", ui_cards[i]):
						ui_cards[i] = 7
					elif re.search("(8_.)", ui_cards[i]):
						ui_cards[i] = 8
					elif re.search("(9_.)", ui_cards[i]):
						ui_cards[i] = 9
					elif re.search("(10_.)", ui_cards[i]):
						ui_cards[i] = 10
					elif re.search("(jack_.)", ui_cards[i]):
						ui_cards[i] = 10
					elif re.search("(queen_.)", ui_cards[i]):
						ui_cards[i] = 10
					elif re.search("(king_.)", ui_cards[i]):
						ui_cards[i] = 10
				ui_card_total = ui_cards[0] + ui_cards[1]
				time.sleep(1)
				print('Your hands total value currently is {0}\n'.format(ui_card_total))
				time.sleep(1)
				print("Now that your hand's value is established we will move onto 'hitting' or 'standing'\n")
				while True:
					if ui_card_total > 21:
						time.sleep(1)
						print("Your hand's value has gone over 21\n")
						time.sleep(1)
						print("But since you have started first in this round and hence you are the dealer you only lose if the computer also busts\n")
						time.sleep(1)
						print("So it is now the computer's turn to select its hand")
						time.sleep(3)
						break
					print("Would you like to 'hit' to gain more cards or 'stand' because you are comfortable with your hand's value\n")
					time.sleep(1)
					hit_or_stand = int(input('Press 1 to hit and press 2 to stand : '))
					if hit_or_stand == 1:
						ui_card_extra = random.choice(thicc_cards)
						thicc_cards.remove(ui_card_extra)
						ui_cards.append(ui_card_extra)
						if re.search("(ace_.)", ui_cards[-1]):
							time.sleep(1)
							ace_quest2 = int(input('You have an ace would you like to regard it as a 1 or 11 : '))
							if ace_quest2 == 1:
								time.sleep(1)
								print('You have chosen your ace to be a 1\n')
								ui_cards[-1] = 1
							elif ace_quest2 == 11:
								time.sleep(1)
								print('You have chosen your ace to be a 11\n')
								ui_cards[-1] = 11
							else:
								time.sleep(1)
								print(shame)
								ui_cards[-1] = random.randint(1, 11)
								print('Your ace is chosen to be a {0}\n'.format(ui_cards[-1]))
						elif re.search("(2_.)", ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 2
						elif re.search("(3_.)", ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 3
						elif re.search("(4_.)", ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 4
						elif re.search("(5_.)", ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 5
						elif re.search("(6_.)", ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 6
						elif re.search("(7_.)", ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 7
						elif re.search("(8_.)", ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 8
						elif re.search("(9_.)", ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 9
						elif re.search("(10_.)", ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 10
						elif re.search("(jack_.)", ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 10
						elif re.search("(queen_.)", ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 10
						elif re.search("(king_.)", ui_cards[-1]):
							print('The card that you have been given randomly is a {0}\n'.format(ui_cards[-1]))
							ui_cards[-1] = 10
						ui_card_total = ui_card_total + ui_cards[-1]
						time.sleep(1)
						print('Your hands total value currently is {0}\n'.format(ui_card_total))
						continue
					elif hit_or_stand == 2:
						time.sleep(1)
						print('So you are confident in your hand\n')
						time.sleep(1)
						print('It is time to reveal hands\n')
						time.sleep(3)
						break

					else:
						time.sleep(1)
						print('Because you are incompetent to select an action you will stand\n')
						time.sleep(1)
						print('It is time to reveal hands\n')
						time.sleep(3)
						break
				time.sleep(2)
				os.system('clear')
				time.sleep(1)
				print('These are the results\n')
				time.sleep(1)
				print('COMPUTER has the score of {0} and {1} has the  score of {2}\n'.format(mi_card_total, name, ui_card_total))
				if ui_card_total > 21 and mi_card_total > 21:
					time.sleep(1)
					print(
						'{0} has busted but so has COMPUTER and because {0} started first, it is a tie\n'.format(name))
					time.sleep(2)
					print('WELL THAT WAS ANTI-CLIMACTIC\n')
				else:
					if ui_card_total > 21:
						time.sleep(1)
						print('{0} has busted without COMPUTER going over so COMPUTER wins\n'.format(name))
						mi_ctr = mi_ctr + 1
						time.sleep(2)
						print('HEY YOU CANT BLAME YOURSELF, YOU JUST CANT WIN AGAINST A MACHINE\n')
					elif mi_card_total > 21:
						time.sleep(1)
						print('COMPUTER has busted without {0} going over so {0} wins\n'.format(name))
						ui_ctr = ui_ctr + 1
						time.sleep(2)
						print('NICE ONE {0}\n'.format(name))
					elif ui_card_total > mi_card_total:
						time.sleep(1)
						print('{0} has a closer hand value to 21 than COMPUTER has\n'.format(name))
						ui_ctr = ui_ctr + 1
						time.sleep(2)
						print('NICE ONE {0}\n'.format(name))
					elif mi_card_total > ui_card_total:
						time.sleep(1)
						print('COMPUTER has a closer hand value to 21 than {0} has\n'.format(name))
						mi_ctr = mi_ctr + 1
						time.sleep(2)
						print('HEY YOU CANT BLAME YOURSELF, YOU JUST CANT WIN AGAINST A MACHINE\n')
					elif mi_card_total == ui_card_total:
						time.sleep(1)
						print('COMPUTER has the same value as {0}, so its a tie\n'.format(name))
						time.sleep(2)
						print('WELL THAT WAS ANTI-CLIMACTIC\n')
						break
				time.sleep(2)
				os.system('clear')
				time.sleep(1)
				another_match = input('HEY, DO YOU WANNA PLAY ANOTHER GAME {0}, PRESS 3 TO EXIT OR PRESS ANY OTHER KEY TO CONTINUE : '.format(name))
				if another_match == '3':
					time.sleep(1)
					print('OK THEN {0}, HOPE TO SEE YOU AGAIN\n'.format(name))
					time.sleep(1)
					print('BY THE WAY, HERE IS THE SCORE\n')
					time.sleep(1)
					print('Both players played {0} round(s)\n'.format(round_ctr))
					time.sleep(1)
					print('COMPUTER has a score of {0} and {1} has a score of {2}\n'.format(mi_ctr, name, ui_ctr))
					if ui_ctr > mi_ctr:
						time.sleep(1)
						print('{0} WINS\n'.format(name))
						print('ILL GET YOU NEXT TIME\n')
						time.sleep(4)
						os.system('clear')
					elif mi_ctr > ui_ctr:
						time.sleep(1)
						print('COMPUTER WINS\n')
						print('TOO BAD IT WAS NOT AN EATING CONTEST\n')
						time.sleep(4)
						os.system('clear')
					elif mi_ctr == ui_ctr:
						time.sleep(1)
						print('TIE\n')
						print('I SEE YOU SWEATING\n')
						time.sleep(4)
						os.system('clear')
					print('WELL SE YOU\n')
					time.sleep(1)
					print('BYE\n')
					time.sleep(2)
					os.system('clear')
					return
				else:
					time.sleep(1)
					print('OK THEN {0}, LETS GO ANOTHER ROUND\n'.format(name))
					time.sleep(1)
					print('LETS GET STARTED\n')
					time.sleep(2)
					os.system('clear')
					round_ctr = round_ctr + 1
					continue
def main():
	msg4 = myRules
	msg2 = myMsgPrint()
	msg1 = bannerPrint2()
	print(msg1)
	print(msg2)
	time.sleep(3)
	#os.system('clear')
	print('HEY YOU, YEAH YOU\n')
	time.sleep(1)
	print('YOU WANNA GAMBLE FOR A BIT AND PLAY SOME BLACKJACK\n')
	quest1 = input('Y/N : ')
	if quest1 in yes_list:
		global name
		time.sleep(1)
		print('GREAT\n')
		time.sleep(1)
		print('BY THE WAY I DONT KNOW YOUR NAME\n')
		time.sleep(1)
		name = input('COULD YOU TELL ME IT : ')
		time.sleep(1)
		print('SO {0} LETS GET STARTED\n'.format(name))
		time.sleep(3)
		print('CLREAING.........\n')
		time.sleep(2)
		os.system('clear')
		print(msg4)
		blackjack()
	elif quest1 in no_list:
		time.sleep(1)
		print('OH OK\n')
		time.sleep(1)
		print('WELL THEN...BYE STRANGER\n')
		time.sleep(1)
		print('>>>>END<<<<')
		time.sleep(1)
		os.system('clear')
	else:
		time.sleep(1)
		print('bye\n')
		time.sleep(1)
		os.system('clear\n')
	
if __name__ == '__main__':
	main()

