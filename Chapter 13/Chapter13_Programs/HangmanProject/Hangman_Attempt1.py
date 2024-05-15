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


def play_game(secret_word):
    correct_guesses = ''
    incorrect_guesses = ''

    partial_word = '_' * len(secret_word)
    print(f'Your word is {len(secret_word)} letters long')
    print('You can make maximum 7 incorrect guesses\n')

    while len(incorrect_guesses) < 7:
        guessed_letter = get_guess(correct_guesses + incorrect_guesses)
        if guessed_letter in secret_word:
            print('Good, you made a correct guess')
            correct_guesses += guessed_letter
            partial_word = get_partial_word(secret_word, correct_guesses)
            print_with_spaces(partial_word)
            if partial_word == secret_word:
                print('Congratulations, you won the game')
                print(f'You guessed the word in {len(correct_guesses)} correct guesses ', end=' ')
                print(f'and {len(incorrect_guesses)} incorrect guesses')
                break
        else:
            print('Sorry, incorrect guess')
            incorrect_guesses += guessed_letter
            print_with_spaces(partial_word)

    else:
        print('You made 7 incorrect guesses')
        print('Now no more attempts left, you have lost the game')
        print('The word was', secret_word)


########################################################################

print('.' * 50, 'Welcome to HANGMAN', '.' * 50)
secret_word = 'circumference'
play_game(secret_word)
