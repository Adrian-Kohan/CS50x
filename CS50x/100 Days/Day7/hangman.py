import random

word_list = ["ardvark", "baboon", "camel"]
#randomly chosen a word from word_list and assign it to a variable named word_chosen
chosen_word = random.choice(word_list)
print(chosen_word)
#ask the user to guess a letter and assign it to a variable called guess. make guess lowercase
guess = input("Guess a letter: ").lower()
guess_list = []
for i in chosen_word:
    guess_list.append("_")
#check if the letter user guessed is one of the lettere in the chosen word
for i in chosen_word:
    if guess == i:
        guess_list[i] = guess
        print(quess_list)
