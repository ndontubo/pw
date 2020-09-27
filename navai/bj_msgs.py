#!/usr/bin/python3.5 -tt


"""
Author Nav Don
"""

global msg1, msg2, msg3, msg4, name, deck, mi_res, myRules

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

