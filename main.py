"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Martina Liga
email: msornova@seznam.cz
"""
import random
import time

# Generování 4 místného čísla s omezeními
def create_number():
    
    incorrect_number = True
    
    while incorrect_number:
        secret_number = random.sample([0,1,2,3,4,5,6,7,8,9], k = 4)
        if secret_number[0] != 0: 
            incorrect_number = False
    return secret_number
    
# Vyžádání vstupu od uživatele
def guess_number():
    guess_number = input("Enter a number:")
    return guess_number

# Kontrola vstupu
def check_input(guess_number):
    lenght = len(guess_number)
    if lenght != 4:
        print("The number must contain 4 digits! Try again")
        return False
    elif guess_number[0] == "0":
        print("The number could not start with 0! Try again")
        return False
    elif not guess_number.isnumeric():
       print("Only digits are accepted! Try again")
       return False
    elif len(list(guess_number)) != len(set(guess_number)):
        print("Number includes duplicities! Try again")
        return False
    else:
        return True

# Úprava vstupu na list a int
def list_guess(guess_number):
    guess_n = []
    for i in guess:
        guess_n.append(int(i))
    return guess_n
    

# Vyhodnocení - porovnání generovaného čísla a tipu od uživatele
def perform_evaluation(secret, guess): 
    
    evaluation = dict(bulls = 0, cows = 0)
    
    for idx, secret_value in enumerate(secret):
        for idy, guess_value in enumerate(guess):
            if idx == idy and secret_value == guess_value:
                evaluation['bulls'] += 1
            elif idx != idy and secret_value == guess_value:
                evaluation['cows'] += 1
    return(evaluation)

# Vypis vyhodnocení (jednotné a množné číslo)
def print_evaluation(bulls, cows):
    if bulls == 1 and cows != 1:
        print(bulls, "bull, ",cows, "cows")
    elif bulls == 1 and cows == 1:
        print(bulls, "bull, ", cows, "cow")
    elif bulls != 1 and cows == 1:
        print(bulls, "bulls ", cows, "cow")
    else:
        print(bulls, "bulls, ", cows, "cows")

# MAIN
# Úvodní pozdrav
print("Hi there!", "-"*47, 
      "I've generated a random 4 digit number for you.", 
      "Let's play a bulls and cows game.",
      sep = "\n")

# Tvorba čísla
secret = create_number()
print(secret)

# Spuštění času
start_time = time.time()

# Hra
counter = 0
in_the_middle_of_guessing = True

while in_the_middle_of_guessing:
    
    incorrect_input = True
    while incorrect_input:
        guess = guess_number()
        if check_input(guess):
            incorrect_input = False
    guess_n = list_guess(guess)
    
    evaluation = perform_evaluation(secret, guess_n)
    
    print_evaluation(evaluation["bulls"], evaluation["cows"])
   
    counter += 1
    if evaluation["bulls"] == 4:
        in_the_middle_of_guessing = False
print("Correct, you have guessed the right number in ", counter, "guesses") 

# Skončení času
end_time = time.time()

print("it took", round(end_time - start_time, ndigits=0), "seconds to guess the number")