#!/usr/bin/python3.5 -tt


"""
Author Nav Don
"""
import os
import time
import random
import re
import sys

global msg1, msg2, msg3, msg4, name, deck, mi_res, myRules, thicc_cards, deal_dict, round_bet, player_order, player_bet, total_pot

fd = open('run.log', 'w')

def main():
	msg4 = myRules
	msg2 = myMsgPrint()
	msg1 = bannerPrint2()
	print(msg1)
	print(msg2)
	time.sleep(5)
	os.system('clear')
	print('HEY YOU, YEAH YOU\n')
	print('YOU WANNA GAMBLE FOR A BIT AND PLAY SOME BLACKJACK\n')
	quest1 = input('Y/N : ')
	if quest1 in yes_list:
		global name
		global rounds_count
		player_count = int(input('HOW MANY PLAYERS ARE PARTICIPATING : '))
		rounds_count = int(input('HOW MANY ROUNDS DO YOU WISH TO PLAY: '))
		if player_count > 0:
			#time.sleep(1)
			global player_cards
			player_cards = {}
			global player_list
			player_list = []
			global credit_dict
			credit_dict = {}
			global score_dict
			score_dict = {}
			global final_winner
			final_winner = ''
			for cnt in range(player_count):
				print('ENTER NAME FOR USER {0}'.format(cnt + 1))
				uname = input('Username: ')
				player_list.append(uname)
				credit_dict[uname] = 10000
			for k, v in credit_dict.items():
				print(k, "Your total credits are ----->", v)
			player_list.append('DEALER')
			time.sleep(1)
			credit_dict['DEALER'] = 10000
			print('SO LETS GET STARTED\n')
			print("DEALER ALSO HAS CREDITS OF {0}".format(credit_dict['DEALER']))
			time.sleep(3)
			print('CLREAING.........\n')
			time.sleep(2)
			os.system('clear')
			print(msg4)
			blackjack(player_list, credit_dict, score_dict, rounds_count)
		else:
			time.sleep(2)
			print('NICE TRY\n')
			time.sleep(1)
			os.system('clear')
			sys.exit()
	elif quest1 in no_list:
		time.sleep(2)
		print('OH OK\n')
		time.sleep(2)
		print('WELL THEN...BYE STRANGER\n')
		time.sleep(2)
		os.system('clear')
	else:
		time.sleep(2)
		print('bye\n')
		time.sleep(2)
		os.system('clear\n')

deck = ['ace_spades', 'ace_hearts', 'ace_diamonds', 'ace_clubs', '2_spades', '2_hearts', '2_diamonds', '2_clubs',
		'3_spades', '3_hearts', '3_diamonds', '3_clubs', '4_spades', '4_hearts', '4_diamonds', '4_clubs', '5_spades',
		'5_hearts', '5_diamonds', '5_clubs', '6_spades', '6_hearts', '6_diamonds', '6_clubs', '7_spades', '7_hearts',
		'7_diamonds', '7_clubs', '8_spades', '8_hearts', '8_diamonds', '8_clubs', '9_spades', '9_hearts', '9_diamonds',
		'9_clubs', '10_spades', '10_hearts', '10_diamonds', '10_clubs', 'jack_spades', 'jack_hearts', 'jack_diamonds',
		'jack_clubs', 'queen_spades', 'queen_hearts', 'queen_diamonds', 'queen_clubs', 'king_spades', 'king_hearts',
		'king_diamonds', 'king_clubs']

