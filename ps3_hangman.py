# Hangman game

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
secretWord = chooseWord(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    flag=1
    for letter in secretWord:
        if letter not in lettersGuessed:
            flag=0
            break
    if flag==1:
        return True
    else:
        return False
            



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    word=''
    for letter in secretWord:
        if letter in lettersGuessed:
            word+=letter
        else:
            word+='_'
    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
  
    remaining=''
    let=string.ascii_lowercase
    for letter in let:
        if letter not in lettersGuessed:
            remaining=remaining+' '+letter
    return remaining         
    

def hangman(secretWord):
	kbinp='1'
	while(kbinp!='0'):
		print("Welcome to the game hangman!")
		l=len(secretWord)
		print("I am thinking of a word that is "+str(l)+" letters long")
		print("------------")
		guessesleft=8
		lettersGuessed=[]
		while guessesleft>0 and not isWordGuessed(secretWord,lettersGuessed):
			print("You have "+str(guessesleft)+" guesses left")
			print("Available letters: "+getAvailableLetters(lettersGuessed))
			print("Please guess a letter: ",end='')
			guessedLetter=input()
			if guessedLetter in lettersGuessed:
				print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed))
			else:
				lettersGuessed.append(guessedLetter)
				if guessedLetter in secretWord:
					print("Good guess: "+ getGuessedWord(secretWord, lettersGuessed))
				elif guessedLetter not in secretWord:
					print("Oops! that letter is not in my word: "+getGuessedWord(secretWord, lettersGuessed))
					guessesleft-=1    
			print("------------") 
		   
		if guessesleft==0 and not isWordGuessed(secretWord,lettersGuessed):
			print("Sorry, you ran out of guesses. The word was "+secretWord)
		else:
			print("Congratulations, you won!")
		print("***************************")
		print("press any key to play again and 0 to exit")
		kbinp=input()


hangman(secretWord)


    
    
