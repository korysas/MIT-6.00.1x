# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

from subprocess import call
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

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False

    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            result += letter + ' '
        else:
            result += '_ '

    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available_letters = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        available_letters.remove(letter)
    
    return ''.join(available_letters)


def get_input(available_letters):
    success = False
    while not success:
        print('Guess a letter: ', end='')
        user_input = input()
        if len(user_input) > 1:
            if user_input[0] not in string.ascii_lowercase:
                print('WARNING: Please enter an alphabetical character')
                continue

            print('WARNING: more than one character, taking the first character as input')

            if user_input[0] not in available_letters:
                print('WARNING: letter already guessed')
                continue

            return user_input[0]

        if user_input not in available_letters:
            print('WARNING: letter already guessed')
            continue

        return user_input


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    is_won = False
    no_guesses = 0
    MAX_GUESSES = 7
    lettersGuessed = list()

    while not is_won and no_guesses <= MAX_GUESSES:
        # clear the screen
        tmp = call('clear', shell=True)

        # show secret word
        print(getGuessedWord(secretWord, lettersGuessed), end='\n\n')

        # show available letters
        print('Available letters: ', end='')
        print(getAvailableLetters(lettersGuessed), end='\n\n')

        # show number of guesses remaining
        print('Guesses remaining: ' + str(MAX_GUESSES - no_guesses + 1), end='\n\n')

        # prompt for user input
        letter = get_input(getAvailableLetters(lettersGuessed))
        lettersGuessed.append(letter)

        if letter in secretWord:
            getGuessedWord(secretWord, lettersGuessed)
            is_won = isWordGuessed(secretWord, lettersGuessed)
            continue

        no_guesses += 1

    if is_won:
        print('\nYou Win!')
        return 0

    print('\nYou lose :(')
    return 1


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
