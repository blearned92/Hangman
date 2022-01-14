import random

def print_0_mistakes():
    print("-------------------------------------------")
    print("  |------|-")
    print("  |      | ")
    print("  |        ")
    print("  |         ")
    print("  |        ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_1_mistakes():
    print("-------------------------------------------")
    print("  |------|-")
    print("  |      | ")
    print("  |      O ")
    print("  |         ")
    print("  |         ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_2_mistakes():
    print("-------------------------------------------")
    print("  |------|-")
    print("  |      | ")
    print("  |      O ")
    print("  |      | ")
    print("  |      | ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_3_mistakes():
    print("-------------------------------------------")
    print("  |------|-")
    print("  |      | ")
    print("  |      O ")
    print("  |     /| ")
    print("  |      | ")
    print("  |        ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_4_mistakes():
    print("-------------------------------------------")
    print("  |------|-")
    print("  |      | ")
    print("  |      O ")
    print("  |     /|\\")
    print("  |      |  ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_5_mistakes():
    print("-------------------------------------------")
    print("  |------|-")
    print("  |      | ")
    print("  |      O ")
    print("  |     /|\\")
    print("  |      | ")
    print("  |     /   ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_6_mistakes():
    print("-------------------------------------------")
    print("  |------|-")
    print("  |      | ")
    print("  |      O ")
    print("  |     /|\\")
    print("  |      | ")
    print("  |     / \\")
    print(" /|\\       ")
    print("/ | \\      ")

def print_game_status():
    if mistakes == 0:
        print_0_mistakes()
    elif mistakes == 1:
        print_1_mistakes()
    elif mistakes == 2:
        print_2_mistakes()
    elif mistakes == 3:
        print_3_mistakes()
    elif mistakes == 4:
        print_4_mistakes()
    elif mistakes == 5:
        print_5_mistakes()
    elif mistakes == 6:
        print_6_mistakes()

    print("-------------------------------------------")
    print("Word: ", end="")
    for element in guesses:
        print(f"{element} ", end='')
    print(f"\nYou have {remaining_guesses} guess(es) remaining")
    print("Guesses so far: " + str(lettersGuessed))
    print("-------------------------------------------")


words = ["swordfish", "chilli-dog", "logarithm", "cheeseburger", 
"giraffe", "milkshake", "rhythm", "noodle-cup", "stegosaurus", 
"rubik's cube", "Python", "Data Structure", "Algorithm"]
guesses = []
lettersGuessed = []
remaining_guesses = 6
mistakes = 0
word_index = random.randint(0, len(words)-1)
word = words[word_index].upper()

for i in range(len(word)):
    if word[i].isalpha():
        guesses.append("_")
    elif word[i] == " ":
        guesses.append(" ")
    elif word[i] == "'":
        guesses.append("'")
    else:
        guesses.append("-")

print("-------------------------------------------")
print("""Let's Play Hangman! 
Guess the randomly assigned word within a limited amount of
guesses and save the poor stickman from his doom!

Rules: 
- Only Letters count as valid inputs.
- If a word is used as an input, only the first letter will 
  be used.
- Letters are not case sensitive.
- Letters can only be guessed once. Repeats do not count
  against you. 
- After 6 failed guesses, you lose!
- Guess every letter correctly to win.

  Good luck!
  """)
print("-------------------------------------------")

startGame = False

while not startGame:
    user_input = input("Type 'Y' to Start: ")
    if user_input.upper() != 'Y':
        pass
    else:
        print("-------------------------------------------")
        print("Save the stickman from his doom!")
        startGame = True


game_over = False
while not game_over:
    print_game_status()

    user_input = input("Please enter a letter:\n")
    

    if not user_input.isalpha():
        print("-------------------------------------------")
        print("That's not a valid input. Please try again.")
    elif user_input in lettersGuessed:
        print("-------------------------------------------")
        print("You have already guessed that letter!")
    else:
        letter = user_input[0].upper()
        lettersGuessed.append(user_input[0])
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guesses[i] = letter
                    print("-------------------------------------------")
                    print("Good guess! " + guesses[i] + " is a part of the word!")
            if "_" not in guesses:
                game_over = True

        else:
            print("-------------------------------------------")
            print("Sorry, that's not part of of the word!")
            remaining_guesses -= 1
            mistakes += 1
            if mistakes == 6:
                game_over = True




if mistakes == 6:
    print("--------------------------------------")
    print("You Lose. Please Try Again!")
    print("The Correct Answer Was: " + word + "!")
    print("You Guessed: " + str(" ".join(guesses)))
    print("--------------------------------------")
else: 
    print("--------------------------------------")
    print("Congratulations! You Won!")
    print("The Correct Answer Was: " + word + "!") 
    print("You Guess Like a Pro! The Stickman is Saved!")
    print("--------------------------------------")
