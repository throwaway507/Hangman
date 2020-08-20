import random
from hangmanSketches import hangmans

print("Welcome to the hangman game!")
print("You have to discover the secret word by guessing every letter that is in that word.")
print("Each time you guess correctly a letter uncovers.")
print("Each time you guess the wrong letter you lose one life.")
print("You have only three lives thus use them wisely!")

max_lives = 7
current_lives = max_lives
indexes = []
win = False
misses = ''
tried = ''

with open('dictionary.txt') as f:
    content = f.read().split('\n')

word_to_guess = random.choice(content).lower()
underscores = "_ " * len(word_to_guess)

while current_lives > 0:
    print(hangmans[max_lives - current_lives])
    print(underscores)
    print()
    print(f"You have {current_lives} lives left.")
    print(f"Misses: {misses}")

    letter = input("Type the letter: ").lower()
    if len(letter) != 1 or letter == ' ':
        print("Wrong input. Try again.")
    elif letter in tried or letter in misses:
        print("You have already tried this letter, try a different one.", end='')

    else:
        tried += letter
        if letter in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == letter:
                    indexes.append(i)
            underscores = ''

            for j in range(len(word_to_guess)):
                if j in indexes:
                    underscores += word_to_guess[j]
                    underscores += ' '
                else:
                    underscores += "_ "

            print(f"\nGood job! '{letter}' is in the word.")
            if '_' not in underscores:
                win = True
                break

        else:
            underscores = ''
            for j in range(len(word_to_guess)):
                if j in indexes:
                    underscores += word_to_guess[j]
                    underscores += ' '
                else:
                    underscores += "_ "

            current_lives -= 1
            if letter not in misses:
                if misses:
                    misses += ", "
                misses += letter

            print("\nWrong letter! You are losing one life.")

print(hangmans[max_lives - current_lives])

if win:
    print("You have guessed the word! Congratulations!")
else:
    print(f"You have zero lives. You lost, the word was '{word_to_guess}', better luck next time!")
    print(f"Misses: {misses}")
