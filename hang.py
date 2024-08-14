import random

def choose_word():
    words = ['java', 'python', 'computer', 'hangman', 'programming']
    return random.choice(words)

def hangman():
    word = choose_word()
    guessed_letters = []
    tries = 4
    
    while tries > 0:
        guessed_word = ''.join(letter if letter in guessed_letters else '_' for letter in word)
        
        if guessed_word == word:
            print(f'Congratulations! You guessed the word: {word}')
            return
        
        print(f'Word: {guessed_word}')
        print(f'Tries left: {tries}')
        
        guess = input('Guess a letter or the whole word: ').lower()
        
        if len(guess) == 1:  # Guessing a letter
            if guess in guessed_letters:
                print('You already guessed that letter!')
            elif guess in word:
                print('Correct!')
                guessed_letters.append(guess)
            else:
                print('Incorrect!')
                tries -= 1
        else:  # Guessing the whole word
            if guess == word:
                print(f'Congratulations! You guessed the word: {word}')
                return
            else:
                print('Incorrect!')
                tries -= 1
        
        print()  # Print empty line for spacing
    
    print(f'Oops! You ran out of tries. The word was: {word}')

if __name__ == '__main__':
    print('Welcome to Hangman!')
    hangman()
