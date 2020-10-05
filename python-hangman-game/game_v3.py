# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # construct method
    def __init__(self, word):
        self.word = word
        self.missed_letters = []
        self.guessed_letters = []

    # method to guess the letter
    def guess(self, letter):

        # if the letter passed here is in the word picked and the letter is not in the letters already guessed
        # put this letter in the variable of guessed letters

        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)

        # if letter is not in the word picked and is not in the variable of missed letters
        # put this ltter in the variable of missed letters
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    # method to verify if it's game over
    def hangman_over(self):
        return self.hangman_won() or (len(self.missed_letters) == 6)

    # method to verify if the player won
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False

    # method for not showing the letter on the board
    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    # method for checking game status and print the board on screen
    def print_game_status(self):
        print(board[len(self.missed_letters)])
        print('\nPalavra: ' + self.hide_word())
        print('\nLetras erradas: ', )
        for letter in self.missed_letters:
            print(letter, )
        print()
        print('Letras corretas: ', )
        for letter in self.guessed_letters:
            print(letter, )
        print()


# method to read a random word in the file words.txt
def rand_word():
    with open("words.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# method main, execute the game
def main():

    # object
    game = Hangman(rand_word())

    # while game is not finished, print status, request a letter and read the character
    while not game.hangman_over():
        game.print_game_status()
        user_input = input('\Type a letter : ')
        game.guess(user_input)

    # verify game status
    game.print_game_status()

     # according with status, print it to the user
    if game.hangman_won():
        print('\Congrats! You win!!')
    else:
        print('\nGame over! You loose.')
        print('The word was ' + game.word)



# start program
if __name__ == "__main__":
    main()