yes_list = ['y', 'Y', 'Yes', 'yes', 'YES', 'Yeah', 'yeah', 'YEAH']
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
	return ('''	
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
	return ('''************************************************************************************************************
BBBBBBBBB  LL          AAAAAAA 	 CCCCCCCC KK      KK | JJJJJJJJJJ  AAAAAAA   CCCCCCCCC KK      KK
BB      BB LL         AA     AA	CC        KK      KK |       JJ   AA     AA CC         KK      KK
BB      BB LL         AA     AA	CC        KK     KK  |       JJ   AA     AA CC         KK     KK
BB   BBBB  LL         AAAAAAAAA CC        KK   KKK   |       JJ   AAAAAAAAA CC         KK   KKK
BB      BB LL         AA     AA	CC        KK     KK  |       JJ   AA     AA CC         KK     KK
BB      BB LL         AA     AA	CC        KK      KK |  J    JJ   AA     AA CC         KK      KK
BBBBBBBBB  LLLLLLLLLL AA     AA	 CCCCCCCC KK      KK |  JJJJJJ    AA     AA  CCCCCCCCC KK      KK      ''')

def dealTheCards(players_list):
	global thicc_cards
	deal_dict = {}
	thicc_cards = deck.copy()
	# print(len(thicc_cards))
	for player in players_list:
		print(players_list, file=fd)
		print(len(players_list), file=fd)
		deal_dict[player, 'card1'] = random.choice(thicc_cards)
		thicc_cards.remove(deal_dict[player, 'card1'])
		deal_dict[player, 'card2'] = random.choice(thicc_cards)
		thicc_cards.remove(deal_dict[player, 'card2'])
		print(player, file=fd)
	print(deal_dict, file=fd)
	print(len(thicc_cards), file=fd)
	return (deal_dict)


def blackjack(player_list, credit_dict, score_dict, rounds_count):
	global player_order, round_bet
	global thicc_cards
	player_order = []
	new_player_list = []
	new_player_list2 = []
	rounds = 0
	while rounds_count > 0:
		rounds = rounds + 1
		mi_cards_list = []
		loser_list = []
		winner_list = []
		winner_dict = {}
		ui_cards = []
		player_bet = {}
		total_pot = 0
		mi_card_total = 0
		ui_card_total = 0
		checkFlag = 0
		rounds_count = rounds_count - 1
		turns = 0
		time.sleep(1)
		print('\n')
		new_player_list = player_list.copy()
		new_player_list2 = new_player_list

		init_deal_dict = dealTheCards(new_player_list)

		for k, v in init_deal_dict.items():
			if re.search('DEALER', str(k)):
				mi_cards_list.append(v)
				print(mi_cards_list, file=fd)

		round_bet = int(input('How much are we agreeing to bet for this round: '))
		total_pot = len(new_player_list) * round_bet

		while len(new_player_list) > 0:

			for pl, scr in credit_dict.items():
				if scr < 1 or scr < round_bet:
					new_player_list.remove(pl)
					player_list.remove(pl)
					score_dict.pop(pl)
					time.sleep(1)
					checkFlag = 1
					print('{0}, because you cannot bet anymore credits, you are ELIMINATED FROM the game\n'.format(pl))

			if len(new_player_list) == 1 and checkFlag:
				announceWinner()
				return

			print(credit_dict, file=fd)
			print(new_player_list, file=fd)
			curr_player = random.choice(new_player_list)
			new_player_list.remove(curr_player)
			print(new_player_list, file=fd)
			shame = 'Because of your incompetence to select a proper value I shall choose it for you randomly\n'
			print('NOW PLAYING ------->  {0}'.format(curr_player))
			print('ALL OTHER PLAYERS LEAVE THIS TABLE, YOU WILL BE CALLED ONCE CURRENT PLAYER IS DONE WITH HIS/HER ROUND\n')
			print('{0} - your current credits are {1}.. BEST OF LUCK\n'.format(curr_player, credit_dict[curr_player] - round_bet))
			game_start = input('Press ENTER when ready\n')
			if game_start == '':
				if curr_player != "DEALER":
					ui_card_total = 0
					print('Your cards are :')
					for pl, crd in zip([curr_player, curr_player], ['card1', 'card2']):
						the_cards = init_deal_dict[pl, crd]
						print(the_cards)
					for pl, crd in zip([curr_player, curr_player], ['card1', 'card2']):
						if re.search("(ace_.)", init_deal_dict[pl, crd]):
							ace_quest = int(input('You have an ace would you like to regard it as a 1 or 11 : '))
							if ace_quest == 1:
								print('You have chosen your ace to be a 1\n', file=fd)
								init_deal_dict[pl, crd] = 1
								ui_cards.append(init_deal_dict[pl, crd])
							elif ace_quest == 11:
								print('You have chosen your ace to be a 11\n', file=fd)
								init_deal_dict[pl, crd] = 11
								ui_cards.append(init_deal_dict[pl, crd])
							else:
								print(shame)
								init_deal_dict[pl, crd] = random.randint(1, 11)
								print('Your ace is chosen to be a {0}\n'.format(init_deal_dict[pl, crd]))
								ui_cards.append(init_deal_dict[pl, crd])
						elif re.search("(2_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 2
						elif re.search("(3_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 3
						elif re.search("(4_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 4
						elif re.search("(5_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 5
						elif re.search("(6_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 6
						elif re.search("(7_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 7
						elif re.search("(8_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 8
						elif re.search("(9_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 9
						elif re.search("(10_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 10
						elif re.search("(jack_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 10
						elif re.search("(queen_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 10
						elif re.search("(king_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 10
						ui_card_total += init_deal_dict[pl, crd]
						score_dict[curr_player] = ui_card_total
						ui_cards.append(init_deal_dict[pl, crd])
					print('Your hands total value currently is {0}\n'.format(ui_card_total))
					print("Now that your hand's value is established we will move onto 'hitting' or 'standing'\n")
					while True:
						if ui_card_total > 21:
							print("Your hand's value has gone over 21\n")
							print("Because you have busted, you have no chance of winning\n")
							print("So now it is the next player's turn to select his/her hand\n")
							time.sleep(4)
							score_dict[curr_player] = ui_card_total
							break
						print(
							"Would you like to 'hit' to gain more cards or 'stand' because you are comfortable with your hand's value\n")
						hit_or_stand = int(input('Press 1 to hit and press 2 to stand : '))

						if hit_or_stand == 1:
							ui_card_extra = random.choice(thicc_cards)
							thicc_cards.remove(ui_card_extra)
							# ui_cards.append(ui_card_extra)
							if re.search("(ace_.)", ui_card_extra):
								ace_quest2 = int(input('You have an ace would you like to regard it as a 1 or 11 : '))
								if ace_quest2 == 1:
									print('You have chosen your ace to be a 1\n')
									ui_card_total = ui_card_total + 1
									score_dict[curr_player] = ui_card_total
								elif ace_quest2 == 11:
									print('You have chosen your ace to be a 11\n')
									ui_card_total = ui_card_total + 11
									score_dict[curr_player] = ui_card_total
								else:
									time.sleep(2)
									print(shame)
									ui_card_total = ui_card_total + random.randint(1, 11)
									print('Your ace is chosen to be a {0}\n'.format(ui_card_extra))
									score_dict[curr_player] = ui_card_total
							elif re.search("(2_.)", ui_card_extra):
								print('The card that you have been given randomly is a {0}\n'.format(ui_card_extra))
								ui_card_total += 2
								score_dict[curr_player] = ui_card_total
							elif re.search("(3_.)", ui_card_extra):
								print('The card that you have been given randomly is a {0}\n'.format(ui_card_extra))
								ui_card_total += 3
								score_dict[curr_player] = ui_card_total
							elif re.search("(4_.)", ui_card_extra):
								print('The card that you have been given randomly is a {0}\n'.format(ui_card_extra))
								ui_card_total += 4
								score_dict[curr_player] = ui_card_total
							elif re.search("(5_.)", ui_card_extra):
								print('The card that you have been given randomly is a {0}\n'.format(ui_card_extra))
								ui_card_total += 5
								score_dict[curr_player] = ui_card_total
							elif re.search("(6_.)", ui_card_extra):
								print('The card that you have been given randomly is a {0}\n'.format(ui_card_extra))
								ui_card_total += 6
								score_dict[curr_player] = ui_card_total
							elif re.search("(7_.)", ui_card_extra):
								print('The card that you have been given randomly is a {0}\n'.format(ui_card_extra))
								ui_card_total += 7
								score_dict[curr_player] = ui_card_total
							elif re.search("(8_.)", ui_card_extra):
								print('The card that you have been given randomly is a {0}\n'.format(ui_card_extra))
								ui_card_total += 8
								score_dict[curr_player] = ui_card_total
							elif re.search("(9_.)", ui_card_extra):
								print('The card that you have been given randomly is a {0}\n'.format(ui_card_extra))
								ui_card_total += 9
								score_dict[curr_player] = ui_card_total
							elif re.search("(10_.)", ui_card_extra):
								print('The card that you have been given randomly is a {0}\n'.format(ui_card_extra))
								ui_card_total += 10
								score_dict[curr_player] = ui_card_total
							elif re.search("(jack_.)", ui_card_extra):
								print('The card that you have been given randomly is a {0}\n'.format(ui_card_extra))
								ui_card_total += 10
								score_dict[curr_player] = ui_card_total
							elif re.search("(queen_.)", ui_card_extra):
								print('The card that you have been given randomly is a {0}\n'.format(ui_card_extra))
								ui_card_total += 10
								score_dict[curr_player] = ui_card_total
							elif re.search("(king_.)", ui_card_extra):
								print('The card that you have been given randomly is a {0}\n'.format(ui_card_extra))
								ui_card_total += 10
								score_dict[curr_player] = ui_card_total
							time.sleep(2)
							print('Your hands total value currently is {0}\n'.format(ui_card_total))
							ui_cards.append(ui_card_extra)
							continue
						elif hit_or_stand == 2:
							print('So you are confident in your hand\n')
							print("So now it is the next player's turn to select his/her hand\n")
							time.sleep(4)
							score_dict[curr_player] = ui_card_total
							break
						else:
							print('Because you are incompetent to select an action you will stand\n')
							print("So now it is the next player's turn to select his/her hand\n")
							time.sleep(4)
							score_dict[curr_player] = ui_card_total
							break
					print('score dict = {0}'.format(score_dict), file=fd)
					os.system('clear')
					time.sleep(2)
					continue
				elif curr_player == 'DEALER':
					mi_card_total = 0
					time.sleep(2)
					ace_ctr = 1
					for pl, crd in zip([curr_player, curr_player], ['card1', 'card2']):
						if re.search("(ace_.)", init_deal_dict[pl, crd]):
							if re.search("(ace_.)", init_deal_dict[pl, crd]):
								if ace_ctr == 1:
									ace_ctr = ace_ctr + 1
									ace_quest = 11
								else:
									ace_quest = 1
							else:
								ace_quest = 11
							if ace_quest == 11:
								init_deal_dict[pl, crd] = 11
								mi_card_total += init_deal_dict[pl, crd]
								score_dict[curr_player] = mi_card_total
							elif ace_quest == 1:
								init_deal_dict[pl, crd] = 1
								mi_card_total += init_deal_dict[pl, crd]
								score_dict[curr_player] = mi_card_total
							else:
								init_deal_dict[pl, crd] = random.randint(1, 11)
								mi_card_total += init_deal_dict[pl, crd]
								score_dict[curr_player] = mi_card_total
						elif re.search("(2_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 2
							mi_card_total += init_deal_dict[pl, crd]
							score_dict[curr_player] = mi_card_total
						elif re.search("(3_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 3
							mi_card_total += init_deal_dict[pl, crd]
							score_dict[curr_player] = mi_card_total
						elif re.search("(4_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 4
							mi_card_total += init_deal_dict[pl, crd]
							score_dict[curr_player] = mi_card_total
						elif re.search("(5_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 5
							mi_card_total += init_deal_dict[pl, crd]
							score_dict[curr_player] = mi_card_total
						elif re.search("(6_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 6
							mi_card_total += init_deal_dict[pl, crd]
							score_dict[curr_player] = mi_card_total
						elif re.search("(7_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 7
							mi_card_total += init_deal_dict[pl, crd]
							score_dict[curr_player] = mi_card_total
						elif re.search("(8_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 8
							mi_card_total += init_deal_dict[pl, crd]
							score_dict[curr_player] = mi_card_total
						elif re.search("(9_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 9
							mi_card_total += init_deal_dict[pl, crd]
							score_dict[curr_player] = mi_card_total
						elif re.search("(10_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 10
							mi_card_total += init_deal_dict[pl, crd]
							score_dict[curr_player] = mi_card_total
						elif re.search("(jack_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 10
							mi_card_total += init_deal_dict[pl, crd]
							score_dict[curr_player] = mi_card_total
						elif re.search("(queen_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 10
							mi_card_total += init_deal_dict[pl, crd]
							score_dict[curr_player] = mi_card_total
						elif re.search("(king_.)", init_deal_dict[pl, crd]):
							init_deal_dict[pl, crd] = 10
							mi_card_total += init_deal_dict[pl, crd]
							score_dict[curr_player] = mi_card_total
					print("Now that your hand's value is established we will move onto 'hitting' or 'standing'\n")
					while True:
						if mi_card_total > 21:
							print("DEALER, your hand's value has gone over 21\n")
							time.sleep(2)
							print("Because you have busted, you have no chance of winning\n")
							time.sleep(2)
							print("So now it is the next player's turn to select his/her hand\n")
							time.sleep(4)
							break
						else:
							print(
								"DEALER, would you like to 'hit' to gain more cards or 'stand' because you are comfortable with your hand's value\n")
							print('Press 1 to hit and press 2 to stand : ')
							len_in_deck = len(thicc_cards)
							mi_res = 0
							'''
							if 21 <= mi_card_total >= 16:
								mi_res = 2
							else:
								if 50 <= len_in_deck >= 40:
									mi_res = 1
								elif 39 <= len_in_deck >= 20:
									if 15 <= mi_card_total >= 10:
										# thicc_cards
										temp = len(new_player_list) * 4
										if len(thicc_cards) < temp and re.findall("ace|king|jack|queen", mi_cards_list):
											mi_res = 1
										elif temp <= 4 >= len(mi_cards_list):
											mi_res = 2
									elif 9 <= mi_card_total >= 2:
										mi_res = 1
								elif 19 <= len_in_deck >= 0:
									if 15 <= mi_card_total >= 5:
										if (len(ui_cards) <= 4 and len(mi_cards_list <= 4)) or (len(ui_cards) <= 4 and re.findall("ace|king|jack|queen", mi_cards_list)):
											mi_res = 1
										elif len(ui_cards) <= 4 >= len(mi_cards_list):
											mi_res = 2
									elif 4 <= mi_card_total >= 0:
										mi_res = 1
							'''
							if 21 <= mi_card_total >= 16:
								mi_res = 2
							else:
								if 50 <= len_in_deck >= 20:
									mi_res = 1
								elif 19 <= len_in_deck >= 0:
									if 15 <= mi_card_total >= 5:
										if (len(ui_cards) <= 4 and len(mi_cards_list) <= 4) or (len(ui_cards) <= 4 and re.findall("ace|king|jack|queen", mi_cards_list)):
											mi_res = 1
										elif len(ui_cards) <= 4 >= len(mi_cards_list):
											mi_res = 2
									elif 4 <= mi_card_total >= 0:
										mi_res = 1
								else:
									mi_res = 2
							if mi_res == 1:
								time.sleep(2)
								print('I THINK I WILL HIT\n')
								mi_card_extra = random.choice(thicc_cards)
								thicc_cards.remove(mi_card_extra)
								mi_cards_list.append(mi_card_extra)
								if re.search("(ace_.)", mi_cards_list[-1]):
									time.sleep(2)
									if 21 - mi_card_total < 11:
										mi_cards_list[-1] = 1
										mi_card_total = int(mi_card_total) + mi_cards_list[-1]
										score_dict[curr_player] = mi_card_total
										time.sleep(2)
									else:
										mi_cards_list[-1] = 11
										mi_card_total = int(mi_card_total) + mi_cards_list[-1]
										score_dict[curr_player] = mi_card_total
										time.sleep(2)
								elif re.search("(2_.)", mi_cards_list[-1]):
									mi_cards_list[-1] = 2
									mi_card_total = int(mi_card_total) + mi_cards_list[-1]
									score_dict[curr_player] = mi_card_total
								elif re.search("(3_.)", mi_cards_list[-1]):
									mi_cards_list[-1] = 3
									mi_card_total = int(mi_card_total) + mi_cards_list[-1]
									score_dict[curr_player] = mi_card_total
								elif re.search("(4_.)", mi_cards_list[-1]):
									mi_cards_list[-1] = 4
									mi_card_total = int(mi_card_total) + mi_cards_list[-1]
									score_dict[curr_player] = mi_card_total
								elif re.search("(5_.)", mi_cards_list[-1]):
									mi_cards_list[-1] = 5
									mi_card_total = int(mi_card_total) + mi_cards_list[-1]
									score_dict[curr_player] = mi_card_total
								elif re.search("(6_.)", mi_cards_list[-1]):
									mi_cards_list[-1] = 6
									mi_card_total = int(mi_card_total) + mi_cards_list[-1]
									score_dict[curr_player] = mi_card_total
								elif re.search("(7_.)", mi_cards_list[-1]):
									mi_cards_list[-1] = 7
									mi_card_total = int(mi_card_total) + mi_cards_list[-1]
									score_dict[curr_player] = mi_card_total
								elif re.search("(8_.)", mi_cards_list[-1]):
									mi_cards_list[-1] = 8
									mi_card_total = int(mi_card_total) + mi_cards_list[-1]
									score_dict[curr_player] = mi_card_total
								elif re.search("(9_.)", mi_cards_list[-1]):
									mi_cards_list[-1] = 9
									mi_card_total = int(mi_card_total) + mi_cards_list[-1]
									score_dict[curr_player] = mi_card_total
								elif re.search("(10_.)", mi_cards_list[-1]):
									mi_cards_list[-1] = 10
									mi_card_total = int(mi_card_total) + mi_cards_list[-1]
									score_dict[curr_player] = mi_card_total
								elif re.search("(jack_.)", mi_cards_list[-1]):
									mi_cards_list[-1] = 10
									mi_card_total = int(mi_card_total) + mi_cards_list[-1]
									score_dict[curr_player] = mi_card_total
								elif re.search("(queen_.)", mi_cards_list[-1]):
									mi_cards_list[-1] = 10
									mi_card_total = int(mi_card_total) + mi_cards_list[-1]
									score_dict[curr_player] = mi_card_total
								elif re.search("(king_.)", mi_cards_list[-1]):
									mi_cards_list[-1] = 10
									mi_card_total = int(mi_card_total) + mi_cards_list[-1]
									score_dict[curr_player] = mi_card_total
								continue
							elif mi_res == 2:
								time.sleep(2)
								print('I THINK I WILL STAND\n')
								time.sleep(2)
								print('DEALER, so you are confident in your hand\n')
								time.sleep(2)
								print("DEALER, now it is next player's turn\n")
								score_dict[curr_player] = mi_card_total
								break
							else:
								time.sleep(2)
								print('I THINK I WILL STAND\n')
								time.sleep(2)
								print('DEALER, so you are confident in your hand\n')
								time.sleep(2)
								print("DEALER, now it is next player's turn\n")
								score_dict[curr_player] = mi_card_total
								break
					print('score dict = {0}'.format(score_dict), file=fd)
					os.system('clear')
					time.sleep(2)
					continue
		if len(new_player_list) == 0:
			print('These are the scores for this round :\n')
			time.sleep(1)
			for pl, val in score_dict.items():
				print(pl, "Your hand's value for this round is ----->", val, '\n')
				time.sleep(1)
				if val > 21:
					loser_list.append(pl)
					print(pl, 'has been eliminated for going over 21\n')
					time.sleep(2)
				else:
					winner_dict[pl] = val
			if len(loser_list) == len(player_list):
				print('No Winner in this round')
				continue
			diff_winner_list = list(winner_dict.values())
			for i in range(1, len(diff_winner_list)):
				for j in range(len(diff_winner_list) - 1):
					if diff_winner_list[j] > diff_winner_list[j + 1]:
						diff_winner_list[j], diff_winner_list[j + 1] = diff_winner_list[j + 1], diff_winner_list[j]
			print(diff_winner_list, file=fd)
			for pl, val in winner_dict.items():
				if winner_dict[pl] != diff_winner_list[-1]:
					loser_list.append(pl)
				else:
					winner_list.append(pl)
			print('Winner List is ----> {0} and \n Loser List ----> {1}'.format(winner_list,loser_list), file=fd)
			print('----->UPDATING CREDITS FOR THIS ROUND<-----\n')

			credit = int(total_pot / len(winner_list))

			updateCredits(credit, loser_list, winner_list)
			os.system('clear')
			time.sleep(1)
	print(credit_dict, file=fd)
	announceWinner()


def announceWinner():
	fin_loser_list = []
	fin_winner_list = []
	in_credit_list = list(credit_dict.values())
	for i in range(1, len(in_credit_list)):
		for j in range(len(in_credit_list) - 1):
			if in_credit_list[j] > in_credit_list[j + 1]:
				in_credit_list[j], in_credit_list[j + 1] = in_credit_list[j + 1], in_credit_list[j]
	for pl, val in credit_dict.items():
		if credit_dict[pl] != in_credit_list[-1]:
			fin_loser_list.append(pl)
		else:
			fin_winner_list.append(pl)
	print('------>WINNERS ARE<------\n')
	for elm in fin_winner_list:
		print(elm,'------>',credit_dict[elm],'\n')

	print('------>LOSERS ARE<------\n')
	for elm in fin_loser_list:
		print(elm,'------>',credit_dict[elm],'\n')


def updateCredits(crdt, lsr_list, wnr_list):
	in_credit = crdt
	in_loser_list = lsr_list.copy()
	in_winner_list = wnr_list.copy()


	for pl, scr in credit_dict.items():
		if pl in in_loser_list:
			scr1 = scr - round_bet
			credit_dict[pl] = scr1
			print('{0} has lost {1} credits and has total credits of {2}\n'.format(pl, round_bet, scr1))
			time.sleep(1)
		elif pl in in_winner_list:
			scr1 = scr + in_credit - round_bet
			credit_dict[pl] = scr1
			print('{0} has gained {1} credits and has total credits of {2}\n'.format(pl, in_credit - round_bet, scr1))
			time.sleep(1)
	time.sleep(5)


if __name__ == '__main__':
	main()
