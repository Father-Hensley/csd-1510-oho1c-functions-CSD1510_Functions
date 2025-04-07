#Write a function that takes two parameters: a prompt message and an error message.
#The function will prompt the user with the passed in prompt to enter an integer
#If the text entered cannot be cast to an int, display the error message.
#The function will continue to prompt the user to enter an integer until a proper integer is entered.
#The most direct way of doing this would be using a try block, which has not been covered yet. You will need to research this.
#Write supporting code to call the function, and then display the number that was entered.

def get_int(pmessage, emessage): #This is the fuction
    while True: #While loop focusing on true statements
        try: #NEW-Allows the program to continue running with a known error
            x = int(input(pmessage)) #Informs for an input. Set for an integer
            return x #return value for x
        except ValueError: #NEW-Creates an exception allowing the function to continue
            print(emessage)

integer = get_int("Enter a number: ", "Do you know what a number is?") #Like a print statement. Gives the prompt to the user
print(f"{integer} is what you entered") 