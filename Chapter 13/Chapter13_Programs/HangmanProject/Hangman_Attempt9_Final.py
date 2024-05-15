import random

hangman_drawings = (
    '''
                  ______
                 |      |        
                        |      
                        |     
                        |         
                        |     
               _________|__
    ''',
    '''
                  ______
                 |      |        
                 O      |      
                        |     
                        |         
                        |     
               _________|__
    ''',
    '''
                  ______
                 |      |        
                 O      |      
                 |      |     
                        |         
                        |     
               _________|__
    ''',
    '''
                  ______
                 |      |        
                 O      |      
                /|      |     
                        |         
                        |     
               _________|__
    ''',
    '''
                  ______
                 |      |        
                 O      |      
                /|\     |     
                        |         
                        |     
               _________|__
   ''',
    '''
                   ______
                  |      |        
                  O      |      
                 /|\     |     
                  |      |         
                         |     
                _________|__
    ''',
    '''
                   ______
                  |      |        
                  O      |      
                 /|\     |     
                  |      |         
                 /       |     
                _________|__
    ''',
    '''
                   ______
                  |      |        
                  O      |      
                 /|\     |     
                  |      |         
                 / \     |     
                _________|__
    ''')


def ask_if_guessed(secret_word):
    response = input('If you have guessed the word, enter it otherwise press Enter : ')

    if response == '':
        return False
    elif response == secret_word:
        return True
    else:
        print('No this is not the word ....')
        return False


def get_guess(letters_guessed):
    if letters_guessed:
        print('Letters guessed already : ', end=' ')
        for letter in letters_guessed:
            print(letter, end=' ')
        print()

    while True:
        letter = input('Guess a letter : ').lower()
        if len(letter) != 1 or letter not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a single letter')
        elif letter in letters_guessed:
            print('You already guessed this letter before, enter another letter\n')
        else:
            break
    return letter


def get_partial_word(secret_word, correct_guesses):
    partial_word = ''
    for letter in secret_word:
        if letter in correct_guesses:
            partial_word += letter
        else:
            partial_word += '_'
    return partial_word


def print_with_spaces(string):
    print()
    for ch in string:
        print(ch, end=' ')
    print('\n\n')


def play_game(secret_word, hint):
    correct_guesses = ''
    incorrect_guesses = ''
    hint_shown = False

    partial_word = '_' * len(secret_word)
    print(f'Your word is {len(secret_word)} letters long')
    print('You can make maximum 7 incorrect guesses\n')
    print(hangman_drawings[0])

    while len(incorrect_guesses) < 7:
        guessed_letter = get_guess(correct_guesses + incorrect_guesses)
        if guessed_letter in secret_word:
            print('Good, you made a correct guess')
            correct_guesses += guessed_letter
            partial_word = get_partial_word(secret_word, correct_guesses)
            print_with_spaces(partial_word)
            if partial_word == secret_word or ask_if_guessed(secret_word) == True:
                print('Congratulations, you won the game')
                print(f'You guessed the word in {len(correct_guesses)} correct guesses ', end=' ')
                print(f'and {len(incorrect_guesses)} incorrect guesses')
                break
        else:
            print('Sorry, incorrect guess')
            incorrect_guesses += guessed_letter
            print(hangman_drawings[len(incorrect_guesses)])
            print_with_spaces(partial_word)

        if len(incorrect_guesses) == 5 and hint_shown == False:
            print('You can make only 2 more mistakes, here is a hint for you')
            print(f'Meaning of the secret word is - {hint}\n')
            hint_shown = True
    else:
        print('You made 7 incorrect guesses')
        print('Now no more attempts left, you have lost the game')
        print('The word was', secret_word)


def get_a_word(number_of_words):
    with open('words.txt', 'r') as file:
        x = random.randint(1, number_of_words)
        for i in range(x):
            line = file.readline()

    return line.split(',')


########################################################################

print('.' * 50, 'Welcome to HANGMAN', '.' * 50)

used_words = []

with open('words.txt', 'r') as file:
    number_of_words = 0
    for line in file:
        number_of_words += 1

while True:
    secret_word, hint = get_a_word(number_of_words)
    while secret_word in used_words:
        secret_word, hint = get_a_word(number_of_words)
    used_words.append(secret_word)
    play_game(secret_word, hint)

    response = input('\nWant to play again (y/n) : ')
    if response == 'n':
        break
