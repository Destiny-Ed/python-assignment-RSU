#Write a program that will accept and compute the sum of odd numbers 
#between 1 and 100 inclusive

#Solution

#........................................................................
#Psuedo Code 
#........................................................................

#1#Declare a function
#2#Wrap all statement in the function inside try...except to handle any form of exception

#3# Input a number between 1 and 100 inclusive from a user and save as maximunNumb
#4# If maximumNumb is not a valid number. then restart program .............

#5# Declare a variable oddSum to store the total sum and first initialize it to 0
#6# While maximumNumb is less than 1 or greater than 100 ask user to input a number again

#7# Iterate through the maximumNumb by checking for the difference with 1
#8# Use control structure to check whether the difference is an odd numbers
#9# Compute the odd numbers and store then to the oddsum
#10# Output the oddSum which now contains the sum of all numbers



def callFunction():
    try:
        maximumNumb = int(input("Enter a valid number : "))
        oddSum = 0

        while maximumNumb > 100 or maximumNumb < 1:
            maximumNumb = int(input("Enter a number between 1 and 100 inclusive :"))


        for numbers in range(1, maximumNumb + 1):
            if(numbers % 2 == 1):
                print("Odd number " + str(numbers))
                oddSum = oddSum + numbers
                
        print("The sum of the odd numbers : " + str(oddSum) )
    except ValueError as _:
        print("Value entered is not a number. Try again...")
        callFunction()


callFunction()


#===================================================================================
#Flow chart
#===================================================================================

        