#This is a teacher led demo.
#Watch this video or follow along in class.

def AddTwoNumbers(number1, number2): #Function that returns the sum of two variables
    result = number1 + number2
    return result 

def PrintHelloTen(): #Function looping 10 times
    for _ in range(10):
        print("Hello")
x = 5 #Variables
y = 10
result = AddTwoNumbers(x,y) #Calling def function and keeping the result


print(result) #Prints AddTwoNumbers function

PrintHelloTen() #Calling def function to print hello 10 times