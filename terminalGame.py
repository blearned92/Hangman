import random

def print_6_mistakes():
    print("  |------|-")
    print("  |      | ")
    print("  |        ")
    print("  |         ")
    print("  |        ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_1_mistakes():
    print("  |------|-")
    print("  |      | ")
    print("  |      O ")
    print("  |         ")
    print("  |         ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_2_mistakes():
    print("  |------|-")
    print("  |      | ")
    print("  |      O ")
    print("  |      | ")
    print("  |      | ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_3_mistakes():
    print("  |------|-")
    print("  |      | ")
    print("  |      O ")
    print("  |     /| ")
    print("  |      | ")
    print("  |        ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_4_mistakes():
    print("  |------|-")
    print("  |      | ")
    print("  |      O ")
    print("  |     /|\\")
    print("  |      |  ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_5_mistakes():
    print("  |------|-")
    print("  |      | ")
    print("  |      O ")
    print("  |     /|\\")
    print("  |      | ")
    print("  |     /   ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_6_mistakes():
    print("  |------|-")
    print("  |      | ")
    print("  |      O ")
    print("  |     /|\\")
    print("  |      | ")
    print("  |     / \\")
    print(" /|\\       ")
    print("/ | \\      ")

words = ["swordfish", "chillidog", "logarithm", "android", "giraffe", "beautiful", "rhythm"]
guesses = []
remaining_guesses = 6
mistakes = 0
word_index = random.randint(0, len(words)-1)
word = words[word_index].upper()
print(word)

