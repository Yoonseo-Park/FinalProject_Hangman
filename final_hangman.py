import random

HANGMAN = [
    '''
  *---*
  |   |
      |
      |
      |
      |
========= ''',
    '''
  *---*
  |   |
  @   |
      |
      |
      |
=========''',
    '''
  *---*
  |   |
  @   |
  |   |
      |
      |
=========''',
    '''
  *---*
  |   |
  @   |
 /|   |
      |
      |
=========''',
    '''
  *---*
  |   |
  @   |
 /|)  |
      |
      |
=========''',
    '''
  *---*
  |   |
  @   |
 /|)  |
 /    |
      |
=========''',
    '''
  *---*
  |   |
  @   |
 /|)  |
 / >  |
      |
=========''']

words = ['alligator', 'airplane', 'balloon', 'bear', 'camel', 'clam', 'decision', 'donkey',
'eagle', 'elevator', 'fighter', 'flag', 'goose', 'government', 'hawk', 'hawaii', 'icecream', 'italy',
'jewelry', 'juice', 'knowledge', 'knife', 'lion', 'lizard', 'monkey', 'mouse', 'nurse', 'napkin',
'owl', 'orange', 'panda', 'python', 'question', 'queen', 'rabbit', 'rainbow', 'shark', 'spider',
'tiger', 'toilet', 'university', 'umbrella', 'vase', 'victory', 'whale', 'world', 'yellow', 'youth' 'zebra', 'zombie']

print('')
print(' ============================= ')
print('|        W E L C O M E        |')
print('|            T   O            |')
print('|        H A N G M A N        |')
print('|          W O R L D          |')
print(' ============================= ')
print('')

# get a randomly chosen word from the words list
def getRandomWord(word_list):
    word_index = random.randint(0, len(word_list)-1)
    return word_list[word_index]

# let the player know how many trials are left by showing the Hangman
def gameBoard(HANGMAN, wrong_letters, correct_letters, secret_word):
    print(HANGMAN[len(wrong_letters)])
    print('Wrong letters list :', end=' ')
    for letter in wrong_letters:
        print(letter, end=' ')
    print('')

    blanks = '_' * len(secret_word)
    # fill blanks with correctly guessed letters
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    # print blanks with correctly guessed letters
    for letter in blanks: 
        print(letter, end=' ')
    print()


def getGuess(already_guessed):
    while True:
        guess = input("Guess a letter. : ").lower()
        if len(guess) != 1: # multiple letters are not accepted
            print('Please enter a single letter.')
        elif guess in already_guessed: # If the player entered already-guessed-letter
            print('You have already guessed that letter. Enter another one.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz': # only 'letters' are accepted
            print('Please enter a LETTER.')
        else:
            return guess

wrong_letters = ''
correct_letters = ''
secret_word = getRandomWord(words)
gameIsDone = False

def playAgain():
    print('Do you want to play again? [yes/no]')
    return input().lower().startswith('y')

while True:
    gameBoard(HANGMAN, wrong_letters, correct_letters, secret_word)

    # Let the player enter a letter
    guess = getGuess(wrong_letters + correct_letters)

    if guess in secret_word:
        correct_letters = correct_letters + guess
        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                foundAllLetters = False
        if foundAllLetters == True:
            print(f'Congratulations! The secret word is "{secret_word.upper()}"! You are the winner!')
            gameIsDone = True

    else:
        wrong_letters = wrong_letters + guess
        # Check if the player has run out of guesses
        if len(wrong_letters) == len(HANGMAN) - 1:
            gameBoard(HANGMAN, wrong_letters, correct_letters, secret_word)
            print('You have run out of guesses!')
            print(f'After {str(len(wrong_letters))} wrong guesses and {str(len(correct_letters))} correct guesses, the secret word was "{secret_word.upper()}"!')
            gameIsDone = True

    # Ask the player if he/she wants to play again.
    if gameIsDone:
        if playAgain():
            wrong_letters = ''
            correct_letters = ''
            gameIsDone = False
            secret_word = getRandomWord(words)
        else:
            break