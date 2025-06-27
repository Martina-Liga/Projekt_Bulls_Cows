import random
import time

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

# MAIN
# Úvodní pozdrav
print("Hi there!", "-"*47, 
      "I've generated a random 4 digit number for you.", 
      "Let's play a bulls and cows game.",
      sep = "\n")
secret = create_number()
print(secret)