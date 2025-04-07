#Write a function that takes as input number of dice and number of sides. The function will then return a list
#of randomly generated numbers in the proper count and range. For example if the the function is asked to generate
#3D6 or three sixed sided dice, then a potential output would be [2,2,6]
#This function cannot have any input or print statements.
#Write supporting code that will as the user for number of dice and sides, call the function, then report the results.
#The function should not be called if number of dice is zero or less and instead should report bad input to the user
#The function should not be called if number of sides is 1 or less and instead should report bad input to the user
#Sample outputs (your text does not have to match exactly)
import random 
random.seed() #Gets that engine running

#Defaults inputs to zero before user inputs(advised)
number_of_Dice = 0
sides_of_Dice = 0

def diceroll(number_of_Dice, sides_of_Dice): #Function for inputs
    dice_result = [] #Start with an empty list
    for i in range(number_of_Dice): #Loop for dice roll
        roll = random.randint(1, sides_of_Dice) #Uses the random.seed
        dice_result.append(roll) #Building the list result
    return dice_result

#NEWish-While loop to run the code
while True:
    try:
        #User input and integer conversion
        number_of_Dice = int(input("How many dice are you rolling? "))
        sides_of_Dice = int(input("How many sides on the dice? "))
        if number_of_Dice <= 0: #Did they follow the rule?
            print("Dice must be greater than 0, try again")
            continue #Skips to the next step
        elif sides_of_Dice <=1:
            print("Sides must be greater than 1, try again")
            continue #Skips to the next step
        final = diceroll(number_of_Dice, sides_of_Dice) #Congrats you're rolling dice
        final_result = ", ".join(str(num) for num in final) #Collecting those results and adding a comma to make it all pretty
        print(f"You rolled {number_of_Dice} dice and chose {sides_of_Dice} sides. Resulting in: {final_result}") #Its the result of all of this

        again = input("Want to try again(y/n): ").lower()#NEWish-Cycles through asking "continue"Note:.lower() converts all to lower case
        if again != "y": #IF! they answer y it will prompt again
            break 

    except ValueError: #NEW-Creates an exception allowing the function to continue
        print("Numbers unless otherwise specified") #If they do not want to give integers


