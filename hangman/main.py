# -------------- PLEASE FORK ---------------
# ---- DO NOT MODIFY ANYTHING IN THIS STARTER CODE --------

import random
import time

# --- DO NOT MODIFY ANYTHING IN THIS SECTION ----

# required for importing from the words list.
# Read wordsList into a file in Python.
with open ('wordsList.txt') as filename:
  words = filename.read() 
# Split text file by comma and save to wordBank
wordBank = words.split(',')
# wordBank now has a list of 3668 words ranging from 8-letters to 12-letters.
#--------------------------------------------------
# Begin your project code here

def hangmanDrawing(errors):#logic to draw the which hangman to be implemented later when the user gets something wrong based on the number of errors made
  if errors == 0:
    print("_____\n" + "|    |\n" + "|     \n" + "|     \n" + "|     \n" + "|     \n" + "|_____")
  if errors == 1:
    print("_____\n" + "|    |\n" + "|    O\n" + "|     \n" + "|     \n" + "|     \n" + "|_____")
  if errors == 2:
    print("_____\n" + "|    |\n" + "|    O\n" + "|    |\n" + "|    |\n" + "|     \n" + "|_____")
  if errors == 3:
    print("_____\n" + "|    |\n" + "|    O\n" + "|   /| \n" + "|    |\n" + "|     \n" + "|_____")
  if errors == 4:
    print("_____\n" + "|    |\n" + "|    O\n" + "|   /|\ \n" + "|    |\n" + "|   \n" + "|_____")
  if errors == 5:
    print("_____\n" + "|    |\n" + "|    O\n" + "|   /|\ \n" + "|    |\n" + "|   /\n" + "|_____")
  if errors == 6:
    print("_____\n" + "|    |\n" + "|    O\n" + "|   /|\ \n" + "|    |\n" + "|   / \ \n" + "|_____")
def replaceDisplay(letter, word, list):#def for when to change to change the blank dashes to some with the corresponding letters --> makes program more efficient
  for i in range(len(word)):
    if word[i] == letter:
      list[i] = letter
  return " ".join(displayList)
  
print("Welcome to the Hangman Game!\n")
name = input("What is you name: ")#Welcome and personalization via name
time.sleep
print("OK", name, "The rules are pretty straightforward:")#Stating game rules
print("______________________________________")
print("  -Like the real game, you will have to guess a word with a certain number of letter which I will tell you")
print("  -You can reveal parts of the word by guessing a letter each time")
print("  -If your guess is wrong, a body part is drawn on the hangman")
print("  -If the hangman is complete --> you LOSE")
print("  -If the word is revealed --> you WIN")
print("STARTING GAME\n")
print("______________________________________\n")
time.sleep(3)
while True:
  correctWord = random.choice(wordBank)#initializing variables and lists that are curucial and universal
  displayList = []
  errorGuess = 0
  correctGuess = 0
  wrongBank = []
  correctBank = []
  print("\n"+ name, "I'm thinking of a " + str(len(correctWord)) + " letter word")#tells user the number of letters
  for i in range(len(correctWord)):
    displayList.append("_")
  displayDash = " ".join(displayList)#joining the items in the list to form the dashes thatare displayed
  while True:
    hangmanDrawing(errorGuess)#calls the hangman drawing function
    if correctGuess == len(correctWord):#condition for if the word is revealed based on the number of correct guesses matches the length of the word
      time.sleep(2)
      print("*****************************************")
      print("\nCongrats", name+ "! you have revealed the word and WON the game.")#congradulations
      break
    elif errorGuess == 6:#condition for if the hangman is complete by checking whether the 
      time.sleep(2)
      print("*****************************************")
      print("\nAww man, you weren't able to get the word in time. It was '" + correctWord + "' by the way")
      time.sleep(0.5)#saying they lost
      print("Don't worry,", name, "I bet you can get it next time")
      break
    print("\n" + displayDash)#printing the dashes
    print("WRONG BANK:", wrongBank, "\n")#displaying wrong bank
    time.sleep(1)
    userLetter = input("Gimme a letter to guess: ")#user input for guessing letter
    if userLetter in correctWord:#if the user has guessed this before if the letter was correct
      if userLetter in correctBank:
        time.sleep(0.5)
        print("The letter is in the word but you have used it before")
      else:#if the letter is correct; updaitng all the other varaibles
        correctBank.append(userLetter)
        time.sleep(1)
        print("Good guess!", "'", userLetter, "'", "was part of the word and it occures", correctWord.count(userLetter), "times")
        correctGuess += 1 * correctWord.count(userLetter)#weighted addition to the ammount of correct guesses because one guess coudl reveal multiple spaces of the same letter
        displayDash = replaceDisplay(userLetter, correctWord, displayList)#uses the replaceDisplay function to efficiently replace dashes with letters that have been guessed
    else:
      time.sleep(1)
      print("Sorry,", userLetter, "was not part of the word")#when they have guessed it wrong
      errorGuess += 1#updating errorguess
      if userLetter in wrongBank:#if they have used this letter before
        time.sleep(0.5)
        print("You used that letter before btw")
      else:
        wrongBank.append(userLetter)#updating hte wrong bank
  playAgain = input("Would you like to play AGAIN [Y/N]: ").upper()#asking to play again
  if playAgain == "Y":#if yes then setting up new game
    print("\nGreat! I'll set up another game")
    print("RESTARTING...")
    time.sleep(3)
    print("_________________________________________")
  elif playAgain == "N":#if no then breakign from loop and thanking them for their time
    print("\nOk, I had a great time though. Thanks", name+ "!")
    break
      

  

