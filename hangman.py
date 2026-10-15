import random

words = ["apple", "tiger", "house", "water", "chair"]

word = random.choice(words)

guessed = ["_"] * len(word)

wrong_guesses = 0

while wrong_guesses < 6 and "_" in guessed:

    print("\nWord:", " ".join(guessed))
    print("Wrong guesses:", wrong_guesses, "/ 6")

    letter = input("Guess a letter: ").lower()
    if letter in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter

    else:
        print("Wrong!")
        wrong_guesses += 1

if "_" not in guessed:
    print("\n🎉 You won!")
    print("The word was:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)