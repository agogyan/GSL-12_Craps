## GSL-12, TUMO Labs project Craps!
## Rules:
## The player should roll two dice. If the sum of both of them is 7 or 11 the 
## player wins. If the sum is 2, 3 or 12 (craps) the casino wins. If during 
## the first roll the sum is 4, 5, 6, 8, 9 or 10, that number becomes the 
## “goal” number. To win, the player should roll the dice till they roll the 
## goal number again. If the player rolls a 7 before rolling the goal number, 
## they lose.

import random

#################################################
## Defining a function "dice" which generates two random numbers
## and returns their sum
def dice():
    value1 = random.randrange(1, 7)
    value2 = random.randrange(1, 7)
    total_sum = value1 + value2
    print(f"Dice 1 value: {value1}\nDice 2 value: {value2}\nSum is: {total_sum}")
    return total_sum

#################################################
## Function "roll" which prompts the user to write 'wow',
## which is equivalent to rolling dice
def roll():
    print("Please, roll the dice! Just type 'WOW' ")
    roll1 = input().strip('!.').lower() # storing the typed word and cutting any spaces or ., ! symbols
    # Checking if the input is correct. If it's not, waiting for a correct input
    if roll1 !='wow':
        print('''Probably a misprint, please, try again. Just type WOW!''')

        roll1 = input().strip('!.').lower()
#################################################        
## Function game which is called when necessary to start the game
def game():
    # prompting the user to roll the dice and storing the sum of two dice values
    roll()
    answer1 = dice()
# storing some strings to use later
    loseString7 = "Sorry for you, it's 7. You lose, we win!!!"
    loseString = "Sorry for you. You lose, we win!!!"
    winString = "Congratulations, you win!!!"
# checking if the user wins or loses immediately, or he/she needs 
# to continue rolling dice
    if answer1 in (7,11):
        return print(winString)
    elif answer1 in (2,3,12):
        return print(loseString)
    else: 
        print(f"Now your goal number is {answer1}. Soooo, we continue playing.")
# rolling the dice for the second time and storing the sum in answer2
        roll()
        answer2 = dice()
        if answer2 == 7: # checking if lose
            return print(loseString7)
        else:
# rolling dice until the sum is the same as the sum of dice for the first roll            
            while answer2 != answer1: 
                print(f"Now your goal number is {answer1}. Soooo, we continue playing.")
                roll()
                answer2 = dice()
                if answer2 == 7: # if sum is 7, then lose
                    print(loseString7)
                    return
            print("Aaaaand ... you win!!!")
            return

#################################################

print("Ready to play CRAPS? Let's go!")
game()

# checking if the user wants to play again

print('Hope you enjoyed the game. Wanna play again? y/n')
answer = input().strip('es!.').lower()
while answer == 'y':
    game()
    print('Hope you enjoyed the game. Wanna play again? y/n')
    answer = input().strip('es!.').lower()
else:
    if answer =='n':
        print('Sorry you leave.')