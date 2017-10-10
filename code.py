# This program was developed to display
# the result of rolling a pair of dice

import random

def intro():
    print ('This program enables the user to simulate a throw')
    print ('of a pair of dice')
    print()
    print ("Rolling the dice ....")
    print ()
    print ("Result loading ....")
    print()
    print ('Here are the results of rolling the dice:')
    print ()

def main():
    intro()
    dice_throw = 'y'
    while dice_throw == 'y' or dice_throw == 'Y':
        for num in range (2):
            random_num = random.randint (1, 6)
            print (random_num, end=" ")
            print()
        dice_throw = input("""Do you want to continue with throwing the dice
If yes, type 'y' 
If no, type 'n': """)
            
main()
