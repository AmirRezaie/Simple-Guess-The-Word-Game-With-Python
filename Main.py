print("Welcome. For Start The Game, Enter 'START' And Enjoy")

def start_game():
    st = 0
    try:
        st = input('..')
        if st == "START":
            print("Here's Our List")
            show_list()
        else:
            print("For Begin The Game, You Must Enter 'START'")
            start_game()
    except ValueError:
        print("With {} We Can't Contine".format(st))

def show_list():
    print(wordslist)
    ready = 0
    print('Are U Ready For Start The Game? yes or no?')
    try:
        ready = input(".. ")
        if ready == "yes":
            print("Guess The Word")
            run_game()
        else:
            print("See U Later")
    except ValueError:
        print("With {} We Can't Contine".format(st))
        
wordslist = ["madrid","istanbul","new york","london","rome","milan","budapst","tehran","manchester","hamburg"]
import random

secret_word=random.choice(wordslist)

def run_game():
    guesses = []
    guess = 0

    while len(guesses) <= 5:
        try:
            guess = input(".. ")
        except ValueError:
            print("{} Isn't a word".format(guess))
        else:
            if guess == secret_word:
                print("{} was my word and you win".format(guess))
                break
            else:
                print("Your Guess Is Wrong. Pls Select Another Word")
        guesses.append(guess)
    else:
        print("You Lose! My Word Was {}".format(secret_word))
start_game()
