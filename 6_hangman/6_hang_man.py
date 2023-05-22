
import random
from hangman_art import stages, logo
from hangman_words import word_list

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(f'Pssst, the solution is {chosen_word}.')
print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f'You already gussed {guess}')
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f'The letter {guess} is not in this word. You lose a life. \n You have {lives} lives left.')
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print(f'You win. You had {lives} lives left.')

    print(stages[lives])