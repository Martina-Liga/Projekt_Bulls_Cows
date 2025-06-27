"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Martina Liga
email: msornova@seznam.cz
"""
import random
import time

<<<<<<< HEAD
=======
# Generování 4 místného čísla s omezeními
>>>>>>> eaa1a0da1dda7e562d5072d7d842d0caae860e36
def create_number() -> list:
    """
    The function generates 4 digit number having below characteristics:
    - first digit is not 0
    - digits are unique
    """

    sequence_set_1digit = {1,2,3,4,5,6,7,8,9}
    sequence_list_1digit = list(sequence_set_1digit)
    secret_number_start = random.sample(sequence_list_1digit, k = 1)
    
    sequence_set_rest = {0,1,2,3,4,5,6,7,8,9}-set(secret_number_start)
    sequence_list_rest = list(sequence_set_rest)
    secret_number_end = random.sample(sequence_list_rest, k = 3)
    
    secret_number = secret_number_start + secret_number_end

    return secret_number
    
def guess_number():
    """ The function requests the user to type the number"""
    attempt = input("Enter a number:")
    print(attempt)
    return attempt
    


def check_input(guess_number) -> bool:
"""The function checks whether the user input is in line with the rules"""
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
print(type(secret))
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